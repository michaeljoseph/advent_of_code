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


def decompress(data, markers=False):
    decompressed_length = 0
    decompressed_data = ''

    data = data.replace(' ', '')

    done = False
    current = 0

    if data.find(MARKER_START) == -1:
        done = True
        decompressed_data = data
        decompressed_length = len(data)

    while not done:
        marker_start = data.find(MARKER_START, current)
        # no more markers, copy to end of data
        if marker_start == -1:
            done = True
            decompressed_length += len(data[current:])
            decompressed_data += data[current:]
            break
        else:
            # copy from current to marker_start
            decompressed_length += marker_start - current
            decompressed_data += data[current: marker_start]

        marker_end = data.find(')', marker_start)
        marker = data[marker_start + 1: marker_end]
        num_chars, num_repeats = parse_marker(marker)

        current = marker_end + 1 + num_chars
        repeat_data = data[marker_end + 1: current]

        if markers:
            repeat_data = decompress(repeat_data, markers=True)

        decompressed_data += repeat_data * num_repeats
        decompressed_length += len(repeat_data) * num_repeats

    # assert len(decompressed_data) == decompressed_length
    # print(len(decompressed_data), decompressed_length)
    return decompressed_data


def decompress_length(data):
    decompressed_length = 0
    data = data.replace(' ', '')

    done = False
    current = 0

    if data.find(MARKER_START) == -1:
        done = True
        decompressed_length = len(data)

    while not done:
        marker_start = data.find(MARKER_START, current)
        # no more markers, copy to end of data
        if marker_start == -1:
            done = True
            decompressed_length += len(data[current:])
            break
        else:
            # copy from current to marker_start
            decompressed_length += marker_start - current

        marker_end = data.find(')', marker_start)
        marker = data[marker_start + 1: marker_end]
        num_chars, num_repeats = parse_marker(marker)

        current = marker_end + 1 + num_chars
        repeat_data = data[marker_end + 1: current]

        decompressed_length += decompress_length(repeat_data) * num_repeats

    return decompressed_length

if __name__ == '__main__':
    import sys, io

    input_file = sys.argv[1]
    compressed = io.open(input_file).read().strip()

    # decompressed = decompress(compressed, markers=True)
    # print(len(decompressed))
    decompressed_length= decompress(compressed, markers=True)
    print(decompressed_length)
