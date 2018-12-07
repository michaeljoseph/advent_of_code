from collections import Counter


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