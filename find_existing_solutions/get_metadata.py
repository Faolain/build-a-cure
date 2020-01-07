import wikipedia
from wikipedia.exceptions import DisambiguationError
import xml.dom.minidom

from get_pos import *
from get_vars import *
import get_medical_objects
import get_structural_objects
import get_conceptual_objects
from get_medical_objects import *
from get_structural_objects import *
from get_conceptual_objects import *

def get_data_store(index, database, operation, args):
    '''
    this assembles an index or retrieves it from local storage,
    filtering by object_types found in the metadata argument
    '''
    downloaded = downloads(['data', 'datasets'])
    if not downloaded:
        return False
    av = get_vars()
    if av:
        data_store = {}
        ''' if index or database not passed in, fetch the local db if it exists '''
        args, filters, metadata, generate_target, generate_source = get_args(args, av)
        av['metadata'] = metadata if metadata else av['supported_params']
        if operation == 'build':
            database = get_local_database('data', None) if not database else database
            data_store, rows = build_indexes(database, args, filters, av)
        elif operation == 'get_database':
            data_store = get_local_database('data', None)
        elif operation == 'get_index':
            data_store = index
        if data_store and metadata:
            new_index = {}
            for key in metadata:
                new_index[key] = data_store[key] if key in data_store else set()
            if new_index:
                return new_index
    return False

def get_data_from_source(source, keyword, av):
    data = {}
    total = 0
    max_count = 10
    for i in range(0, 10):
        start = i * max_count
        if total > start or total == 0:
            url = source['url'].replace('<KEY>', keyword).replace('<START>', str(start)).replace('<MAX>', str(max_count))
            print('url', url)
            response = requests.get(url)
            if response.content:
                articles = {}
                if source['response_format'] == 'xml':
                    xml_string = xml.dom.minidom.parseString(response.content)
                    if xml_string:
                        count_tag = xml_string.documentElement.getElementsByTagName(source['count'])
                        total = int(count_tag[0].childNodes[0].nodeValue)
                        articles = xml_string.documentElement.getElementsByTagName(source['entries'])
                else:
                    articles = json.loads(response.content)
                if len(articles) > 0:
                    data = process_articles(entries, data, source, av)
    if data:                                         
        return data
    return False

def process_articles(articles, data, source, av):
    for article in articles:
        title = get_text_from_nodes(article, source['title_element'])
        article_text = get_text_from_nodes(article, source['summary_element'])
        if title and article_text:
            article_lines, av = standard_text_processing(article_text, av)
            if article_lines:
                data[title] = article_lines # article_lines[line][word] = pos
    return data

def get_text_from_nodes(entry, element_name):
    nodes = [node for node in entry.childNodes if node.nodeName == element_name]
    if len(nodes) > 0:
        text = ''.join([subnode.wholeText for node in nodes for subnode in node.childNodes])
        if len(text) > 0:
            return text
    return False

def add_row(row, index, empty_index, rows):
    if row:
        if row != empty_index:
            for key, val in row.items():
                if type(val) == dict:
                    row[key] = '::'.join(['_'.join([k,v]) for k,v in val.items()])
                elif type(val) == set or type(val) == list:
                    row[key] = str('::'.join(set(val)))
                elif type(val) == bool:
                    row[key] = '1' if val is True else '0'
                index[key] = index[key].add(row[key])
            rows.append(row)
    return index, rows

def build_indexes(database, args, filters, av):
    ''' 
    - this function indexes data from api providing articles
    - if the local database is found, use that as starting index, otherwise build it
    '''
    rows = []
    empty_index = get_empty_index(av)
    index = database if database else empty_index if empty_index else None
    for arg in args:
        for source in av['sources']:
            data = get_data_from_source(source, arg, av)
            if data:
                for title, article_lines in data.items():
                    for line, word_map in article_lines.items():
                        row = get_metadata(line, title, word_map, av)
                        if row:
                            index, rows = add_row(row, index, empty_index, rows)
    if index and rows:
        write_csv(rows, index.keys(), 'data/rows.csv')
        return index, rows
    return False, False

def get_metadata(line, title, word_map, av):
    ''' 
    this function initializes the row object & populates it with various metadata types:
        - structural_types to get nouns, verbs, phrases, modifiers, clauses, & relationships
        - medical_types to get conditions, symptoms, & treatments in the sentence 
        - conceptual_types to get types, strategies & insights
    '''
    row = get_empty_index(av)                   
    row['line'] = line
    row['word_map'] = word_map
    row['original_line'] = line
    row = replace_names(row, av)
    row = get_similarity_to_title(title, row)
    row = get_structural_metadata(row, av)
    print('\nrow with structural metadata', row)
    for metadata_type in ['medical_types', 'conceptual_types']:
        for object_type in av[metadata_type]:
            if object_type in av['metadata']:
                for search_pattern_key in av['pattern_index']:
                    # check that this data 'strategy', 'treatment' was requested and is supported in pattern_index
                    print('\nget metadata', object_type, search_pattern_key)
                    objects, patterns, av = extract_objects_and_patterns_from_index(index, row, object_type, search_pattern_key, av)
                    if objects:
                        if objects[object_type] != row.keys():
                            row[object_type] = set(row[object_type]).union(set(objects[object_type]))
                    if patterns:
                        joined_key = '_'.join([object_type, search_pattern_key])
                        if joined_key not in row['pattern']:
                            row['pattern'][joined_key] = set()
                        for p in patterns:
                            row['pattern'][joined_key].add(p)
    print('\nmedical objects', row)
    return row

def extract_objects_and_patterns_from_index(index, row, object_type, search_pattern_key, av):
    '''
    - all of your 'find_object' functions need to support params: (subset, row, av)
    - this function is for meta-analysis
        1. find any matches from search_pattern_key patterns in index[object_type]/row[object_type] lines
        2. if pattern matches found in lines, 
            find objects in matches with type-specific logic from find_<object_type> function
        3. if no pattern matches found in lines, 
            find objects in lines with type-specific logic from find_<object_type> function
        for an index or row containing types of elements ('condition', 'symptom', 'strategy')
        this function is for finding patterns in those index types in the input (index or row['line'])
    - object_type is the key in object types supported in av['full_params'] to find:
        ['treatment', 'condition', 'strategy']
    - search_pattern_key is the key of av['pattern_index'] keys to search: 
        ['modifier', 'type', 'role']
    - object_type can equal search_pattern_key
    '''
    patterns = {}
    objects = { object_type: set() }
    index = index if index else row if row else None
    if index:
        if object_type in av['metadata'] or av['metadata'] == 'all':
            lines = [index['line']] if 'line' in index else index[object_type] if object_type in index else [] #index[object_type] if object_type in index else
            for line in lines:
                found_objects_in_patterns, found_patterns, av = get_patterns_and_objects_in_line(line, search_pattern_key, index, object_type, av)
                if found_patterns:
                    patterns = found_patterns
                if found_objects_in_patterns:
                    objects[object_type] = objects[object_type].union(found_objects_in_patterns)
                else:
                    ''' 
                    if there are no matches found for object_type patterns, 
                    do a standard object query independent of patterns to apply type-specific logic 
                    '''
                    found_objects = apply_find_function(object_type, line, index, av)
                    if found_objects:
                        print('find function objects', object_type, found_objects)
                        objects[object_type] = objects[object_type].union(found_objects)
            if objects or patterns:
                print('extracted objects', objects, 'patterns', patterns)
                return objects, patterns, av
    return False, False, av

def get_patterns_and_objects_in_line(line, search_pattern_key, index, object_type, av):
    ''' the reason we allow search_pattern_key and object_type to differ is to find subset matches 
        example: 
            find 'modifiers' in 'treatment patterns' would have:
            object_type = 'modifier' and search_pattern_key = 'treatment'
    '''
    found_objects = set()
    generated_patterns, all_patterns, av = get_all_versions(line, 'all', 'all', av)
    if generated_patterns and all_patterns:
        found_patterns, av = match_patterns(line, search_pattern_key, generated_patterns, all_patterns, av)
        if found_patterns and object_type != 'pattern':
            for pattern_type in found_patterns:
                for pattern, matches in found_patterns[pattern_type].items():
                    ''' filter pattern matches for this type before adding them, with type-specific logic in find_* functions '''
                    ''' note: this is not restricting output to found objects '''
                    for m in matches:
                        objects_found = apply_find_function(object_type, m, index, av)
                        if objects_found:
                            found_objects = found_objects.union(objects_found)
    if found_patterns or found_objects:
        return found_objects, found_patterns, av
    return False, False, av

def apply_find_function(object_type, subset, index, av):
    ''' find functions check for objects of object_type in matches list which match pattern 
        - all find object functions need to support params:
            - subset, row_index, av
                - subsets = 'dog of cat', 'cat of dog' (matches for pattern 'x of y')
    '''
    function_name = ''.join(['find_', object_type])
    if function_name in globals():
        if function_name:
            if get_structural_objects and get_conceptual_objects and get_medical_objects and get_vars:
                function = None
                for package in [get_structural_objects, get_conceptual_objects, get_medical_objects, get_vars]:
                    try:
                        function = getattr(package, function_name)
                    except Exception as e:
                        continue
                if function:
                    got_objects = function(subset, index, av)
                    if got_objects:
                        if len(got_objects) > 0:
                            return set([item for item in got_objects])
    return False

def get_structural_metadata(row, av):
    '''
        1. identifies 'ngram', 'modifier', 'phrase', 'noun_phrase', 'verb_phrase', 'clause', 'subject', 'pattern'
        2. then assembles conditions of sentence & executes order_clauses on conditions
        3. then identifies 'relationship' objects from sentence conditions
        verb-noun-phrases should be converted into modifiers
        once you have the nouns/modifiers, you can pick a subject from the noun or modifier
    '''
    print('\n\nget_structural_metadata', row)
    keep_ratios = ['extra', 'high', 'none']
    corrected_line = correct(row['line'])
    row['line'] = corrected_line if corrected_line else row['line']
    generated_patterns, all_patterns, av = get_all_versions(row['line'], 'all', 'all', av)
    if generated_patterns:
        print('generated_patterns', generated_patterns)
        for pattern_type, patterns in generated_patterns.items():
            if pattern_type not in row['pattern']:
                row['pattern'][pattern_type] = set()
            if len(patterns) > 0:
                for pattern in patterns:
                    print('pattern', pattern)
                    row['pattern'][pattern_type].add(pattern)
    word_pos_line = ''.join([x for x in row['line'] if x in av['alphanumeric'] or x in av['clause_analysis_chars']])
    print('\nword pos line', word_pos_line)
    words = word_pos_line.split(' ')
    new_line = []
    max_words, counts = get_common_words(row['line'], 3, av)
    if max_words and counts:
        row['count'] = counts
        row['common_word'] = max_words
    names = get_names(row['line'])
    if names:
        row['names'] = names
    for i, w in enumerate(words):
        if len(w) > 0:
            pos = row['word_map'][w] if row['word_map'] and w in row['word_map'] else get_nltk_pos(w, av)
            if pos:
                if pos in av['tags']['VC']:
                    row['clause_marker'].add(w)
                if pos in av['tags']['ALL_N'] or w in av['alphabet'] or pos == 'N':
                    ''' format nouns like 'inhibitor' or 'catalyzer' as a verb '''
                    present_verb = conjugate(w, 'VBZ', av)
                    if present_verb:
                        row['verb'].add(present_verb)
                        new_line.append(present_verb)
                    else:
                        row['noun'].add(w)
                        new_line.append(w)
                elif pos in av['tags']['ALL_V'] or pos == 'V':
                    ''' dont conjugate '-ing' to preserve verb-noun modifier phrases '''
                    present_verb = conjugate(w, 'VBZ', av)
                    if present_verb:
                        row['verb'].add(present_verb)
                        new_line.append(present_verb)
                    else:
                        row['verb'].add(w)
                        new_line.append(w)
                elif pos in av['tags']['D'] or pos == 'D':
                    ratio = get_determiner_ratio(w)
                    if ratio:
                        if ratio in keep_ratios:
                            row['det'].add(str(ratio))
                            new_line.append(str(ratio))
                elif pos in av['tags']['P'] or pos == 'P':
                    row['prep'].add(w)
                    new_line.append(w)
                elif pos in av['tags']['C'] or pos == 'C':
                    row['conj'].add(w)
                    new_line.append(w)
                elif pos in av['tags']['ADV'] or pos in av['tags']['ADJ'] or pos == 'ADJ' or pos in av['tags']['ADV'] or pos in av['tags']['ADV'] or pos == 'ADV':
                    row['descriptor'].add(w)
                    new_line.append(w)
                else:
                    row['taken_out'].add('_'.join([w, str(pos)]))
            else:
                if w in av['alphabet']:
                    row['noun'].add(w)
                    new_line.append(w)
    row['line'] = ' '.join(new_line) if len(new_line) > 0 else word_pos_line
    print('\ninterim row', row)
    ngrams = find_ngrams(row['line'], av) # 'even with', 'was reduced', 'subject position'
    if ngrams:
        for k, v in ngrams.items():
            row['ngram'] = row['ngram'].union(v)
    print('\nngrams', row['ngram'])
    structure_types = ['modifier', 'phrase', 'verb_phrase', 'noun_phrase', 'clause']
    for i, key in enumerate(structure_types):
        objects, patterns, av = extract_objects_and_patterns_from_index(None, row, key, key, av)
        if objects:
            print('\n\n\nobjects', key, objects)
            if key in objects:
                if key == 'verb_phrase':
                    for item in objects[key]:
                        new_list = []
                        for w in item.split(' '):
                            pos = get_nltk_pos(w, av)
                            if pos:
                                present_verb = conjugate(w, 'VBZ', av)
                                if present_verb:
                                    new_list.append(present_verb)
                                else:
                                    new_list.append(w)
                            else:
                                new_list.append(w)
                        if len(new_list) > 0:
                            row[key].add(' '.join(new_list))
                elif key == 'subject':
                    for item in objects[key]:
                        row[key].add(item.split(' ')[0]) # to do: remove trailing verb in 'N V' subject pattern
                elif key == 'clause':
                    row[key] = objects[key]
                else:
                    print('objects key', key)
                    if objects[key] != row.keys():
                        row[key] = set(row[key]).union(set(objects[key]))
        if patterns:
            for pattern_type in patterns:
                if pattern_type not in row['pattern']:
                    row['pattern'][pattern_type] = set(patterns[pattern_type])
                else:
                    if len(row['pattern'][pattern_type]) == 0:
                        row['pattern'][pattern_type] = set(patterns[pattern_type])
                    else:
                        row['pattern'][pattern_type] = row['pattern'][pattern_type].union(patterns[pattern_type])
    print('\nafter pattern identification', row)
    '''
    derived_patterns = derive_and_store_patterns(row['line'], av)
    if derived_patterns:
        for ep in derived_patterns:
            if 'derived_patterns' not in row['pattern']:
                row['pattern']['derived_patterns'] = set()
            row['pattern']['derived_patterns'].add(ep)
    '''
    new_row = find_relationship(row['line'], row, av)
    row = new_row if new_row else row
    print('\nafter relationships', row)
    objects, patterns, av = extract_objects_and_patterns_from_index(row, None, 'relationship', 'relationship', av)
    if objects:
        if 'relationship' in objects:
            row['relationship'] = row['relationship'].union(set(objects['relationship']))
        if patterns:
            for pattern_key in patterns:
                if pattern_key not in row['pattern']:
                    row['pattern'][pattern_key] = set()
                row['pattern'][pattern_key] = row['pattern'][pattern_key].union(patterns[pattern_key])
    if row:
        for key in row:
            print('key', key, row[key])
        exit()
        return row
    return False

if sys.argv:
    index = get_data_store(None, None, 'build', sys.argv)
    print('get_data_store:index', index)
