import md5
import sys


def generate_password_digits(door_id, limit=8):
    found = 0
    x = 1
    while found < limit:
        current = door_id + str(x)
        hash = str(md5.new(current).hexdigest())

        if hash.startswith('00000'):
            found += 1
            yield hash[5]
        x += 1


door_id = sys.argv[1]

print(''.join([password_digit for password_digit in generate_password_digits(door_id)]))
