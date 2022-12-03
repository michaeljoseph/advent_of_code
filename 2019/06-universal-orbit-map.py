import logging
from typing import List, Dict

from common import get_puzzle, configure_logging

configure_logging()
log = logging.getLogger(__name__)


class UniversalOrbitMap:
    def __init__(self, orbit_data: List[str]):
        self.orbits = {
            orbit.split(')')[1]: orbit.split(')')[0]
            for orbit in orbit_data
        }

    @property
    def planets(self):
        return self.orbits.keys()

    def orbit_path(self, planet):
        dorb = self.orbits.get(planet)

        if dorb is None:
            return []
        # print(locals())
        return [dorb] + self.orbit_path(dorb)

    def indirectly_orbits(self, planet):
        return self.orbit_path(planet)[1:]

    def directly_orbits(self, planet):
        path = self.orbit_path(planet)
        return path[0] if path else None

    def sum_orbits(self, planet):
        return (1 if self.directly_orbits(planet) else 0) + len(self.indirectly_orbits(planet))

    def total_orbits(self):
        return sum([self.sum_orbits(p) for p in self.planets])


def test_orbits():
    orbit_data = [
        'COM)B',
        'B)C',
        'C)D',
        'D)E',
        'E)F',
        'B)G',
        'G)H',
        'D)I',
        'E)J',
        'J)K',
        'K)L',
    ]
    uom = UniversalOrbitMap(orbit_data)

    # D directly orbits C and
    assert uom.directly_orbits('D') == 'C'
    # indirectly orbits B and COM
    assert uom.indirectly_orbits('D') == ['B', 'COM']
    # a total of 3 orbits.
    assert uom.sum_orbits('D') == 3

    # L directly orbits K and
    assert uom.directly_orbits('L') == 'K'
    # indirectly orbits J, E, D, C, B, and COM
    assert uom.indirectly_orbits('L') == ['J', 'E', 'D', 'C', 'B', 'COM']
    # a total of 7 orbits.
    assert uom.sum_orbits('L') == 7

    # COM orbits nothing.
    assert uom.directly_orbits('COM') is None
    assert uom.indirectly_orbits('COM') == []

    # The total number of direct and indirect orbits in this example is 42.
    assert uom.total_orbits() == 42


if __name__ == '__main__':
    # What is the total number of direct and indirect orbits in your map data?
    uom = UniversalOrbitMap(get_puzzle(6).strip().split('\n'))
    print(uom.total_orbits())
