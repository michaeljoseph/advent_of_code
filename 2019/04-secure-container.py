import pytest


def meets_criteria(password):
    """
    It is a six-digit number.
    The value is within the range given in your puzzle input.
    Two adjacent digits are the same (like 22 in 122345).
    Going from left to right, the digits never decrease;

    :param password:
    :return:
    """
    str_password = str(password)
    right_length = len(str_password) == 6

    adjacent_same = False
    never_decreases = True
    for idx, char in enumerate(str_password):
        if (idx + 1) > len(str_password) - 1:
            continue

        if str_password[idx+1] == char:
            adjacent_same = True

        if int(str_password[idx+1]) < int(char):
            never_decreases = False

    return right_length and adjacent_same and never_decreases


@pytest.mark.parametrize('password, criteria', [
    (111111, True),
    (223450, False),
    (123789, False),
])
def test_meets_criteria(password, criteria):
    assert meets_criteria(password) == criteria


if __name__ == '__main__':
    passwords_that_meet_the_criteria = [
        password
        for password in range(152085, 670283)
        if meets_criteria(password)
    ]
    print(len(passwords_that_meet_the_criteria))
