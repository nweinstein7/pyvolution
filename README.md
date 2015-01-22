Python Evolutionary Algorithm
----------------------------------

##Instructions:

Extend the Organism class to make your own custom organism subject to artificial selection through its fitness function
  1. __init__: in your custom organism, you need to initialize genome to have the values you want.
    * for example, the gene could be a dictionary of different int values
  2. mutate_gene: create a custom method for your gene to mutate 
    * for example, mutating an integer gene could be setting it to a random value
  3. evaluate: this method applies the environmental constraints on the organism to calculate its fitness

Extend the EvolutionarySimulator class to run through generations of organisms, selecting the fittest ones
  1. get_organism: all you really have to extend to get it working - determines what kind of organism your simulator wants

The EvolutionarySimulator applies roulette wheel selection to the populatio each generation, creating a new generation
