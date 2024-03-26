import sys

sys.path.append('/home/magomet/EvoHyp-python/GeneticAlgorithm')

from DeepSolution import DeepSolution
from Heuristics import Heuristics
from DeepProblem import DeepProblem
from GeneticAlgorithm import GeneticAlgorithm
from DEEP import DEEP



'''
ds = DeepSolution()
ds.set_heuristic_combination("ABCD")
str = ds.get_heuristic_combination()
print(str)
'''
'''
heuristics_obj = Heuristics()  # creating Heuristics object
section_name = "default_settings22"  # getting section name from map
fit = heuristics_obj.run_heuristic("deep_rastr.ini", section_name)  # calling run_heuristic
'''
'''
problem = DeepProblem("deep_clust.ini")
heuristics = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef"
genetic_algorithm = GeneticAlgorithm.GeneticAlgorithm(seed = 123, heuristics = heuristics, ran_gen = None)
genetic_algorithm.set_parameters("Parameters.txt")
genetic_algorithm.set_problem(problem)
genetic_algorithm.evolve()
'''
dp = DEEP("deep_clust.ini")
heuristics = "ABCDEF"
dp.create_solution(heuristics=heuristics)