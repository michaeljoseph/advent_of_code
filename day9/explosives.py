MARKER_START = '('
import re


def parse_marker(marker):
    return [int(x) for x in re.match(r'(\d*)x(\d*)', marker).groups()]


def extract_marker(data, current):
    marker_start = data.find(MARKER_START, current)
    if marker_start == -1:
        return False

    marker_end = data.find(')', marker_start)
    marker = data[marker_start+1:marker_end]
    return marker, marker_end


def decompress(data):
    decompressed_data = ''

    data = data.replace(' ', '')

    done = False
    current = 0

    if data.find(MARKER_START) == -1:
        done = True
        decompressed_data = data

    while not done:
        marker_start = data.find(MARKER_START, current)
        # no more markers, copy to end of data
        if marker_start == -1:
            done = True
            decompressed_data += data[current:]
            break
        else:
            # copy from current to marker_start
            decompressed_data += data[current: marker_start]

        marker_end = data.find(')', marker_start)
        marker = data[marker_start + 1: marker_end]
        num_chars, num_repeats = parse_marker(marker)

        current = marker_end + 1 + num_chars
        repeat_data = data[marker_end + 1: current]
        decompressed_data += repeat_data * num_repeats

    return decompressed_data


if __name__ == '__main__':
    import sys, io

    input_file = sys.argv[1]
    compressed = io.open(input_file).read().strip()

    decompressed = decompress(compressed)
    print(decompressed)
    print(len(decompressed))
