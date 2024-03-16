import numpy as np

class SCA:

    def create_solution(obj_func, dim, max_iter, lb, ub):
        population_size = 10
        a = 2  # Constant in SCA formula

        # Initialize the population within the bounds [lb, ub]
        population = np.random.uniform(lb, ub, (population_size, dim))

        best_solution = None
        best_fitness = float('inf')

        for _ in range(max_iter):
            for agent in population:
                fitness = obj_func(agent)
                if fitness < best_fitness:
                    best_fitness = fitness
                    best_solution = agent

                r1 = np.random.random(dim)  # Random vector [0, 1]
                r2 = np.random.random(dim)  # Random vector [0, 1]

                agent = agent + r1 * np.sin(r2) * (best_solution - agent) + a * (2 * r1 - 1)  # Update step

            # Boundary check
                agent = np.minimum(np.maximum(agent, lb), ub)

        return best_solution, best_fitness
