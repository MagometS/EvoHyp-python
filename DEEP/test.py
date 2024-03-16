import sys

sys.path.append('/home/magomet/EvoHyp-python/GeneticAlgorithm')

from DeepSolution import DeepSolution
from Heuristics import Heuristics



'''
ds = DeepSolution()
ds.set_heuristic_combination("ABCD")
str = ds.get_heuristic_combination()
print(str)
'''
heuristics_obj = Heuristics()  # creating Heuristics object
section_name = "default_settings22"  # getting section name from map
fit = heuristics_obj.run_heuristic("deep_rastr.ini", section_name)  # calling run_heuristic
