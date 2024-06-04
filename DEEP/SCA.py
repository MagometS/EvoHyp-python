import numpy as np
import configparser
import subprocess
import io
import random
import math
import os.path


class SCA:

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


        solution, fitness = self.individ_load(self.file_name + '.chk', population_size)

        # chkfile  = self.file_name + '.chk'

        # if os.path.exists(chkfile):
        #     solution, fitness = self.individ_load(self.file_name + '.chk', population_size)
        # else:
        #     solution = []
        #     fitness = []
        #     for i in range(population_size):
        #         temp_pos = [random.uniform(lower_bound, upper_bound) for j in range(dim)]
        #         solution.append(temp_pos)
        #         fitness.append(self._obj_function(temp_pos))
 
        
        iter_best = []
        best_fitness = min(fitness)
        print(best_fitness)
        index_best_fitness = fitness.index(best_fitness)
        best_solution = solution[index_best_fitness].copy()  # the position of the best-so-far candidate

        
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
                # print("sca solution ", solution[i])

            for i in range(population_size):
                if fitness[i] < best_fitness:
                    best_fitness = fitness[i]
                    best_solution = solution[i].copy()
            iter_best.append(best_fitness)

        self.individ_save(self.file_name + '.chk', solution, fitness)

        # print("index", index_best_fitness)
        # print('sca best_solution:', best_solution)

        # index_best_fitness = fitness.index(best_fitness)
        # best_solution = solution[index_best_fitness].copy()

        best_solution_str = [str(num) for num in best_solution]
        
        # print("sca_fitline " + str(best_fitness) + " " + " ".join(best_solution_str))

        #выводить в форме 26.000000000000 p[0]:-0.465405203240 p[1]:-2.002952118361 p[2]:-3.207954750384 p[3]:-0.885287699249 p[4]:-2.157680026563 p[5]:-1.658628386335 p[6]:-0.918774186489 p[7]:-1.393377595340 p[8]:-1.446648095796 p[9]:-1.257747608850
        format_best_fitness = "{:.12f}".format(best_fitness)
        
        # return str(best_fitness) + " " +  " ".join(best_solution_str)
        return format_best_fitness + " " +  " ".join(best_solution_str)

    
    
    def _obj_function(self, agent):
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
    

    def boundary_check(self, value, lb, ub):
        for i in range(len(value)):
            value[i] = max(value[i], lb)
            value[i] = min(value[i], ub)
        return value
    

    def individ_load(self, filename, population_size):
        solution = []
        fitness = []
        with open(filename) as reader:
            lines = reader.readlines()

        for i in range(population_size):
            solution.append([float(num) for num in lines[i * 16 + 10].split()]) # в deepmethod это cтрока x
            fitness.append(float(lines[i * 16 + 1])) # в deepmethod это cost 
            # fitness.append([float(num) for num in lines[i * 16 + 1]])

        # print(solution)
        # print(fitness)
        return solution, fitness

       
    def individ_save(self, filename, solution, fitness):
        if os.path.exists(filename) == False:
            with open(filename, "w") as writer:
                pass

        with open(filename, "r") as reader:
            lines = reader.readlines()
        

        for i in range(len(fitness)):
            solution_str = [str(num) for num in solution[i]]

            lines[i* 16 + 1] = str(fitness[i]) + '\n'
            str_x = " ".join(solution_str) + '\n'
            lines[i* 16 + 10] = str_x
            lines[i* 16 + 12] = str_x


        with open(filename, "w") as writer:
            writer.writelines(lines[:len(fitness) * 16])