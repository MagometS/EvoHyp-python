from DeepSolution import DeepSolution
from Heuristics import Heuristics
'''
ds = DeepSolution()
ds.set_heuristic_combination("ABCD")
str = ds.get_heuristic_combination()
print(str)
'''
heuristics_obj = Heuristics()
heuristics_obj.run_heuristic('deep_rastr.ini')
