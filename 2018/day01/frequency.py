import sys
from pprint import pprint
from collections import Counter 


def calculate_frequency(frequency_changes: list, current_frequency = 0):
    frequency_states = []

    for frequency_change in frequency_changes:
        calculation_string = f"{current_frequency} {frequency_change.strip()}"

        current_frequency = eval(calculation_string)

        frequency_states.append(current_frequency)

    return frequency_states[-1], frequency_states


def find_first_duplicate(frequency_changes: list):
    duplicate_found = False
    current_frequency = 0
    all_states = [current_frequency]

    while not duplicate_found:
        current_frequency, states = calculate_frequency(frequency_changes, current_frequency)
        all_states.extend(states)

        more_than_one = [
            state
            for state, frequency in Counter(all_states).most_common()
            if frequency > 1
        ]

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