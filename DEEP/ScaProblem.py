from GeneticAlgorithm.Problem import Problem
from ScaSolution import ScaSolution


class ScaProblem(Problem):
    filename = None

    def __init__(self, filename):
        self.filename = filename
    

    def evaluate(self, heuristic_combination):
        solution = ScaSolution()
        solution.set_heuristic_combination(heuristic_combination)
        solution.create_solution(self.filename)
        return solution
