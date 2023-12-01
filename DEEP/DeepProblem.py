from GeneticAlgorithm.Problem import Problem
from DeepSolution import DeepSolution

class DeepProblem(Problem):
    def evaluate(self, heuristic_combination):
        # Implements the abstract method to create a solution using heuristicComb
        # using an instance of the Solution class which is also used to calculate
        # the fitness using the objective value of the created solution.
        solution = DeepSolution()
        solution.set_heuristic_combination(heuristic_combination)
        solution.create_solution()
        return solution