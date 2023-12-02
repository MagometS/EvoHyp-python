from GeneticAlgorithm.Problem import Problem
from DeepSolution import DeepSolution


class DeepProblem(Problem):
    def evaluate(self, heuristic_combination):
        solution = DeepSolution()
        solution.set_heuristic_combination(heuristic_combination)
        solution.create_solution()
        return solution
