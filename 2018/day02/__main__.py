import sys
from . import checksum

print(checksum(open(sys.argv[1]).readlines()))