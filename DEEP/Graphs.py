# Overall Best Heuristic Combination: ATRbOeYRg 
# Overall Best Heuristic Combination: dEDg
# QXfbIdAHg
from DeepScaComparison import DeepScaComparison

import sys
import time

import re
import configparser
import subprocess
import io

import numpy as np
import matplotlib.pyplot as plt

from DeepProblem import DeepProblem
from DeepScaProblem import DeepScaProblem



class Graphs(object):
    @classmethod
    def solve(cls, filename, heuristic_combination):

        problem = DeepScaProblem(filename)
        # heuristic_combination = str("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg")
        

        problem.evaluate(heuristic_combination)


    @classmethod
    def draw(cls, log_filename):
        fit = []
        sol = []

        with open(log_filename, 'r') as file:
            lines = file.readlines()

        for i in range(len(lines)):
            cleaned_line = re.sub(r'p\[\d+\]:', '', lines[i])

            part = [float(num) for num in cleaned_line.split()]
        
            fit.append(part[0])
            sol.append(part[1:])

        cost = []

        for i in range(len(sol)):
            cost.append(obj_function(sol[i])) #Проверить, что fit это значение растригина с этими параметрами

        print(fit)
        print(cost)
    
    
    @classmethod
    def main(cls, filename, heuristic_combination):
        # filename = "deep_rastr.ini" # .ini file for deepmethod
        cls.solve(filename, heuristic_combination)


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

    heuristic_combination = 'ABCD'
    Graphs.main('graphs.ini', heuristic_combination)
    # Graphs.draw('fit_log.txt')



