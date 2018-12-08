import sys
from . import total_overlaps 

list_of_claims = open(sys.argv[1]).readlines()
print(total_overlaps(list_of_claims))