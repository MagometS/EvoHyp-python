from GeneticAlgorithm.Problem import Problem
from DeepScaSolution import DeepScaSolution



class DeepScaProblem(Problem):
    filename_deep = None
    filename_sca = None
    obj_function = None

    def __init__(self, filename_deep, filename_sca, obj_function):
        self.filename_deep = filename_deep
        self.filename_sca = filename_sca
        self.obj_function = obj_function


    def evaluate(self, heuristic_combination):
        solution = DeepScaSolution(self.obj_function)
        solution.set_heuristic_combination(heuristic_combination)
        solution.create_solution(self.filename_deep, self.filename_sca)
        return solution
