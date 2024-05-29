# Overall Best Heuristic Combination: ATRbOeYRg 
# Overall Best Heuristic Combination: dEDg

from DeepScaComparison import DeepScaComparison

import sys
import time

import re
import configparser
import subprocess
import io

from DeepProblem import DeepProblem
from DeepScaProblem import DeepScaProblem
from GeneticAlgorithm.GeneticAlgorithm import GeneticAlgorithm

class Graphs(object):
    @classmethod
    def solve(cls, filename):

        problem = DeepScaProblem(filename)
        # heuristic_combination = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg")
        heuristic_combination = str("AAAA")

        problem.evaluate(heuristic_combination)
    
    
    @classmethod
    def main(cls, filename):
        # filename = "deep_rastr.ini" # .ini file for deepmethod
        cls.solve(filename)


# def draw_score_to_iterations(heuristic_combination, file_score, file_iter, number_iterations):
#     sol = DeepScaComparison('deep_clust.ini')

#     fit = []
#     iterations = []


#     for i in range(number_iterations):
#         part = sol.create_solution(heuristic_combination)
#         print(part)
#         fit.append(part.split(" ")[0])
#         iterations.append((i + 1) * 2)
    
#     return fit, iterations


def draw(filename):
    fit = []
    sol = []

    with open(filename, 'r') as file:
        lines = file.readlines()

    for i in range(len(lines)):
        cleaned_line = re.sub(r'p\[\d+\]:', '', lines[i])

        part = [float(num) for num in cleaned_line.split()]
        
        fit.append(part[0])
        sol.append(part[1:])

    cost = []

    for i in range(len(sol)):
        cost.append(obj_function(sol[i]))

    print(fit)
    print(cost)



def obj_function(agent):
        try:
    
            command = './rastrign_func.py'    #формируем команду для subprocess
            arg = [str(num) for num in agent]
            
            arguments = [command, *arg]

            p = subprocess.run(arguments, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  
            stdout_text = io.TextIOWrapper(io.BytesIO(p.stdout), encoding='utf-8') #оборачиваем p.stdout чтобы работал readline()

            while True:
                line = stdout_text.readline().strip()
                if line == '':
                    break
                log_line = line

            # part1 = log_line.split("cost:")
            # # print(part1[1])
            # # p.communicate()
            # part = part1[1]
            part = float(log_line)

        except Exception as e:
            print(e)

        return part
    




if __name__ == '__main__':

    # fit, iterations = draw_score_to_iterations('A', 'f', 'f', 8)
    # print("fit: ", fit)
    # print('it: ', iterations)

    # Graphs.main('deep_clust.ini')
    draw('fit_log_ATRbOeYRg.txt')



