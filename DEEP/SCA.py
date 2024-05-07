import numpy as np
import configparser
import subprocess
import io


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
        population = np.random.uniform(lower_bound, upper_bound, (population_size, dim))

        # best_solution = None # эти два параметра надо считыать из ini/chk и вписыать обратно
        # best_fitness = float('inf')

        best_solution, best_fitness = self.individ_load(self.file_name + '.chk')

        for _ in range(max_iterations):
            for agent in population:
                fitness = self._obj_function(agent)
                if fitness < best_fitness:
                    best_fitness = fitness
                    best_solution = agent

                r1 = np.random.random(dim)  # Random vector [0, 1]
                r2 = np.random.random(dim)  # Random vector [0, 1]

                agent = agent + r1 * np.sin(r2) * (best_solution - agent) + a * (2 * r1 - 1)  # Update step

                agent = np.minimum(np.maximum(agent, lower_bound), upper_bound)

        self.individ_save(self.file_name + '.chk', best_solution, best_fitness)

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


    def individ_load(self, filename, population_size):

        solution = []
        fitness = []
        with open(filename) as reader:
            lines = reader.readlines()
        

        for i in range(population_size):
            solution.append([float(num) for num in lines[i * 16 + 10].split()]) # в deepmethod это cтрока x
            fitness.append(float(lines[i * 16 + 1])) # в deepmethod это cost 

        # print(solution)
        # print(fitness)
        return solution, fitness

       

    def individ_save(self, filename, solution, fitness):
        with open(filename, "r") as reader:
            lines = reader.readlines()

        last_16_lines = lines[-16:]

        last_16_lines[0] = str(fitness)
        last_16_lines[9] = str(solution)

        with open(filename, "w") as writer:
            writer.writelines(last_16_lines)



            
        



        

    
        

