import time

from DeepProblem import DeepProblem
from GeneticProgram import GeneticProgram

class DeepExample:
    @classmethod
    def solve(cls):
        problem = DeepProblem()
        seed = round(time.time() * 1000)
        heuristic_combination = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdef")
        problem.set_heuristic_combination(heuristic_combination)
        genetic_program = GeneticProgram(seed, heuristic_combination, 1)
        genetic_program.set_parameters("Parameters.txt")
        genetic_program.set_problem(problem)
        sol = genetic_program.evolve()
        print("Best Solution")
        print("--------------")
        print("Fitness:", sol.get_fitness())
        print("Heuristic: ")
        print((sol.get_heuristic()).__str__())
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
    def main(cls):
        cls.solve()

if __name__ == "__main__":

    DeepExample.main()
    


