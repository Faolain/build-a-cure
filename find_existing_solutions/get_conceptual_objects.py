''' 
these functions do more advanced linguistic processing than 
keyword or pattern matching as in identify_elements 
'''

def find_article_intents(article, av):
    '''
    this function is checking for any purpose-related keywords
    to find priority data of bio components, 
    like 'bacteria seek to optimize efficiency' would return 'efficiency'

    if something (object, process, attribute) is a known output of a function, 
        its assumed to be the intent

    this should capture the core intent which should be one of the supported intents
    all intents are inherently relationships so most could be standardized to:
     'find', 'test', 'build', 'compare', or 'verify'

    but you want to find which one fits more given their subtle differences
    for example:
        - 'test' indicates a known relationship was tested
        - 'find' indicates a new relationship was tested

        - 'verify' indicates replication of a research object (result, study)
        - 'compare' indicates analysis of related research objects (study/study, result/protocol)

        - 'build' contains instructions on how to synthesize something
        - 'find' would indicate info about a relationship between the input & output in the study, 
            but not necessarily include the instructions

    for studies that have a 'test' intent (to confirm a theorized relationship),
        the relationship youre trying to find is between:
         'method'/'compound' and 'success'/'failure'
    for other studies that are exploratory (to find a new relationship),
        the relationship may be to find correlation between two medical factors:
        'condition' and 'treatment' or 'condition' and 'symptom' or 'treatment' and 'symptom'
    '''
    intents = []
    for line in article.split('\n'):
        intent = find_intent(line)
        if intent:
            intents.append(intent)
    if len(intents) > 0:
        return intents
    return False

def find_key_sentences(article, av):
    '''
    key_sentences should have an item from each sentence_type that is relevant to the study intent
    '''
    key_sentences = {}
    intents = get_article_intents(article)
    if intents:
        key_sentences['intent'] = ','.join(intents)
    for line in article.split('\n'):
        sentence_type = get_sentence_type(line)
        if sentence_type:
            key_sentences[sentence_type] = line
    return key_sentences

def find_sentence_type(line, av):
    ''' out of sentence_types, determine which this is likeliest to be 
    to do: 
    - implement keyword check for each sentence type
    - add linguistic patterns for each sentence type
    '''
    sentence_types = {
        'hypothesis': [],
        'assumption': [],
        'test': [],
        'intent': [],
        'instruction': [],
        'function': [], # describing processes
        'result': [], # conclusion
        'treatment': []
    }
    sentence_type_values = [ x for k, v in sentence_types.items() for x in v ]
    elements = get_elements(line)
    element_sentence_pattern = ' '.join(elements)
    for k, v in sentence_types.items():
        if element_sentence_pattern in v:
            return k
    return False

def find_hypothesis(article):
    '''
    with an overall intent like 'diagnose',
    if its relevant to the hypothesis of the study
    '''
    intents = ['diagnose', 'check_correlation', 'find_limit', 'evaluate_method']
    return article

def find_fact(subset, row, av):
    ''' function to identify common article intents to identify false info '''
    return row

def find_topic(subset, row, av):
    '''
      this function will be used in remove_unnecessary_words
      to filter out words that are either non-medical or too specific to be useful (names)

      test cases:
          permeability => ['structure']
          medicine => ['medical']
          plausibility => ['logic']
    '''
    topics = ['structural', 'logical']
    return row

def find_variable(subset, row, av):
    ''' use this to determine parameters for synthesis function too '''
    ''' variables are the inputs to functions '''
    ''' this can mean the subject of a sentence, or the inputs of that subject (resources, context) '''
    return row

def find_element(subset, row, av):
    elements = []
    for word in line.split(' '):
        index_type = get_index_type(word)
        if index_type:
            if index_type not in index_scores:
                elements.append(index_type)
            else:
                elements.append(index_type)
        else:
            elements.append(word)
    return elements

def find_causal_layer(subset, row, av):
    return row

def find_intent(subset, row, av):
    intents = {}
    row = get_structural_metadata(line, av)
    if row:
        if 'noun' in row:
            for n in row['noun']:
                functions = get_functions(n)
                if functions:
                    for f in functions:
                        if 'output' in f:
                            if n not in intents:
                                intents[n] = []
                            intents[n].append(f['output'])
                related_components = get_related_components(n)
                if related_components:
                    for rc in related_components:
                        functions = get_functions(n)
                        if functions:
                            for rcf in functions:
                                if 'output' in rcf:
                                    if n not in intents:
                                        intents[n] = []
                                    intents[n].append(rcf['output'])
    return intents
    
def find_function(subset, row, av):
    ''' for fluconazole, this should be: "antifungal", "inhibits cyp3a4" '''
    return False

def find_strategy(subset, row, av):
    '''
     - get the strategy explaining why this method worked or failed for the intent, 
        which may be equal to the mechanism of action, 
        so you can do searches for other compounds with similar activity

     - these are processes used by an organism or used on a compound

    - strategies are the reason for success/failure of a method/treatment, including processes & mechanisms of action
        - "this structure on the compound tears the cell barrier"
        - "induces apoptosis by depriving it of contrary signals"
        - "chlorpromazine increases valproic acid levels, which can be derived from valerian (valerian suppressed cyp3a4), 
        which is a function in common with other compounds with activity against pathogen x"

    - drugs need a way to handle common mutation strategies of pathogens
      - up regulating CDR genes
      - reduced sensitivity of the target enzyme to inhibition by the agent
      - mutations in the ERG11 gene, which codes for 14α-demethylase. 
        These mutations prevent the azole drug from binding, 
        while still allowing binding of the enzyme's natural substrate, lanosterol
    '''
    # initial treatment output should be: ['fluconazole', 'itraconazole', 'sertraline', 'thymol', 'carvacrol', 'peppermint']
    # type output should be: ['azole', 'essential oils from plant genus x']
    # functional output should be: inhibitors of cyp3a4, cyp2c19, cyp2c9, filtered by interference with fluconazole
    return row

def find_insight(subset, row, av):
    '''
    - insights in a article doc are more likely to:
    - have more topic-related keywords
    - have a causation verb (induces, associated) - add function to identify causation verbs
    - relate to intents important to agents (health, avoid illness)
      - "saturated fat intake induces a cellular reprogramming that is associated with prostate cancer progression and lethality"
      https://medicalxpress.com/news/2019-11-high-fat-diet-proven-fuel-prostate.html
      - "The presence of many disulfide bonds making this a possible site for oxidative inactivation by ozone"
      https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4927674/
      - add filtering of insights to apply directly to the topic of the problem space of the target condition or mechanisms requested in metadata
    '''
    return row

def find_fallacy(subset, row, av):
    '''
    Argument to moderation (false compromise, middle ground, fallacy of the mean, argumentum ad temperantiam) – assuming that the compromise between two positions is always correct.[16]
    Continuum fallacy (fallacy of the beard, line-drawing fallacy, sorites fallacy, fallacy of the heap, bald man fallacy) – improperly rejecting a claim for being imprecise.[17]
    Suppressed correlative – a correlative is redefined so that one alternative is made impossible.[18]
    Definist fallacy – involves the confusion between two notions by defining one in terms of the other.[19]
    Divine fallacy (argument from incredulity) – arguing that, because something is so incredible or amazing, it must be the result of superior, divine, alien or paranormal agency.[20]
    Double counting – counting events or occurrences more than once in probabilistic reasoning, which leads to the sum of the probabilities of all cases exceeding unity.
    Equivocation – the misleading use of a term with more than one meaning (by glossing over which meaning is intended at a particular time).[21]
        Ambiguous middle term – a common ambiguity in syllogisms in which the middle term is equivocated.[22]
        Definitional retreat – changing the meaning of a word to deal with an objection raised against the original wording.[1]
        Motte-and-bailey fallacy – the arguer conflates two positions with similar properties, one modest and easy to defend (the "motte") and one much more controversial (the "bailey"). The arguer advances the controversial position, but when challenged, they insist that they are only advancing the more modest position.[23][24][25]
        Fallacy of accent – a specific type of ambiguity that arises when the meaning of a sentence is changed by placing an unusual prosodic stress, or when, in a written passage, it is left unclear which word the emphasis was supposed to fall on.
        Persuasive definition – a form of stipulative definition which purports to describe the "true" or "commonly accepted" meaning of a term, while in reality stipulating an uncommon or altered use. (See also the if-by-whiskey fallacy, below)
    Ecological fallacy – inferences about the nature of specific individuals are based solely upon aggregate statistics collected for the group to which those individuals belong.[26]
    Etymological fallacy – reasoning that the original or historical meaning of a word or phrase is necessarily similar to its actual present-day usage.[27]
    Fallacy of composition – assuming that something true of part of a whole must also be true of the whole.[28]
    Fallacy of division – assuming that something true of a thing must also be true of all or some of its parts.[29]
    False attribution – an advocate appeals to an irrelevant, unqualified, unidentified, biased or fabricated source in support of an argument.
    Fallacy of quoting out of context (contextotomy, contextomy; quotation mining) – refers to the selective excerpting of words from their original context in a way that distorts the source's intended meaning.[30]
    False authority (single authority) – using an expert of dubious credentials or using only one opinion to sell a product or idea. Related to the appeal to authority (not always fallacious).
    False dilemma (false dichotomy, fallacy of bifurcation, black-or-white fallacy) – two alternative statements are held to be the only possible options when in reality there are more.[31]
    False equivalence – describing a situation of logical and apparent equivalence, when in fact there is none.
    Feedback fallacy - in the context of performance appraisal, the belief in the accuracy of feedback, despite evidence that feedback is subject to large systematic errors due to the idiosyncratic rater effect.[32]
    Historian's fallacy – the assumption that decision makers of the past viewed events from the same perspective and had the same information as those subsequently analyzing the decision.[33]
    Historical fallacy – a set of considerations is thought to hold good only because a completed process is read into the content of the process which conditions this completed result.[34]
    Homunculus fallacy – a "middle-man" is used for explanation; this sometimes leads to regressive middle-men. Explains without actually explaining the real nature of a function or a process. Instead, it explains the concept in terms of the concept itself, without first defining or explaining the original concept.
    Inflation of conflict – arguing that if experts of a field of knowledge disagree on a certain point, the experts must know nothing, and therefore no conclusion can be reached, or that the legitimacy of their entire field is put to question.[37]
    If-by-whiskey – an argument that supports both sides of an issue by using terms that are selectively emotionally sensitive.
    Incomplete comparison – insufficient information is provided to make a complete comparison.
    Inconsistent comparison – different methods of comparison are used, leaving a false impression of the whole comparison.
    Intentionality fallacy – the insistence that the ultimate meaning of an expression must be consistent with the intention of the person from whom the communication originated (e.g. a work of fiction that is widely received as a blatant allegory must necessarily not be regarded as such if the author intended it not to be so.)[38]
    Ludic fallacy – the belief that the outcomes of non-regulated random occurrences can be encapsulated by a statistic; a failure to take into account that unknown unknowns in determining the probability of events taking place.[39]  - spin, system
    McNamara fallacy (quantitative fallacy) – making a decision based only on quantitative observations, discounting all other considerations.
    Mind projection fallacy – subjective judgments are "projected" to be inherent properties of an object, rather than being related to personal perceptions of that object.
    Moving the goalposts (raising the bar) – argument in which evidence presented in response to a specific claim is dismissed and some other (often greater) evidence is demanded.
    Nirvana fallacy (perfect-solution fallacy) – solutions to problems are rejected because they are not perfect.
    Prosecutor's fallacy – a low probability of false matches does not mean a low probability of some false match being found.
    Proving too much – using a form of argument that, if it were valid, could be used to reach an additional, invalid conclusion.
    Psychologist's fallacy – an observer presupposes the objectivity of their own perspective when analyzing a behavioral event.
    Referential fallacy[40] – assuming all words refer to existing things and that the meaning of words reside within the things they refer to, as opposed to words possibly referring to no real object or that the meaning of words often comes from how they are used.
    Reification (concretism, hypostatization, or the fallacy of misplaced concreteness) – a fallacy of ambiguity, when an abstraction (abstract belief or hypothetical construct) is treated as if it were a concrete, real event or physical entity. 
    Retrospective determinism – the argument that because an event has occurred under some circumstance, the circumstance must have made its occurrence inevitable.
    Special pleading – a proponent of a position attempts to cite something as an exemption to a generally accepted rule or principle without justifying the exemption.
    '''
    return row

def find_assumption(subset, row, av):
    return row

def find_counterexample(subset, row, av):
    '''
    assumption counterexamples:
      1. "smile formulas are generally under 100 char"
        - wiki for smiles doc has 240-char compound formula: https://en.wikipedia.org/wiki/Simplified_molecular-input_line-entry_system
      2. "structure is a good mechanism for deriving function"
        - bakuchiol has example of structural difference with similar function:
        https://en.wikipedia.org/wiki/Bakuchiol
      3. "wiki articles of related compounds will mention each other"
        - sertraline wiki doesnt mention interaction with fluconazole 
          - youd have to derive by noting that it increased blood level/metabolism of substrates some CYP 450 enzymes inhibited by fluconazole
          - or that it is metabolized by some of the same enzymes
          - https://en.wikipedia.org/wiki/Sertraline#Overdose
    '''
    return row

def find_priority(subset, row, av):
    return row 

def find_core_function(subset, row, av):
    return row

def find_dependency(subset, row, av):
    ''' 
    this should return a list of outputs, n operations away

    - relationships is a list of lists containing ordered causal relationships
    - io_type is 'input' or 'output'

    outputs = get_outputs('nutrient', [['nutrient', 'stomach', 'liver', 'digestive system', 'amino acid']], 3)
    outputs should be:
        [['stomach', 'liver', 'digestive system']]
    '''
    dependencies = []
    return dependencies

def find_impact(subset, row, av):
    '''
        function to combine functions by intent:
          - if you have these two functions:
                - switch on process A
                - switch off processing of B which creates input for process A
          - the output intent is:
                - neutralize process A (assuming the two functions are equal in power)
    '''
    impact = None
    for f in functions:
        f_impact = get_verb_impact(f, object_name, av)
        if f_impact:
            if impact:
                if not impact_match(f_impact, impact, object_name, av):
                    impact = update_impact(f_impact, impact, object_name, av)
            else:
                impact = f_impact
    if impact:
        return impact
    return False

def impact_match(f_impact, impact, object_name, av):
    return f_impact

def update_impact(f_impact, impact, object_name, av):
    return f_impact

def get_verb_impact(function, object_name, av):
    '''
    - function='this compound activates b', object_name='b'
        should return a standard verb like 'activate', 'enable'
    - the object_name is the subject of the sentence
        - make sure the impact verb is acting on that subject so switch if its passive 
    '''
    if object_name in function:
        row = get_structural_metadata(function, av)
        if row:
            if 'verb' in row:
                for v in row['verb']:
                    if v in av['supported_synonyms']:
                        return av['supported_synonyms'][v]
    return False
