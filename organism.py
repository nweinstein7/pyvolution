MUTATION_LEVEL = 10  #There is a 1/10 chance a gene is mutated

import random
from random import randint

class Organism(object):
  '''
  This is a basic organism in an evolutionary simulation
  @param genome: a dictionary of individual genes
  @type genome: dictionary
  @param fitness: the organism's evolutionary fitness
  @type fitness: int or float
  @param id: an identifying integer for this particular organism
  @type id: int
  '''
  def __init__(self):
    self.genome = {}
    self.fitness = 1
    self.id = 1

  def mutate(self):
    '''
    Mutates the genome of the organism
    '''
    for key in self.genome.keys():
      if randint(0,MUTATION_LEVEL)==0:
        self.genome[key] = self.mutate_gene(self.genome[key])

  def mutate_gene(self, gene):
    '''
    Mutates a specific gene in the genome sequence
    Override as needed, depending on the gene
    @param gene: the gene
    @type gene: any type
    @return: the mutated gene
    @rtype: whatever type the gene is
    '''
    return random.uniform(0.0,1.0)

  def cross(self, parent1, parent2):
    '''
    When called on a newly initialized organism, sets that organism as the offspring of two parents
    @param parent1: first parent of the offspring
    @type parent1: organism
    @param parent2: second parent of offspring
    @type parent2: organism
    '''
    for key in self.genome.keys():
        if randint(0,1) == 1:
          self.genome[key] = parent1.genome[key]
        else:
          self.genome[key] = parent2.genome[key]

  def evaluate(self):
    '''
    Evaluates the organism for evolutionary fitness
    Override as needed, depending on the data being used for simulation
    '''
    return self.fitness

  def __repr__(self):
    str = "ORGANISM ID: {0}".format(self.id)
    str += "\nFITNESS: {0}".format(self.fitness)
    return str
