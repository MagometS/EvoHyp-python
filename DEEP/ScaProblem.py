from GeneticAlgorithm.Problem import Problem
from ScaSolution import ScaSolution


class ScaProblem(Problem):
    filename = None
    obj_function = None

    def __init__(self, filename, obj_function):
        self.filename = filename
        self.obj_function = obj_function

    def evaluate(self, heuristic_combination):
        solution = ScaSolution()
        solution.set_heuristic_combination(heuristic_combination)
        solution.create_solution(self.filename, self.obj_function)
        return solution
