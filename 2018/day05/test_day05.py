from pprint import pprint
import pytest

def simplify(polymer):
    redux = []
    idx = 0

    while idx < len(polymer) - 1:
        previous = polymer[idx]
        current = polymer[idx + 1]
        idx += 1

        has_reaction = (
            current != previous and 
            current.lower() == previous.lower()
        )

        if has_reaction:
            idx += 1
        else:
            redux.append(previous)
            if (idx + 1) == len(polymer):
                redux.append(current)

    return ''.join(redux)


def reacts(polymer):
    current, previous = polymer
    return (
        current != previous and 
        current.lower() == previous.lower()
    )


@pytest.mark.parametrize('polymer, result', [
    ('aA', True),
    ('ab', False),
])
def test_reacts(polymer, result):
    assert reacts(polymer) == result

@pytest.mark.parametrize('polymer, reduced', [
    ('aA', ''),
    ('abBA', 'aA'),
    # ('abAB', 'abAB'),
    # ('aabAAB', 'aabAAB'),
])
def ixtest_simplify(polymer, reduced):
    assert simplify(polymer) == reduced


def reduce_polymer(polymer):
    redux = []
    idx = 0

    while idx < len(polymer) - 1:
        previous = polymer[idx]
        current = polymer[idx + 1]
        idx += 1

        has_reaction = (
            current != previous and 
            current.lower() == previous.lower()
        )
        print(locals())

        if not has_reaction: 
            print(f"pass through {previous}")
            redux.append(previous)

            if (idx + 1) == len(polymer):
                redux.append(current)
        else:
            print('reaction!')
            idx += 1

    return ''.join(redux)


@pytest.mark.parametrize('polymer, reduced', [
    ('aA', ''),
    ('abBA', ''),
    ('abAB', 'abAB'),
    ('aabAAB', 'aabAAB'),
    # ('dabAcCaCBAcCcaDA', 'dabCBAcaDA'),
])
def xtest_reduce_polymer(polymer, reduced):
    assert reduce_polymer(polymer) == reduced