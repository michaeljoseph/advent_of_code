import md5
import sys


def sequential_digit(hash):
    return hash[5]


def generate_password_digits(door_id, limit=8):
    found = 0
    x = 1
    while found < limit:
        current = door_id + str(x)
        hash = str(md5.new(current).hexdigest())

        if hash.startswith('00000'):
            digit = sequential_digit(hash)
            if digit is not None:
                found += 1
                yield digit
        x += 1


def find_password_digits(door_id, password_length=8):
    password = [None] * password_length

    password_found = False
    x = 1
    while not password_found:
        current = door_id + str(x)

        hash = str(md5.new(current).hexdigest())
        if hash.startswith('00000'):
            try:
                position = int(hash[5])
                value = hash[6]

                if password[position] is None:
                    password[position] = value

            except (ValueError, IndexError):
                x += 1
                continue

            print(hash, position, value, password)
        x += 1
        password_found = all([digit is not None for digit in password])

    return ''.join(password)


def door_id_password(door_id):
    return ''.join([
        password_digit for password_digit in generate_password_digits(door_id)
    ])

if __name__ == '__main__':
    door_id = sys.argv[1]
    # print(door_id_password(door_id))
    print(find_password_digits(door_id))
