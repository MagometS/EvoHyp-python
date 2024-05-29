import sys
import time

from DeepProblem import DeepProblem
from DeepScaProblem import DeepScaProblem
from GeneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm

class DeepExample(object):
    @classmethod
    def solve(cls, filename):
        # problem = DeepProblem(filename)
        # seed = round(time.time() * 1000)
        # heuristic_combination = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef")
        # # problem.set_heuristic_combination(heuristic_combination)
        # genetic_algorithm = GeneticAlgorithm(seed, heuristic_combination)
        # genetic_algorithm.set_parameters("Parameters.txt")
        # genetic_algorithm.set_problem(problem)
        # sol = genetic_algorithm.evolve()
        # print("Best Solution")
        # print("--------------")
        # print("Fitness:", sol.get_fitness())
        # print("Heuristic: ")
        # print((sol.get_heuristic()).__str__())
        # print("Solution: ")
        # cls.display_solution(sol.get_solution())

        problem = DeepScaProblem(filename)
        seed = round(time.time() * 1000)
        heuristic_combination = str("B")
        # heuristic_combination = str("ABCg")

        # problem.set_heuristic_combination(heuristic_combination)
        genetic_algorithm = GeneticAlgorithm(seed, heuristic_combination)
        genetic_algorithm.set_parameters("Parameters.txt")
        genetic_algorithm.set_problem(problem)
        sol = genetic_algorithm.evolve()
        print("Best Solution")
        print("--------------")
        print("Fitness:", sol.get_fitness())
        # print("Heuristic: ")
        # print((sol.get_heuristic()).__str__())
        print("Heuristic combination: " + sol.get_heuristic_combination())
        print("Solution: ")
        cls.display_solution(sol.get_solution())
    
    @classmethod
    def display_solution(cls, solution):
        # Displays the solution.
        for element in solution:
            attribs = element.get_attributes()
            print(attribs[0], attribs[1], attribs[2])
        print()
    
    @classmethod
    def main(cls, filename):
        # filename = "deep_rastr.ini" # .ini file for deepmethod
        cls.solve(filename)

if __name__ == "__main__":
    DeepExample.main('deep_clust.ini')
