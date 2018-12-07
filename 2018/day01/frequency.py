import sys
from pprint import pprint
from collections import Counter 


def update_frequency(current, change):
    calculation_string = f"{current} {change.strip()}"
    return eval(calculation_string)


def calculate_frequency(frequency_changes: list, current_frequency = 0):
    frequency_states = []

    for frequency_change in frequency_changes:
        current_frequency = update_frequency(current_frequency, frequency_change)
        frequency_states.append(current_frequency)

    return frequency_states[-1], frequency_states


def find_first_duplicate(frequency_changes: list):
    duplicate_found = False
    current_frequency = 0
    all_states = [current_frequency]

    counter = Counter()

    while not duplicate_found:
        current_frequency, states = calculate_frequency(frequency_changes, current_frequency)
        all_states.extend(states)

        counter = Counter(all_states)

        more_than_one = [state for state, frequency in counter.most_common() if frequency > 1]
        if more_than_one:
            if len(more_than_one) > 0:
                first_match = states.index(more_than_one[0])
                for match in more_than_one[1:]:
                    current_match = states.index(match)
                    if current_match < first_match:
                        first_match = current_match 

                return states[first_match]
            return more_than_one.pop()

    return None 


if __name__ == '__main__':
    input_file = sys.argv[1]

    frequency_changes = open(input_file).readlines()

    end_freq, states = calculate_frequency(frequency_changes)
    print(end_freq)

    print(find_first_duplicate(frequency_changes))