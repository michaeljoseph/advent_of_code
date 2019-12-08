from typing import List
from common import get_puzzle, configure_logging


def number_of_digits(layer, digit):
    return sum([
        1 if d == digit else 0
        for d in layer
    ])


def layer_with_fewest(layers, digit):
    lowest = 1000
    layer_idx = None
    for i, layer in enumerate(layers):
        num_digits = number_of_digits(layer, digit)
        if 0 < num_digits < lowest:
            lowest = num_digits
            layer_idx = i

    return layers[layer_idx]


def parse_image(image: List[str], height: int, width: int) -> List[List[str]]:
    layer_size = height * width
    return [
        image[x:x+layer_size]
        for x in range(0, len(image), layer_size)
    ]


def test_space_image_format():
    image_data = [x for x in '123456789012']
    width = 3
    height = 2
    layers = parse_image(image_data, height, width)
    assert len(layers) == 2

    assert layers[0] == ['1', '2', '3', '4', '5', '6']
    assert layers[1] == ['7', '8', '9', '0', '1', '2']

    zero_layer = layer_with_fewest(layers, '0')
    one_digits = number_of_digits(zero_layer, '1')
    two_digits = number_of_digits(zero_layer, '2')

    assert int(one_digits) * int(two_digits) == 1


if __name__ == '__main__':
    layers = parse_image([pixel for pixel in get_puzzle(8)], 6, 25)

    layer = layer_with_fewest(layers, '0')
    ones = number_of_digits(layer, '1')
    twos = number_of_digits(layer, '2')

    print(int(ones) * int(twos))
