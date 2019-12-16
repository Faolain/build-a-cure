from utils import *

def find_metrics(pattern, lines, row, all_vars):
    '''
    find any metrics in this pattern's matches
    to do: some metrics will have letters other than expected
    pull all the alphanumeric strings & filter out dose information
    '''
    metrics = set()
    split_line = pattern.split(' ') if pattern is not None else []
    for i, word in enumerate(split_line):
        numbers = [w for w in word if w.isnumeric()]
        if len(numbers) > 0:
            if len(numbers) == len(word):
                next_word = split_line[i + 1] if (i + 1) < len(split_line) else ''
                if len(next_word) < 5:
                    # to do: add extra processing rather than assuming its a unit of measurement
                    metrics.add(word)
                    metrics.add(next_word) # '3 mg'
            else:
                metrics.add(word) # '3mg'
    return metrics

def find_modifiers(pattern, lines, row, all_vars):
    '''
    - we're isolating modifiers bc theyre the smallest unit of 
        functions (inputs, process, outputs)
        which can be embedded in phrases, clauses, and sentences
    - we wouldnt add noun modifiers which imply an action in the past which wont be repeated:
        "protein isolate"
    - only verb modifiers which imply an action in the present to indicate ongoing relevant functionality:
        "ionizing radiation", "ionizer of radiation"
    - noun modifiers should be indexed as phrases, so get_phrases has to be called before this function
    - use cardinal numbers to get metric modifiers
    - apply pattern_map functionality first if it can replace patterns in modifiers 
    - otherwise continue with below logic
        convert "x subset_keyword y" to "y x"
        subset_keywords = ['of', 'in', 'from']
            "item in list" => "list item"
            "inhibitor of x" => "x-inhibitor"
    - change words to their stem and get the pos of their stem 
      "x has effect of membrane disruption" is a modifier pattern: "x has function of noun noun" 
      "x has function of noun1 noun2": "x noun1 noun2 function"
      but the second noun is a conjugation of a verb "disrupt" so should be converted to 
      "x disrupts membranes"
    '''
    ''' takes out determiners if indicating 'one', 'some', or 'same' quantity '''
    modifier = None
    modified = None   
    tagged_dict = {} 
    blob_dict = {}
    words = subset.split(' ')
    tagged = pos_tag(word_tokenize(subset))
    if tagged:
        for item in tagged:
            tagged_dict[item[0]] = item[1]
        blob = get_blob(subset)
        if blob:
            blob_tokens = blob.parse()
            if blob_tokens:
                for token, val in blob_tokens.items():
                    blob_dict[token] = val.split('/')
        if tagged_dict and blob_dict:
            for i, word in enumerate(words):
                pos = row['word_map'][word] if word in row['word_map'] else ''
                if pos:
                    if pos not in all_vars['pos_tags']['exclude']:
                        if word in blob_dict and word in tagged_dict:
                            #if blob_dict[word][0] != tagged_dict[word]:
                            ''' ntlk and blob tags differ: nltk: 'imaging' => 'VBG' blob: 'imaging' => 'NN', 'B-NP', 'I-PNP' '''
                            modifier = word
                            other_word = words[i + 1] if (i + 1) < len(words) else words[i - 1] if i > 0 else None
                            if other_word:
                                other_word_pos = row['word_map'][other_word] if other_word in row['word_map'] else ''
                                if other_word_pos in all_vars['pos_tags']['ALL_N'] or other_word_pos in all_vars['pos_tags']['ALL_V']:
                                    row['modifiers'].add(' '.join([ratio, other_word]))
        return row
    return False

'''
    - clauses are relationships between subject and objects in line

    - this function:
        1. separates the line by subjects
            1. identifies operators
            2. formats the line into a set of clauses for each subject, organized by operator logic
            3. deconstructs the sentence based on operator logic so its represented by order of operations
                - applies operator logic to clauses to produce alternative relationships:
                    - "x was b even with a" means a is irrelevant, so it should produce the relationships:
                        "x was b"
                        "a does not impact (x was b)"

                    - "x was a and was b" should produce:
                        clause "x was (a and b)"
                        relationship "x was a"
                        relationship "x was b"
                        variable "(a and b)"

                    - "x was a and therefore b"
                        clause "x was a so b"
                        relationship "a therefore b"
                        relationship "x leads to b"
                        variable "(a so b)"

                    - "subject verb even with x or y" should produce:
                        - "subject verb even with x"
                        - "subject verb even with y"

    - once you identify modifiers, identifying clauses is mostly a matter of 
        identifying subjects and operators (and, because, ',')
        
    - retrieved clauses should be:
        a list separated by subjects, containing the acting subject, verb, & object:
            clauses = ['chemical', 'caused', 'reaction'], ['experiment', 'was', 'successful']]

    - converts a sentence like: 
            "in the event of onset, symptoms appear at light speed, even if you take vitamin c at the max dose"
        to reduced ordered form:
            "symptoms appear quickly even with vitamin c max dose"
        because:
            "in the event of onset" == low meaning clause
            "at light speed" => reduced to "quickly"
            "you take" => ""
                it's implied that a patient will be taking the medicine so it doesnt need to be stated
            "vitamin c at the max dose" => modifier pattern "max dose vitamin c"
            "noun1 noun2 at the noun3 noun4" => "noun3 noun4 noun1 noun2"
            "phrase1 at the phrase2" => "phrase2 phrase2"
    conditional_keys = ['C', 'P', 'ADV', 'ADJ', 'verb_potential']
    pos_tags['conditional'] = []
    for tag in conditional_keys:
        pos_tags['conditional'].extend(pos_tags[tag])

    relation_keys = ['C', 'P']
    pos_tags['relation'] = []
    for tag in relation_keys:
        pos_tags['relation'].extend(pos_tags[tag])
'''

def rearrange_sentence(line, all_vars):
    '''
        line = 'x was y even with a' => 
        separate by clause_delimiters:
            ['x was y', 'even with', 'a']
        isolate clauses having embedded relationships with parenthesis:
            (if clause contains verb or verb-modifier)
            '(x was y) even with a'
        replace with clause_map operators:
            '(x equal y) independent a'
        replace with symbolic operators:
            '(x = y) # a'
        }
        now you can generate the relationships based on operator logic stored in our pattern_maps: 
        '(x = y) # a': [
            '(x = y) # a',
            '(x = y) # a',
            'a (x = y) # a'
        ]

        get_relationships('(x = y) # a') = [
            'x is y',
            'x is y even with a',
            'a cannot prevent (x is y)'
        ]
        we would store multiple patterns for the independence relationship, 
        because a is an object and would therefore be a subject (acting agent) in some relationships, 
        so we want to index that too, even though it seems like a duplicate
        if a is a treatment, we definitely want the relationship:
            "treatment a cannot prevent symptom x from being symptom y"
            indexed with treatment a as the subject
    '''
    split = line.split(',')
    clauses = []
    clauses = [
        "in the event of onset",
        "symptoms appear",
        "at light speed", 
        "even if you take vitamin c",
        "at the max dose"
    ]
    ordered_clauses = order_clauses(clauses)
    meaningful_clauses = filter_clauses(ordered_clauses)
    meaningful_clauses = [
        "symptoms appear",
        "quickly", 
        "even with",
        "vitamin c",
        "max dose"
    ]
    converted_clauses = convert_clauses(meaningful_clauses)
    converted_clauses = [
        "symptoms appear",
        "quickly", 
        "independently of",
        "vitamin c",
        "max dose"
    ]
    line = ' '.join(converted_clauses)
    return False

def split_by_relevance(line, word_map, all_vars):
    ''' this function should split a line by det and prep '''
    ''' include splitting by parentheis & clause delimiters '''
    new_subsets = []
    words = line.split(' ')
    new_subset = []
    for w in words:
        pos = word_map[w] if w in word_map else ''
        for key in ['N', 'V', 'verb_keywords', 'ADV', 'ADJ']:
            pos_list = all_vars['pos_tags'][key]
            if pos in pos_list:
                new_subset.append(w)
            else:
                new_subsets.append(new_subset)
                new_subsets.append(w)
                ''' add any DCP in their own item '''
                new_subset = []
        if new_subset:
            new_subsets.append(new_subset)
    if new_subsets:
        return ' '.join(new_subsets)
    return False

def get_conditionals(row, all_vars):
    row['line'], row['clauses'] = rearrange_sentence(row['line'], all_vars)
    sentence_pieces = [] # break up sentence by verbs
    sentence_piece = []
    for w in row['line'].split(' '): 
        if len(w) > 0:
            if '(' in w:
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_piece = [w.replace('(', '')]
            elif ')' in w:
                sentence_piece.append(w.replace(')', ''))
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_piece = []
            elif w not in row['verbs']:
                sentence_piece.append(w)
            else:
                sentence_pieces.append(' '.join(sentence_piece))
                sentence_pieces.append(w) # add the verb separately
                sentence_piece = []
    for j, s in enumerate(sentence_pieces):
        s_split = s.split(' ') if type(s) == str else s
        for i, word in enumerate(s_split):
            if word in row['verbs']:
                prev_object = False if i < 1 else get_object_by_position(i, s_split, 'prev', row['nouns'], row['phrases'])
                prev_object = sentence_pieces[j - 1] if prev_object is False and j > 0 else prev_object
                next_object = False if i == (len(sentence_pieces) - 1) else get_object_by_position(i, s_split, 'next', row['nouns'], row['phrases'])
                next_object = sentence_pieces[j + 1] if next_object is False and j < (len(sentence_pieces) - 1) else next_object
                if active:
                    if prev_object:
                        row['subjects'].add(prev_object)
                        if next_object:
                            row['clauses'].add(' '.join([prev_object, word, next_object]))
                else:
                    # to do: handle other cases where infinitive is linguistically awkward bc clauses will be re-used later
                    if next_object:
                        row['subjects'].add(next_object)
                        if prev_object:
                            row['clauses'].add(' '.join([next_object, word, prev_object]))

    ''' assumes rearrange_sentence was already called on line used to generate clauses '''
    print('\nclauses', row['clauses'])
    row['functions'].add(word) # relationships = treatments, intents, functions, insights, strategies, mechanisms, patterns, systems
    row['components'].add(word) # compounds, symptoms, treatments, metrics, conditions, stressors, types, variables
    row['conditionals'] = []
    row['subjects'] = []
    row['verb_relationships'] = []
    row['delimiters'] = []
    all_vars['clause_delimiters'].append('1')
    for i, c in enumerate(row['clauses']):
        c_strip = c.strip()
        if i == 0:
            items['subject'] = c_strip
        else:
            words = c_strip.split(' ')
            is_a_condition = is_condition(words, row, all_vars)
            if is_a_condition:
                ''' is_a_condition has the next important word in condition '''
                pos = row['word_map'][is_a_condition] if is_a_condition in row['word_map'] else ''
                if pos:
                    if pos not in all_vars['pos_tags']['ALL_V']:
                        for j, w in enumerate(words):
                            if w in all_vars['clause_delimiters']:
                                items['delimiters'].append(w)
                                remainder = ' '.join([x for x in words if words.index(x) >= j])
                                if w == words[-1]:
                                    ''' the delimiter is the last word in this clause '''
                                    remainder = ' '.join([x for x in words if words.index(x) < j])
                                if remainder not in items['conditional']:
                                    items['conditional'].append(remainder)
                            else:
                                if c_strip not in items['conditional']:
                                    items['conditional'].append(c_strip)
                    else:
                        for w in words:
                            if w in all_vars['clause_delimiters']:
                                items['delimiters'].append(w)
                                words.remove(w)
                        if c_strip not in  items['verb_relationships']:
                            items['verb_relationships'].append(c_strip)
            else:
                if c_strip not in items['conditional']:
                    items['conditional'].append(c_strip)
    ''' at this point items represents a sentence broken into: 
        items = {
            "subject": "x",
            "verb_relationships": "is y",
            "delimiter": "even when",
            "condition": "z"
        }
    '''
    print('\nconditionals', items)
    return items
    
def get_object_by_position(index, sentence_pieces, position, check_list, phrases):
    relevant_piece = sentence_pieces[index - 1] if position == 'prev' else sentence_pieces[index + 1] if index < (len(sentence_pieces) - 1) else ''
    if relevant_piece != '':
        sequenced_words = relevant_piece.split(' ') if position == 'next' else relevant_piece.split(' ').reverse()
        for w in sequenced_words:
            phrase_string = ' '.join(phrases)
            if w in phrase_string:
                for phrase in phrases:
                    for i, phrase_word in enumerate(phrase.split(' ')):
                        if phrase_word == w and i == 0:
                            ''' this is the first word in a phrase so get the whole phrase '''
                            return phrase
            elif w in check_list: # check that its in the check_list passed in before returning it
                return w
    return False