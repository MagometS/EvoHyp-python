import numpy as np
import configparser
import subprocess
import io
import random
import math



class SCA:

    #obj_function = None
    file_name = None
    

    def __init__(self, file_name):
        self.file_name = file_name
        

    def run_heuristic(self, section_name):

        config = configparser.ConfigParser()
        config.read(self.file_name)

        heuristic_params = config[section_name]

        lower_bound = float(heuristic_params['lower_bound'])
        upper_bound = float(heuristic_params['upper_bound'])
        population_size = int(heuristic_params['population_size'])
        dim = int(heuristic_params['dim'])
        max_iterations = int(heuristic_params['max_iterations'])

        
        a = 2  # Constant in SCA formula
        
        solution, fitness = self.individ_load(self.file_name + '.chk')

        iter_best = []
        best_fitness = max(fitness)  # the score of the best-so-far candidate
        best_solution = solution[fitness.index(best_fitness)].copy()  # the position of the best-so-far candidate

        for t in range(max_iterations):
            r1 = a - (t + 1) * a / max_iterations

            for i in range(population_size):
                for j in range(dim):
                    r2 = random.uniform(0, 2 * math.pi)
                    r3 = random.uniform(0, 2)
                    r4 = random.random()
                    if r4 < 0.5:
                        solution[i][j] += r1 * math.sin(r2) * abs(r3 * best_solution[j] - solution[i][j])
                    else:
                        solution[i][j] += r1 * math.cos(r2) * abs(r3 * best_solution[j] - solution[i][j])
                solution[i] = self.boundary_check(solution[i], lower_bound, upper_bound)
                fitness[i] = self._obj_function(solution[i])

            for i in range(population_size):
                if fitness[i] > best_fitness:
                    best_fitness = fitness[i]
                    best_solution = solution[i].copy()
            iter_best.append(best_fitness)

        self.individ_save(self.file_name + '.chk', solution, fitness)

        return best_fitness
    
    
    def _obj_function(self, agent):
        try:
    
            command = './rastrign_func.py'                      #формируем команду для subprocess
            arg1 = str(1.56)
            arg2 = str(2.67)
            arg3 = str(7.87)
            arguments = [command, arg1, arg2, arg3]

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
            part = log_line

        except Exception as e:
            print(e)

        return part
    

    def boundary_check(value, lb, ub):
        for i in range(len(value)):
            value[i] = max(value[i], lb[i])
            value[i] = min(value[i], ub[i])
        return value
    

    def individ_load(self, filename, population_size):
        solution = []
        fitness = []
        with open(filename) as reader:
            lines = reader.readlines()
        

        for i in range(population_size):
            solution.append([float(num) for num in lines[i * 16 + 10].split()]) # в deepmethod это cтрока x
            fitness.append(float(lines[i * 16 + 1])) # в deepmethod это cost 

        print(solution)
        print(fitness)
        return solution, fitness

       
    def individ_save(self, filename, solution, fitness):
        with open(filename, "r") as reader:
            lines = reader.readlines()

        for i in range(len(fitness)):
            lines[i* 16 + 1] = str(fitness[i])
            lines[i* 16 + 10] = str(solution[i])

        with open(filename, "w") as writer:
            writer.writelines(lines[:len(fitness) * 16])