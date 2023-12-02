class Combinations:
    def __init__(self, recombination_gamma, recombination_strategy, gamma_init):
        self.recombination_gamma = recombination_gamma
        self.recombination_strategy = recombination_strategy
        self.gamma_init = gamma_init

    @staticmethod
    def comb_set():
        with open("comb_parametrs.txt", "r") as file:
            lines = file.readlines()

        recombination_gammas = []
        recombination_strategies = []
        gamma_inits = []
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line.startswith("[recombination_gamma]"):
                i += 1
                while not lines[i].startswith("[recombination_strategy]"):
                    recombination_gammas.append(lines[i].strip())
                    i += 1
            if line.startswith("[recombination_strategy]"):
                i += 1
                while not lines[i].startswith("[gamma_init]"):
                    recombination_strategies.append(lines[i].strip())
                    i += 1
            if line.startswith("[gamma_init]"):
                i += 1
                while i < len(lines):
                    gamma_inits.append(lines[i].strip())
                    i += 1

        comb = []
        for recombination_strategy in recombination_strategies:
            for gamma_init in gamma_inits:
                for recombination_gamma in recombination_gammas:
                    comb.append(Combinations(recombination_gamma, recombination_strategy, gamma_init))

        for combination in comb:
            print(combination.recombination_strategy, end=' ')
            print(combination.gamma_init, end=' ')
            print(combination.recombination_gamma, end=' ')
            print()

        return comb
