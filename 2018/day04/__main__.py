import sys
from .sleepy_guards import * 

input_file = sys.argv[1]

guard_logs = open(input_file).readlines()

guard, minute =  best_guard_strategy_one(guard_logs)
print(guard * minute)

guard, minute =  best_guard_strategy_two(guard_logs)
print(guard * minute)