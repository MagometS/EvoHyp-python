# Overall Best Heuristic Combination: ATRbOeYRg 
# Overall Best Heuristic Combination: dEDg

from DeepScaComparison import DeepScaComparison

import sys
import time

from DeepProblem import DeepProblem
from DeepScaProblem import DeepScaProblem
from GeneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm

class Graphs(object):
    @classmethod
    def draw(cls, filename):

        problem = DeepScaProblem(filename)
        # heuristic_combination = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg")
        heuristic_combination = str("AB")

        problem.evaluate(heuristic_combination)
    
    
    @classmethod
    def main(cls, filename):
        # filename = "deep_rastr.ini" # .ini file for deepmethod
        cls.draw(filename)


def draw_score_to_iterations(heuristic_combination, file_score, file_iter, number_iterations):
    sol = DeepScaComparison('deep_clust.ini')

    fit = []
    iterations = []

    for i in range(number_iterations):
        part = sol.create_solution(heuristic_combination)
        print(part)
        fit.append(part.split(" ")[0])
        iterations.append((i + 1) * 2)
    
    return fit, iterations


if __name__ == '__main__':

    # fit, iterations = draw_score_to_iterations('A', 'f', 'f', 8)
    # print("fit: ", fit)
    # print('it: ', iterations)

    Graphs.main('deep_clust.ini')



