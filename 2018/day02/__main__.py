import sys
from . import checksum, find_box_ids_with_difference, letters_in_common

list_of_box_ids = open(sys.argv[1]).readlines()

print(checksum(list_of_box_ids))

first, second = find_box_ids_with_difference(list_of_box_ids, 1)
print(letters_in_common(first, second))