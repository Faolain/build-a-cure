# Summary

- now youve built some powerful functions, some of which need completion, debugging & generalization
    - the important next step is hooking up clause/relationship identification to those functions
    - since those are the foundation for the other more important semantic functions in get_medical_objects and get_conceptual_objects
    - key requirements to complete next:
      - find_type
      - find_definition - can pull from dataset for a type to build definition
      - consolidate pattern identification functions
      - test & update find_clause/relation logic
      - test & update derive_patterns logic to build a full pattern index to implement with clause/relation logic

- the relationships between object type layers (structural, conceptual, medical) means that you can re-use logic across layers:
    - example:
      - stressor identification logic can overlap with change/variance/variable identification logic
    - other type mappings to generalize:
      condition = state, symptom = function = side_effects, function = relationship, synthesis = build process, structure = pattern
    - at some point you need to identify this system of relationships between object types & layers 
      so that generation of additional layer interfaces is possible (physics system, math system, chemical system, in addition to medical/bio system)

- you can work on other tasks for a while before completing relationship/clause/pattern fitting:
  - insight identifier
  - dose prediction for a patient
  - fetch contraindications for a drug (find nth-degree side effects, outputs, high dose impact if not metabolized, conditions, interacting/synergistic/neutralizing drugs)
  - find most common adjacent compound (to make it likeliest that the person can find the common compound and synthesize the version they need)
  - fetch synthesis instructions for a drug from most common adjacent compound
  - treatment component identification function
  - drug reaction predictor
  - compound search from smile formula


# Sources

  - check chembl search if you can search for a condition & return molecules known to treat it
  - chembl similarity function can tell you how likely it is that the generated compound mimics functionality of another compound
  - resolve local_database, get_data_store, derive_pattern, get_data_from_source logic & calls
  - pull these properties for compounds on wiki
  - find source of bio keywords & synonyms


# Structural Objects

  - when evaluating interactions, check for other compounds that interfere with metabolism & de/activation (cytochromes it targets, liver enzymes it assists), 
    which can increase or decrease blood ratio of a drug
  - look for processes/intake of nutrients that could combine to form other compounds (berberine) given the output health factors (stable blood sugar)
  - fix order of assembled combinations:
      get_alts: all_alts [['suppose', 'assumed', 'thought'], ['DT', 'PDT', 'WDT', 'TO', 'PP', 'CC', 'IN'], ' that ', ['suppose', 'assumed', 'thought'], ' that']
      get_all_versions |suppose thought assumed| that DPC |suppose thought assumed| that
  - remove plural tags once you finish singularize function
  - make sure apply_pattern_map explores all versions of line, but returns one new line
  - add common patterns that have more than one index type to all index type lists - 'x of y', 'phrase of phrase', etc
  - identify lists in sentence and surround with parenthesis if embedded or insert as examples of an object ('such as', 'like', 'as in'), 'found in', 'including', 'having'
  - find functions should have definition logic & logic to rule out other types & type-specific logic since they're used as a backup to pattern-matching
    the order of find_* function application can take the place of this, if patterns are comprehensive enough
  - add pattern to standardize verb-subject to subject-verb: 'V DET noun_phrase ... ?' => 'DET noun_phrase V ...'
  - finish function to combine functions by intent get_net_impact(functions) & combined operators
  - verify that if not response false check is same as youve been using

  pattern alts:
  - repeated options shouldnt happen within an alt set: |NNS NNS VBZ2 VBZ3 NNS| 
  - implement pattern-mix matching to mix & match patterns of various types to find key patterns with mixed types not generated by current logic

  processing order:
  - examine iterations (lists/keys()/items()/config/if conditions) that determine processing order: (supported_pattern_variables, pos_tags, all_pattern_version_types, reversed keys, etc)
    - when identifying all objects, order can be from low to high
    - when classifying specific objects, order should be from high to low - return first match, or adjust line being analyzed with replacement for each match, starting with longest matches first
    - add ordered pos-tagging pattern_map to apply preference order to correct incorrectly identified word pos - isolate which tags would be identified as other objects first

  clause identification: 
  - add ordering logic in find_clause for special clause keywords:
    - 'as' can mean 'like', 'while', or 'because'
    - 'by' can indicate a process/mechanism "it works by doing x", "as"

  - support conversion between pos types like 'verb-to-noun':
    - 'subject1 verb clause because subject2 verb clause' => 'subject2 verb-to-noun causes subject1 verb-to-noun'
    - 'the process activated x because y inhibits b' => 'y b-inhibition causes the process to activate x' => 'y b-inhibition enables process to activate x'

  - fix rows csv format & read/save delimiter handling for get_objects - we are storing patterns with 'pattern_match1::match2::match3' syntax for example
  - write function to get semantic props of compounds (bio-availability, activation in the host species, etc) & get_common_property between objects
  - integrate conditions/symptoms and treatments/compounds schemas (this would be a nice way to test get_attribute function to find differentiating props)
  - remove len(0) checks for lists when possible & consolidate excessive chained response checks
  - make sure youre not assigning scores or other calculated numbers as dict keys or other identifiers anywhere 
  - add keyword processing to apply_find_function 

# Functions

  - generating find/build functions:
    - prioritize defining & assembling type definitions, both with configuration & programmatically using various sources
      - find source types from which others can be derived
      - apply get_definition to get the definition of those source types
      - then apply transform function for each pair to generate a find function for a type given the find function of an adjacent type
      - find functions use primarily patterns & definitions
      - create function that uses definition to generate patterns given variable values/types/metadata
      - build functions can also be generated using the type definition
      - after generating, functions should be checked for non-identifying factors that dont differentiate them across types

  - generating apply functions:
    - match/align/fit a structure to another structure

  - standardize terms: shape/structure, model/perspective/filter/standard/interface, intent/method/function/rule, path/route, metadata/attribute/variable/property, object/entity, type/class/category
  - add variable accretion patterns (how an object becomes influenced by a new variable, complex system interaction patterns, etc)
  - add get_common_properties function to do extra property-based searches after identifying objects with extract
  - write function to identify contradictory information (retracted studies, false information, conspiracy theory (anti-vax), opinion) & selecting least likely to be false
    - this will be useful when youre pulling non-research study data, like when youre looking up a metric or compound if you dont find anything on wiki
  - write function to rank & identify authoritative sources (wiki is more trustworthy than a holistic or commercialized blog based on editing metadata)
  - add function to test chemical reactions: https://cheminfo.github.io/openchemlib-js/docs/classes/reaction.html
  - fill in keywords & patterns for objects (strategies/mechanisms used by an organism/on a compound)
  - function to predict a compound for a pathogen/condition requires data:
      - compound & pathogen attributes (compound metadata like metabolism/dose/interactions/effects)
      - variable/state impact (gene expression)
      - interaction rules with expected object types (in the bloodstream if taken orally, in the lungs if inhaled)
      - sub-components that could be altered through interaction to neutralize its functionality
      - dependency scope (volume of layers of relevance)
      - add identification functions:
          - types (['structure', 'life form', 'organic molecule'] from 'protein')
          - topic/problem domain
          - objects (nouns like 'protein')
          - components (topical nouns that are found in another topical component, like organelles of a cell)
          - attributes (attribute metric/feature nouns like 'toxicity')
          - functions (verbs like 'ionizing', 'activate', inputs/outputs like subject/predicate nouns)
          - variables (function inputs like subject/modifier nouns)
          - then test on bio systems:
            - "adjacency as a definition of relevance can be used as a way to derive paths" + "path optimization can be used to get a drug to a location in the system"
            - "isolate a pathogen cell before destroying it so it cant communicate info about what destroyed it to other pathogens to help them evolve resistance"
      - functions to determine:
        - position/role in a system 
        - function type associated with its core functions (change rules, boundary rules)
        - emergent effects in edge cases, rule change states, & interacting with other system layers
        - solution via conceptual route
      - function to derive core component functions for any system - then you can write functions to:
        - determine equivalent functions or more optimal version of a function
        - determine function intent
        - alter core functions used to alter function intent
        - when generating solutions, change core functions to vary to describe any function set that builds any other function set in a system
          - set of binding/interaction/priority functions for element atoms

# Conceptual

  - add error-generation
    - add diagrams for error types:
      - misalignment
      - assumptions without supporting logical/information links
      - incorrect position/function/structure/scope/limit/range/definition

  - add causal type identification for known solutions:
    - causal types: direct/indirect, multiple/alternate, hierarchical, replaceable/unique, generatable/emergent
    - why did something work? because of its:
      - structure (which piece - the imidazole)?
      - interactions
      - other attributes
      - similarities

  - add variable-selection example with separate alts having equivalent outputs:
    - if one alt is disabled, then it would give a false result for anyone checking it for ability to impact the output, even though the alternative was being variably used instead

  - function to identify & remove common article intents with high probability of falsehood to reduce it to just facts
  - add intent matching so you can compare treatment relationships with article intents to see if its actually a sentence with a treatment in it
    - finish treatment failure condition - make sure it adds nothing if theres no treatment in the article - this is related to intent function
  - use distortion patterns of entities like atlases, templates, solution progressions to form a compressed version of the host system
    https://techxplore.com/news/2019-11-medical-image-analysis.html
  - add stressor language patterns
  - for queries of functions like "disable a gene", you can include intent & function metadata to point to sets of compounds that could do the required edits:
    - find compound (protein, enzyme, etc) that unfolds DNA
    - find compound that modifies (edits, activates, removes) the gene once unfolded as specifically as possible 
      (can be a compound with a cutting subcomponent at the right length to target the dna if you can bind it to the first or last gene with another compound)
    - find compound with function = "refolds DNA"
    https://medicalxpress.com/news/2019-12-common-insulin-pathway-cancer-diabetes.html

# ML
  - the full data set should have numerical categories indicating condition(s) treated in the output label so it can be separated into sub-sets by condition treated
  - incorporate stacked autoencoders to leverage unsupervised learning to get initial weights
  - incorporate cosine loss rather than categorical cross entropy
  - add recurrent nn example code that can be copied & plugged in without modification

# Diagrams

- make diagram for variable accretion patterns
- finish diagrams for specific concepts, core functions, concept operations, ethical shapes
- finish informal fallacy diagrams: https://en.wikipedia.org/wiki/List_of_fallacies
- consider using dimensionality reduction as a way to identify abstract patterns & functions to explain common deviations from patterns
    https://miro.medium.com/max/1659/1*nQrZmfQE3zmMnCJLb_MNpQ.png
    https://towardsdatascience.com/step-by-step-signal-processing-with-machine-learning-pca-ica-nmf-8de2f375c422
- use this or similar as example when describing current state of problem solving: 
    https://miro.medium.com/max/462/1*X7dQgs1gsJ0Sktz3t7J21Q.png
    https://towardsdatascience.com/feature-extraction-techniques-d619b56e31be

# Questions
  - are pathogen receptors/membranes unique enough that you could design a substance to artificially bind with them to deactivate or puncture the membrane without impacting other structures?