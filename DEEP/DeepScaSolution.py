from typing import List

from GeneticAlgorithm.Solution import Solution
from DeepScaComparison import DeepScaComparison


class DeepScaSolution(Solution):
    heuristic_combination: str = ''

    fitness: float

    initial_solution: List[str] = []


    def get_fitness(self) -> float:
        return self.fitness

    def set_heuristic_combination(self, heuristic_combination: str):
        self.heuristic_combination = heuristic_combination

    def get_heuristic_combination(self) -> str:
        return self.heuristic_combination

    def get_solution(self) -> List[str]:
        return self.initial_solution

    def fitter(self, other: Solution):
        if other.get_fitness() >= self.fitness:
            return 1
        elif other.get_fitness() < self.fitness:
            return -1
        else:
            return 0

    def create_solution(self, filename):
        sol = DeepScaComparison(filename)

        try:
            fitline = sol.create_solution(self.heuristic_combination)
            print(self.heuristic_combination, fitline)
            part2 = fitline.split(" ")
            self.fitness = float(part2[0])
            self.initial_solution = fitline
        except OSError as e:
            print(e)
