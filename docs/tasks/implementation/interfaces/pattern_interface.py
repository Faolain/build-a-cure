'''
  - example of the analysis for this interface: 
    - a pattern can be or contain any structure, optionally including a function (the pattern being a sequence of logical steps) but it is different from a function in that it is more abstract & can optionally include other structures, and the point of the pattern is not to get a particular object like the function output, but to identify common trends across systems so the pattern can be used for inference or value generation 
    - a pattern is a relationship between objects, the point of storing which is to identify repeated relationships 
    - the relationship between objects is not the only part of the pattern that matters - the actual object identities may be an integral part of the pattern 
    - for instance the pattern '1 1 2 3 5' may have a relationship like 'a subset of the fibonacci sequence' but it also may be important that the sequence starts at 1 (the initial object identity) because it may be used for calculation 
    - so the trajectory mapped by a pattern may not be all that matters - the starting/ending points or values of the pattern may also be relevant 
    - this is different from a function which would have abstract starting/ending points in addition to the sequence of logical steps, to govern where the function can be used 
    - patterns that are common across systems imply a level of increased probability of that pattern occurring in other systems, so patterns can be used to infer attributes like probability 
  - functions: 
    - generator: generates a pattern given parameters 
    - compress (reduce the pattern to a generator function) 
    - expand (generate a sequence using a generator function) 
    - implement (apply a generator or sequence to a structure in a context) 
  - attributes: 
    - abstraction: a pattern can be a pattern of specific values (1, 2, 3, 4), the metadata of those values (type: int int int int, divisor attribute: odd even odd even, exclusive divisor attribute: prime prime prime not-prime), or an abstract version of the values (number, pair/number of points required for a line, sides of a triangle, number of players required for a game), or a mix of these 
    - structure: a pattern can optionally include any structured information, optionally including a set of logical steps, a set of attribute values, a list of events, a query on a graph, a trajectory in a tree, a list of numbers representing feature values, etc 
    - relevance: is the pattern relevant for another structural context 
    - composability: what patterns can a particular pattern be combined with 
    - completeness: whether the pattern is complete 
  - objects (components (any type of structured information is allowed in patterns, with values like integers, words, other patterns, references to objects, etc)) 
  - structures (sequence (sequential pattern), network (a pattern of relationships)) 
  - concepts (repetition, relevance) 
  - answers questions like: 
    - what would the path between inputs/output probably be, given patterns of other paths 
    - what is the function linking these variables, given common function patterns between variables of these types/topics/ranges/other metadata? 
'''
