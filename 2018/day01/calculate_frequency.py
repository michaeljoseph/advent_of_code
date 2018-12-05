import sys
from pprint import pprint

if __name__ == '__main__':
    input_file = sys.argv[1]

    current_frequency = 0

    with open(input_file) as fh:
        for frequency_change in fh.readlines():
            calculation_string = f"{current_frequency} {frequency_change.strip()}"
            pprint(calculation_string)
            current_frequency = eval(calculation_string)

    print(current_frequency)