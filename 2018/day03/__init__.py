from itertools import permutations, product
import re

def claim_to_co_ords(x, y, w, h):
    # https://stackoverflow.com/a/9082878
    return list(product(range(x, x+w), range(y, y+h)))


def overlaps(claim_a, claim_b):
    intersects = set(claim_to_co_ords(*claim_a)) & set(claim_to_co_ords(*claim_b))
    # print(locals())
    return len(intersects)


CLAIM_REGEX=re.compile(r"(#\d*) @ (\d*),(\d*): (\d*)x(\d*)")
def parse_claim(claim):
    claim_id, x, y, w, h = CLAIM_REGEX.match(claim).groups()
    return int(x), int(y), int(w), int(h)
    

def parse_claims(list_of_claims):
    return [
        parse_claim(claim)
        for claim in list_of_claims
    ]


def total_overlaps(list_of_claims):
    combos = set(list(permutations(parse_claims(list_of_claims), 2)))
    return sum(set([
        overlaps(claim_a, claim_b)
        for claim_a, claim_b in combos 
    ]))