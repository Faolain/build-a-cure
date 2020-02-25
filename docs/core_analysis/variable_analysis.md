# Variable Accretion Patterns

  - optimal variance in a system

    - in general, variance should be preserved when its capable of resolving problems whose solutions are more valuable than the cost of the problems caused by the variance, otherwise it shouldnt be allowed to vary
    
    - this will create systems that are robust & good at self-optimization, but the problem-solving methods will be optimized for resolving one uncertainty at a time, because the variance will be delegated to uncertainties, to find out which pattern in the uncertainty space is optimal

    - the overall system variance needs to be maintained at a level above the sum of the uncertainty spaces (variance gaps) in the system, otherwise it will be incapable of resolving any other questions than those captured in the uncertainty spaces

    - one way to increase overall system variance is to build connections between uncertainty spaces, and to route variance between them so patterns can coordinate between them, and to inject variance when one uncertainty is resolved

    - example:

      - if you determine optimal bio-system implementation & design dna accordingly, your bio-system will be able to handle the problems optimized, but if you dont allow genetic mutations, it wont be able to adapt to new problems (variance sources) with existing evolution methods, so youd need to build extra evolution methods (like functionality finding/acquiring methods in each cell's dna, or a built-in evolution system that cooperates with other systems like the immune system) to make sure variance is injectable on demand or acquirable accidentally from the environment


  - variable interactions


    - a variable has an upper limit on what degree of change it can determine in another variable that its not equivalent or directly related to
      - sometimes this limit is determinable, like with variables of a known type:
        - an attribute of an object can only have x influence on an emergent system attribute


    - randomness can occur on any interface layer in a system, but the trajectory between layers leaves traces 
    
      - example: converting randomness between linear operation layer (in direction of rotating line) to continuous function layer (in slope of curve)
        "any linear combination of a fixed collection of normal deviates is a normal deviate" - https://en.wikipedia.org/wiki/Normal_distribution

      - this means the adjacent states can be inferred by randomness change patterns between specific interfaces

      - if a variable is completely random, is it possible to spot the influence of structures generating it if you have information about a state change in the random variable

      - why would a sum of independent variable values converge to a normal distribution?

        - this implies that variables that are likelier to have similar averages are likelier to interact later in the system

        - this matches the interaction of variables on an interface
          - opinions are likelier to interact with objects on a similar scale (info, other opinions, perspectives) than objects on a different scale (energy, matter, quantum physics, probability)

        - the idea of an average is similar to the idea of a symmetry (type of change that stays within a change limit)

          - example: 
            - a point that rotates around an axis has a symmetry of type 'average' or 'center', and further rotations dont change the fundamental attributes of the point, like its rotation axis value
            - a type that changes within the type interface but doesnt transform into another interface object is an example of change about the type symmetry/interface

        - so variables with the same symmetries/interfaces are likelier to interact


    - the ways that a set of variables accrete into output variables can be described by a set of possible paths between i/o

      - the way that a set of attributes accrete into one output attribute (type) follows similar patterns outside of neural nets

      - the position of variables can be predicted & their likely interactions from this position

        - "identifying features will be in a similar direction as sensing features" is a prediction about variable position (identifying features & sensing features) based on the i/o attributes of 'relevance', 'alignment', 'distance', and 'difference'

        - "sensing features can be identifying features" is a prediction about variable position (identifying features & sensing features) based on the i/o attributes of 'relevance', 'function overloading' 

        - this can reduce the nodes in a network, especially at earlier layers

      - datasets should be filtered by i/o variables - output variables like 'phenotype' should be the variable to predict in some cases rather than input variables like 'dna'

      - sometimes emergent output variables are in the original data set, when they should be predicted
        - these output variables might correlate with the original target output variable because the neural net (including branches of networks off of the original neural net) can predict both of them
        - these correlating variables can be used as a proxy for predicting the original target output variable, if there is better data on the alternative emergent output variable
        - or the relationship between correlating variables can be calculated & applied to transform predictions of proxy emergent variable to predict the original target variable
        - the gaps in variance described by variables can also be used as an input var
        - predicting gaps in variables (variable changes that usually have a variable in between them but the variable is missing from the dataset)


    - interface variables should be evaluated in branching network loops

      - original network evaluating for output original variable 'type'
          alternate network evaluating for output interface variable 'relevance'
            alternate network output
        ^ back into original network

      - this essentially describes the interface variable with neural nets as nodes, so output relevance can be used for training the original network, as relevance is an input/output variable

      - if a variable can be an output/input or an interim variable, its position should be adjusted

          - input/output variables should be target variables in an alternate version of the network branching off from original network and & routed back to original input set

            - i/o variables like 'relevance' should have their own chain of networks starting from inputs & branching off to loop back to original inputs

          - interim variables should be checked at interim compilation of information layers in the network


    - format data to use different algorithms

      - example:

        - the measure of distance/position between variables can be changed to use different algorithms
          - image processing algorithm can be used once difference measure is found in non-image data so that position can be assigned


    - activation/loss functions need to be more flexible depending on input variables

      - one metric value to assess activation/loss/difference scores & thresholds may be enough for training over many iterations but not optimizing training

      - some predictions that seem inaccurate are:

        - accurate given the data (requires variables from other systems to determine accurate relationship)
        - a result of data not reflecting change patterns (data point creating the loss is an outlier indicating prior or future state or side effects of current state)


    - meaning of neural net structure

      - relevance appears in several positions in this structure:

        - the inclusion of variable values in the vector implies relevance
        - the position of variables in the vector can imply relevance depending on how its processed (example: size of convolution)
        - the distance of network nodes can imply relevance depending on how theyre processed later (example: pooling)
        - the layer of variable accretion implies interface/interaction layer


  - all nodes should be able to communicate with all other nodes but it should be a fallback mechanism to enhance independent functioning & warn of impending variance approaching system

  - questions

    - if big bang was variance leak from another universe, what info can be derived about a system that was organized & efficient enough to be able to accrue a lot of variance & route it either intentionally or accidentally to one point, but would also leak a large amount of variance at once in an unplanned way

      - did this preserve the original universe or was there other variance remaining that reduced or disseminated pieces of it
      - did the remaining variance continue unrestricted until randomness was generated by the cascading change production

    - adding variance in a universe used for computation causes errors up the computation stack, meaning this universe may be wiped out or it may attract error-handlers
    - it may also attract variance if this universe has the best variance-handlers

  - mismatch between limits & variance

    - lack of limits: variance gaps from lack of rule enforcement
    - over-limits: too much rule enforcement preventing adaptation

    - variance can accrue from compounding layers/interactions, just like limits can

      - when too many options are hard-coded in a system, that system loses its flexibility
      - to prevent this:
        - distribute communication tools (nerves, immune system, blood flow)
        - distribute functionality-acquisition tools (bacteria, gene-editing)
        - make sure the entangled cells in a system operate on entanglement networks that can break any cascading entanglement chains
      - the goal is to make sub-components as independent as possible (capable of generating/repairing themselves or the system)
          
  - variable interface is the interface of change/potential & rule evolution

  - variance attracts variance to allocate the task of ordering to the systems that are best at ordering (efficient systems) - entropy

  - how do attributes emerge:
    - with intersecting chains (or fractals, a chain subtype that varies scale) of core functions
    - example:
      - viscosity emerges from the interaction of boundary, distribution, pressure, & binding rules, as liquids change states to form higher viscosity states on the spectrum of liquidity
      - as these objects interact without invalidating the original interface (liquid), other attributes emerge from combinations of objects & their interaction chains
      - from a set of rotated lines, the attributes of a curve can emerge (measurable at visible scale) because of the compounding effects of the incremental rotations at scale

  - do variables with more similarities tend to cooperate or compete more? 
    - it depends on:
      - what stage of similarity theyre at, including whether they:
        - are similar on common or rare metrics
        - what axss of similarity they have in common (variable rules, metadata, types, combinations, structures, networks)
        - occupy different systems
        - evolved in the same system for different reasons/out of different components
      -  if they have prior or imminent dependency (just diverged or are about to converge or have convergence/divergence potential)

  - at what point does a variance accretion become a cascade or another variance shape? it depends on the system structure & the rules governing the development of variance handlers
  - variance handlers can distribute variance across inputs to limit its impact, limit its interaction potential with barriers closing the gaps in rule enforcement, or derive its function so it can be controlled
  - the set of variance handlers that can be generated in a system is calculatable

  - variable importance/relevance filtering rules are often flawed bc of lack of core function analysis & other system analysis types

    - before ruling out a variable, check if the variable set with it removed can generate the functionality theorized to be generated by the removed variable

  - is variance a product of gaps in enforcement rules & useful object combinations/permutations that havent yet been combined for a particular intent on a particular interface?

    - example:

      - because there was no one to prevent the sun from impacting fur color, the sun was allowed to interact with fur, which made some species develop alternate compounds to handle extra radiation exposure

        - the fur interface happened to have object permutations that hadnt been activated yet, which when combined with radiation, evolved another dimension of variance, which was fur shade & compounds
        - the different values of this variable had different matching intents
        - what was the reason this variable (sun) was able to impact the other variable (fur) to add new dimensions to the impacted variable (shade/compounds)?
          - fur has components (dna, pigment, proteins) which had latent functions (like skin has vitamin production functions) impacted by components of sun (radiation)
          - why did these components have reactability with sun components?
            - scale (dna is a similar scale to radiation metadata)
            - structure (dna has a structure that can be modified by radiation structure)
            - variance intersections 
              (radiation variance in the form of waves causes variability in output structure of dna, which itself is highly variable given number of genes & fragility of expression & repair)

    - you can see how it would be possible to generate the possible causes by navigating through trajectories & combinations of interface components

  - is there a relationship between the potential of energy to produce information (certainty & uncertainty), allocating variance & stasis to either at a time asymmetrically
    https://en.wikipedia.org/wiki/Introduction_to_eigenstates

  - is knowability/calculatability determined by variance distribution physics?

  - can you exert control on variance distribution of resources (power, energy, info) to produce changes in default physics at scale?

  - can you exert operations on uncertainties (and uncertainty objects & attributes like measurement/calculation potential, changes/patterns in change rules) to aggregate uncertainties or produce emergent certainties 

    - combinations of random vars producing predictable vars (due to predictability of randomness property in inputs) - does certainty cascade/accrete like variance does?

    - aligning uncertainties (variance/variance generator distribution, divergence, superpositions) to produce certainties (measurement threshold, standardization, energy concentration, information, guaranteed randomness)

    - example: this is similar to how you dont need to measure an individual particle's electron position if you assemble a bunch of particles and the output of their electron spins generates adequate measurement potential

  - visualize:

    - emergent properties as circuits within an object/system/type set

    - variables as an output vector or tensor composed of tensors or vector sets
      - several metrics united by origin point, 
        such as how a species' features are composed of a network of many causative factors, 
        where a variable like dog paw shape is representable as a subset of these network paths, 
        and a smaller subset of network path patterns (causation physics)

  - add examples of system/object/rule/type change patterns

  - add examples of variable gathering patterns into a type

  - add examples of variable accretion patterns (how an object like a system or a type becomes influenced by a new variable)

    - variable path pattern convergence/divergence and interaction with systems/objects/types/rules

      - this should enable you to predict:
        - variable flow (which variables are about to be irrelevant, which variables would disrupt others, which variable types to use)
        - variance flow:
          - in system/object/rule/type:
            - stability/boundary/change/isolation patterns (core/granular functions without side effects, independent closed loop systems)
            - exchange rates (how it trades variance with other objects and how the sum of all trades influences system variance)
        - impact between variables & other system objects
        - impact of variable survival success on external system dynamics
        - optimal variables/functions/paths for a function/system/type
        - optimal origin positions of concepts to allow successful systems to evolve

    - stable variable collisions occur when variables:

      - dont disrupt the system interactions
          example:
          - produce metabolites that are handled by existing mechanisms
      - actively coordinate with the system interactions for existing intents
          example:
          - aligns intents
          - links trade loops to optimize trades
      - supports emerging intents that have not been exhausted out of full set of possible system intents
          example:
          - creates a type split
      - replace system interactions
          example:
          - provide extra regulatory layers as a backup check
          - provide self-repair or self-regenerative capacity to create independence within the system

    - unstable variable collisions happen when variables:

      - introduce more variance than needed or supported, or enter the system at a point or state where supporting functionality is inaccessible or underivable
          example: 
          - interfering with a gene that is not regulated/protected
      - interfere with system interactions
          example: 
          - prevent cell communication
      - remove barriers between systems
          example: 
          - removing barriers between organs or systems can produce cascading problems (blood barrier, intestinal/mucosal barrier)
      - a variance injector that interferes with causal variables or system-wide variables
          example: 
          - mutagenic compounds disrupt bio system on a system level

    - example:

      - more complex models progress to simpler models with increases in system stability, which create a system that can interact with more systems without a corresponding degree of change disrupting its functioning, but rather aggregates logic & fits it in the places where it can enhance stability, as a steadily increasing degree of exposure to new variables allows the system enough time to produce handlers that standardize chaotic inputs to usable inputs

      - this progression makes it possible to identify:
        - when a simpler model is the future & more useful version of a complex model
        - which direction the complex model is progressing in (away from/toward standardization/simplicity)
        - the set of reasons why its moving in that direction (system unraveling through interaction with more complex systems its not prepared for, etc)

    - if there are multiple explanations for various factors, but there are variable relationships connecting different options for different variables, the (more) related variables are likelier to be explanatory
      
      - example:

        - the reason for dog ear shape could be for maximizing hearing or for protecting against pests
        - the reason for dog tail shape could be for maximizing speed or for protecting against pests
        - the reason for dog paw shape could be for weight distribution or for flexibility or for protecting against predators

        - given these sets of variables in the dog system, which explanation is likeliest to be correct given their relationships, if there are any across variables?

          - the evolutionary position of a dog is relevant: 
            - is a dog an apex predator or known for being particular fast at running away from predators?
            - do dogs typically carry excess weight or get some other benefit from paw weight distribution like flexibility?
            - do dogs have better haering/speed than adjacent species?
            - are pests/predators a bigger threat than paw injuries from excess weight?

          - the reasons also have relevant patterns:
            - regardless of position on food chain, most species have a ratio of x protective mechanisms to y functionality/attribute optimization mechanisms

          - look for relationships between all variables
            - is flexibility of paw manipulation a factor influencing speed? (adapting to terrain)
            - is tail shape related to weight distribution? (balance)

          - of the two obvious relationships (maximizing & protecting), is hearing/speed more important than protective mechanisms? 
            (and therefore likely to evolve sooner or be a better identifying trait)

            - given the lack of direct predators for many dog species/environments, variables to defend against predators arent as likely as variables to defend against pests
            - given the lack of hunting requirements for many dog species, hearing & speed arent as important as if dogs had to find their own food
            - this leaves 'protecting' as the remaining relationship with the higher impact

          - there are other relationships to analyze:

            specific objects:
              - senses (hearing)
              - extremities (paw, tail)

            attributes:
              - shape
              - adaptability (flexibility, protective spectrums)
              - balance (distribution, even number of limbs, spreading out sensory features, extra extremities to improve balance)
              - backup mechanisms (extra limbs (3 are necessary for similar speed), multiple protective features, multiple senses)


    - variables contain variance according to data type & variance source patterns - when a source exceeds the capacity of a variable, how does it spill into the system or other objects?
     
      - example: 

        - when a stressor (sharp-edged object or membrane-processing enzyme) becomes too much for a variable (cell membrane strength) to handle, what is the impact on the system?

          - the cell contents become unbounded by the membrane & leak into the bloodstream
          - the contents interact with other cells expected in blood
          - those cells are disrupted
          - regulatory processes may be alerted to clean up the contents
          - if regulatory processes are not available, the disruption may cascade, distributed by blood flow
          - mutations & other serious disruptions with minimal triggering requirements may occur as a result of the cascade
          - if more than one cell was disrupted in this way, the mutations may accrete, and eventually one of them may be a cancer-causing mutation

      - the net impact of a variance spill can be a variance cascade or other variance shapes


    - how do variables accrete in the first place?

      - when different requirements can be built with the same set of core components, each interim set of core component combinations producing those requirements is a variable

      - example:

        - when different required intents (balance, flexibility, senses) can be built with the same set of core components
          (tissue types, cell types, genes, mutations, microorganisms, shape, nutrients), 
          each interim set of core component combinations (paw shape, nerve distribution, extremity & feature distribution) producing those requirements is a variable
      
        - height: many input variables (nutrients, activity) determine the height variable, and the height variable is an input to many different required intents (hunt, fight, reach, climb)

      - variables act as an interface between input variables & output variables, so the variables we tend to pay attention to are often hubs in the network of variables


    - system constants may temporarily cover gaps in variance explanations during system state changes
      - how do variables decay into constants?
      - how do constants interact with variance sources to become variables?


    - variable accretion & relationship paths can explain type variance (trajectory through a neural network)

      - the set of protection-intent variables for a dog can explain differences in survival & evolution between dog & adjacent/predator/prey species in extreme conditions
      - it can also impact the larger ecosystem, unless theres a dog-network substitute about to take its place when it goes extinct, or exacting an opposing stressor on the ecosystem
        - example: if theres a set of variables higher up the causal chain (adaptability), and that is allowed to interact with other systems in the ecosystem, it will probably generate other domesticatable predators that can take the place of dogs (cats)
      - the variable sets (learning, energy magagement, mutation patterns, efficiency) generating those two variable sets (protection & adaptability) are the explanatory sets for evolved attributes/rules shared across type layers


    - in a system with similar structures having similar complexity, similar variables may evolve that can act as replacements/substitutes/alternatives

      - example: 
        - a square may have different but similar uses for its corners, like storing some set of small objects
        - when it starts to rotate (injected with variance in form of relative internal object position), 
          the grouping rules for those small objects may be applied adequately to other sets


    - from variable accretion patterns, you can derive common variable distortion functions:

      - ensuring backups/alternatives to test a value for usefulness
      - applying divide & conquer to variable values, & retaining or requiring useful values
      - change variable metadata (data type, variance, dependencies, value options)
      - split/merge/link/unlink/inject/eject a variable
      - change variable to a constant or eject variable when variance is required in dimensions the original variable cant influence
          example: if dogs suddenly need to breathe in space, their tail shape may not matter anymore
      - inject a variable when a system is so orderly it cant handle a particular problem
          example: 
          if mutations cant help the dog evolve quickly enough, attack from high-variance interfaces:
            - function deployment: give it the function to export functionality between cells & a non-hostile microorganism with the functionality to convert the lung to an organ capable of providing it with air
            - function expansion: add genes/chromosomes/TADs/pathogen that would give it this ability
            - function hack: design an lung that converts space particles to breathable air & surgically insert the lung
            - stressor deployment: give it the stressors that would lead to it developing the required function, if buildable from available core functions


    - why do variables accrete into sets?
      - variables organize into object input sets for cooperative differentiation of labor (filtration, regulation, identification, communication, protection) & organize into coordinating systems for layers of functionality/core function types (object health tests, object input deployment)  
      - input sets: one aggregating factor organizing variables into input sets is their ability to add useful change to achieve outputs from a set of inputs
        - a function can gather variables useful to it, just like a membrane can gather components useful to the cell
      - type sets: standard, simple platform structures attract variance across a dimension set (a standard implementation of a paw provides an interface for distortions to occur that may have utility for various intents)
      - when a particular level of variance is no longer required, variables can consolidate or be ejected 
          (if dogs' predators were to evolve a better alternative to vision, dogs might stop having different fur colors to disguise themselves to predators or survive in different climates)
      - when a variable is added that is unnecessary, it creates extra disorder where none is demanded, and this can result in systemic change or destruction