from GeneticAlgorithm.Problem import Problem
from DeepScaSolution import DeepScaSolution



class DeepScaProblem(Problem):
    filename = None
   

    def __init__(self, filename):
        self.filename = filename


    def evaluate(self, heuristic_combination):
        solution = DeepScaSolution()
        solution.set_heuristic_combination(heuristic_combination)
        solution.create_solution(self.filename)
        return solution
