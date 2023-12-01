from DeepSolution import DeepSolution

ds = DeepSolution()
ds.set_heuristic_combination("ABCD")
str = ds.get_heuristic_combination()
print(str)