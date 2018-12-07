import sys
from .frequency import calculate_frequency, find_first_duplicate

input_file = sys.argv[1]

frequency_changes = open(input_file).readlines()

end_freq, states = calculate_frequency(frequency_changes)
print(end_freq)

print(find_first_duplicate(frequency_changes))
