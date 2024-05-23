import sys

sys.path.append('/home/magomet/EvoHyp-python/GeneticAlgorithm')

from DeepSolution import DeepSolution
from Heuristics import Heuristics
from DeepProblem import DeepProblem
from GeneticAlgorithm import GeneticAlgorithm
from DEEP import DEEP
from SCA import SCA
from rastrign_func import rastrign_func
from DeepScaProblem import DeepScaProblem


# ds = DeepSolution()
# ds.set_heuristic_combination("ABCD")
# str = ds.get_heuristic_combination()
# print(str)


# heuristics_obj = Heuristics()  # creating Heuristics object
# section_name = "default_settings22"  # getting section name from map
# fit = heuristics_obj.run_heuristic("deep_rastr.ini", section_name)  # calling run_heuristic


# problem = DeepProblem("deep_clust.ini")
# heuristics = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef"
# genetic_algorithm = GeneticAlgorithm.GeneticAlgorithm(seed = 123, heuristics = heuristics, ran_gen = None)
# genetic_algorithm.set_parameters("Parameters.txt")
# genetic_algorithm.set_problem(problem)
# genetic_algorithm.evolve()

# dp = DEEP("deep_clust.ini")
# heuristics = "ABCDEF"
# dp.create_solution(heuristics=heuristics)

# sca = SCA('deep_clust.ini')
# best_fitness = sca.run_heuristic('sca_default_settings1')
# print(best_fitness)


problem = DeepScaProblem('deep_clust.ini')
problem.evaluate('gAgAgAgA')

# sca = SCA('p')
# solution, fitness = sca.individ_load('deep_clust.ini' + '.chk', 2)
# print(fitness)
# print(solution)
# fitness = [1.0 , 2.0]
# sca.individ_save('deep_clust.ini' + '.chk', solution, fitness)



# m =[]
# a ="1 2 3"
# b = '4 5 6'

# m.append([float(num) for num in a.split()])
# m.append([float(num) for num in b.split()])
# print(m)
