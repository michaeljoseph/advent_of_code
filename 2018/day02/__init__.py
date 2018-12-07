from collections import Counter
from itertools import permutations


def any_repeats(box_id: str, how_many: int):
    counter = Counter(box_id)

    repeats = [
        state 
        for state, frequency in counter.most_common()
        if frequency == how_many
    ]
    return any(repeats)


def checksum(list_of_box_ids):
    return ( 
        sum([
            any_repeats(box_id, 2)
            for box_id in list_of_box_ids
        ])
        *
        sum([
            any_repeats(box_id, 3)
            for box_id in list_of_box_ids
        ])
    )


def difference(first, second):
    assert len(first) == len(second)
    return sum(
        1
        for i in range(len(first))
        if first[i] != second[i]
    )
    

def letters_in_common(first, second):
    assert len(first) == len(second)
    return ''.join([
        first[idx]
        for idx in range(len(first))
        if first[idx] == second[idx]
    ])


def find_box_ids_with_difference(list_of_box_ids, distance):
    for first, second in permutations(list_of_box_ids, 2):
        if difference(first, second) == distance:
            return first, second

    return None, None