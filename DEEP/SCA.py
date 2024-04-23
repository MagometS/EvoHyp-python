import numpy as np
import configparser
import subprocess
import io

class SCA:

    #obj_function = None
    file_name = None
    

    def __init__(self, file_name, obj_function):
        self.file_name = file_name
        #self.obj_function = obj_function
        

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

        best_solution = None
        best_fitness = float('inf')

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

    
        

