- solution attributes

  - solution reusability: how to design/choose solutions for reusability
  - cost/benefit analysis (such as learning/understanding/integration/implementation/migration/functionality gap cost potential)
  - abstraction level: choosing the abstraction level that will reduce misunderstandings while optimizing reusability

  - solution types:
  
    - tools: as an immediate implementation option
    - learning (understanding as an alternative to using/selecting existing tools)
    - problem analysis: calculating probable solution cost, calculating value of problem reduction vs. problem solution (vs. secondary or source problem reduction/solution)

- tool selection (tools as a subset of solutions, which also includes learning, calculating solution metadata before investing)

  - tool indexing

    - tool index update strategy (when do you recalculate tool index):

      - how often do you update your knowledge of new tools/features to make calculations about migrating to/integrating a new tool

    - tool attributes (how do you index tools):

      - optimization
      - granularity/abstraction: needs to do one specific task really well, or needs to cover an abstract problem gap with minimal impact/side effects
      - integrations
      - time to learn/integrate/migrate
      - complexity: is source code available/understandable, how many security researchers have reviewed it using what tools
      - existing tool support
        - does it already interact with our other tools
      - simplicity/understanding status of tool
        - this tool is simple enough to be known to be exploitable in these ways so we have pre-designed plans for using this tool optimally
      - modularity
        - can it be swapped out & replaced seamlessly or does it have other dependencies making replacing it a complex calculation
      - current/planned features
        - it does x or will do x and thats all we care about, bc there arent good alternatives that can do x
      - delegation
        - features are not in a space we want to invest time in building/learning so we need to delegate labor to this tool
      - trust
        - we trust this tool provider bc theyre a, b, c (big company, good disaster response, good feedback integration into tools, etc)
      - standards compliance
        - this tool design implements standards with consistency/completeness
      - incentives
        - if third party tool is provided by a secondary platform/marketplace, 
          what guarantees are offered by the platform provider & by the third party tool provider for implementation side effects
          (third party tool integrated with a secondary platform tool)

- choose processes to automate

  - automation attributes:

    - resource investment (cost/time/security of sending data in a certain format or with a certain procedure)
    - understanding of problem space (are the rules clear enough that we can safely automate with little expectation of variance injection)

- inefficient process identification

  - inefficiency attributes:

    - granular/conflicting intent (only serves one intent optimally at sacrifice of another related intent that people often need together)
    - lack of clarity in cost/benefit structures (bc of abstraction, its not clear how a tool will provide a cost when interacting with another tool)

  - how do you minimize inefficiencies in workflow

    - translating task into clear requirements to reduce questions
    - identifying information gaps to distribute information where its relevant & needed

- error handling

  - what strategies do you use for anticipating problems (of a certain type & in general)

- planning decisions

  - how much time do you invest in planning & what are your planning strategies to avoid having to solve problems later?

- learning decisions

  - how do you decide what to invest time learning
    - for instance with splunk, how would you identify what level of expertise is required in order to design optimal queries?
      - different query design + latency + data mismatch because of compute/aggregate/cache data strategies that differ from a standard db implementation
    - the optimal level of learning is where you can identify a clear design intent for deviations from standard implementations

  - how do you educate yourself on inherent limitations of a tool 
    (if its designed for another intent, if its too new for advanced error handling)

  - how do you identify lack of knowledge and translate that into optimal search keywords for learning maximization?

    - identify lack of knowledge:

      - there is a level & pattern of complexity that is common to understanding of a tool:
        - people dont normally develop a solution of complexity 2 for a problem of complexity 1 - there are reasons for the complexity mismatch
        - so to identify lack of knowledge, look for over-simplification in summarization of a tool
        - sometimes the lack of knowledge will be on the implementation side rather than the user side, bc of lack of planning/organization

    - how do you identify key objects/terms that are necessary for acquiring a functional level of understanding that is capable of anticipating/minimizing errors in implementing that tool?

      - a beginner wouldnt know to search for 'abstract syntax tree' when education themselves about testing tools
      - a beginner wouldnt know to search for 'latency' or 'caching' when learning a new data storage/query tool

    - how do you map lack of knowledge to these terms once you identify lack of knowledge and key terms to acquire functional understanding?

      - you can derive key concepts of the problem space and map them to key concepts of solution space

        - key concepts of security problem space:
          - standardization

        - key concepts of security solution space:
          - standardization applied to code interpretation: formatting/parsing/translation
            - query for 'code security formatting parsing translation' should lead you to 'abstract syntax tree'
              - query result keywords:
                - interpolation, string 
                  - data type is key concept of string
                    - machine interpretation of data type by language
                      - machine language
                      - query for "code machine language parsing" has suggested related keywords:
                        - Lexical Analysis
                        - Compiler
                        - Backus–Naur Form
                        - Context-free Grammar
                        - Code Generation
                        - query for "code parsing compiler security" or "code parsing lexical security" would then also lead to 'abstract syntax tree' concept in subsequent results
                      - query for "code machine language parsing" leads to "abstract syntax tree" in first few results

        - in this way you can derive which concepts are important to learn to acquire functional understanding for a particular problem

        - how do you score these concepts based on importance, once you find them?
          - repeated abstract concepts inherent to sub-tools like languages (which is a sub-tool of the security intent) are likelier to be important
          - concepts with clear differences in intent are likely to be important (caching & latency reduction are sub-tools of data storage/retrieval intent with clearly different intent matrixes)
