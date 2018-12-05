"""

In a valid triangle,
the sum of any two sides
must be larger than the remaining side.
For example,
the "triangle" given above is impossible, because 5 + 10 is not larger than 25.
"""


from itertools import permutations


def valid_triangle_sides(x, y, z):
    return (int(x)+int(y)) > int(z)


def possible_triangle(triangle):
    for x, y, z in permutations(triangle, 3):
        if not valid_triangle_sides(x, y, z):
            return False

    return True


def tests():
    impossible = [5, 10, 25]
    assert not possible_triangle(impossible)
    column = [101, 102, 103]
    assert possible_triangle(column)


def count_possible_triangles(triangles):
    possible_triangles = 0
    for triangle in triangles:
        possible = possible_triangle(triangle)
        possible_triangles += 1 if possible else 0
        # print('{} - {}'.format(triangle, possible))
    return possible_triangles


if __name__ == '__main__':
    import sys
    import io

    input_file = sys.argv[1]
    file_contents = io.open(input_file).readlines()
    # triangle_input = [x.split() for x in file_contents]
    #
    # print(count_possible_triangles(triangle_input))

    columns = []
    for x in file_contents:
        for i, column in enumerate(x.split()):
            print(locals())
            columns[i].append(column)

    print(columns)

