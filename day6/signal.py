
def extract_column(data, column_number):
    return ''.join([
        row[column_number] for row in data
    ])


def transpose_data(data):
    transposed = []
    for col in range(len(data[0])):
        transposed.append(extract_column(data, col))

    return transposed


def error_correct_character(column_data):
    from collections import Counter
    c = Counter(column_data)
    return c.most_common(1)[0][0]


def error_correct_data(data):
    corrected_code = []
    for character_col in transpose_data(data):
        corrected_code.append(error_correct_character(character_col))

    return ''.join(corrected_code)

if __name__ == '__main__':
    import sys, io

    input_file = sys.argv[1]
    messages = [x.strip() for x in io.open(input_file).readlines()]

    print(error_correct_data(messages))