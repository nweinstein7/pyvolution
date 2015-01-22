from organism import Organism
import random

ELITE_LEVEL = 10 #Population_size / 10 will be number of elites left over between generations

class EvolutionarySimulator(object):
  '''
  Runs an evolutionary simulation
  @param population_size: the number of organisms in the population
  @type population_size: int
  @param n_elites: number of elite organisms kept intact between generations
  @type n_elites: int
  @param n_generations: the number of generations to run
  @type n_generations: int
  @param organisms: the organisms to undergo evolution
  @type organisms: array
  @param sorted_organisms: the organisms sorted by fitness
  @type sorted_organisms: array
  '''
  def __init__(self, population_size=40, n_generations=100):
    self.population_size = population_size
    self.n_elites = self.population_size / ELITE_LEVEL
    self.n_generations = n_generations
    self.organisms = []
    self.sorted_organisms = []
    self.organisms = self.initialize_population()

  def get_organism(self):
    '''
    Returns the type of organism used for the simulation
    Override to run a simulation with a custom organism
    @return: a new organism
    @rtype: organism
    '''
    return Organism()

  def initialize_population(self):
    '''
    Initializes the population for the simulation
    @return: the array containing all organisms
    @rtype: array
    '''
    for x in range(0,self.population_size):
        organism = self.get_organism()
        organism.id = x
        self.organisms.append(organism)
    return self.organisms

  def select(self):
    '''
    Performs roulette wheel selection, returns organisms in proportion to their fitness
    @return: an (on average) evolutionary fit organism
    @rtype: organism
    '''
    #sum up fitnesses of all organisms in population
    sum = 0
    for x in range(0,self.population_size):
        sum = sum + self.sorted_organisms[x].fitness

    #select a random point between zero and sum of fitnesses
    roulette_ball = random.uniform(0.0,1.0) * sum

    #this "roulette ball" will more likely fall on fitter individuals
    tally = 0
    for y in range(0,self.population_size):
        tally = tally + self.sorted_organisms[y].fitness
        if roulette_ball < tally:
          return self.sorted_organisms[y]
    return self.sorted_organisms[0]

  def simulate(self):
    '''
    Runs the evolutionary simulation
    '''
    for count in range(1, self.n_generations):
      print "\n\n\nGENERATION: {0}".format(count)
      for organism in self.organisms:
        organism.evaluate()
        print organism
      self.sorted_organisms = sorted(self.organisms, key=lambda organism: organism.fitness, reverse=True)
      #Elitism:
      for i in range(0, self.n_elites):
        self.organisms[i] = self.create_elite_organism(self.sorted_organisms[i], i)
        print "\nELITES: ", self.sorted_organisms[i]
      for x in range(self.n_elites, len(self.organisms)):
        self.organisms[x] = self.create_new_organism(x)

  def create_elite_organism(self, parent, id):
    '''
    Creates an elite offspring by crossing a previous generation's elite organism with itself
    @param parent: the elite organism from previous generation
    @type parent: organism
    @param id: id of new offspring
    @type id: int
    @return: the elite offspring
    @rtype: organism
    '''
    offspring = self.get_organism()
    offspring.id = id
    offspring.cross(parent, parent)
    return offspring

  def create_new_organism(self,id):
    '''
    Creates a new organism by selecting and crossing organisms
    @param id: id of new organism
    @type id: int
    @return: offspring
    @rtype: organism
    '''
    offspring = self.get_organism()
    offspring.id = id
    offspring.cross(self.select(), self.select())
    offspring.mutate()
    return offspring

if __name__ == '__main__':
  sim = EvolutionarySimulator()
  sim.simulate()
