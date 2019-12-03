from pathlib import Path

import requests
import browser_cookie3

AOC = 'https://adventofcode.com'


def get_puzzle(day):
    puzzle_input = Path(f'day{day}_input.txt')

    if not puzzle_input.exists():
        session = requests.Session()
        session.cookies = browser_cookie3.load()

        puzzle_input = Path(f'day{day}_input.txt')

        if not puzzle_input.exists():
            print(f'Downloading day {day} puzzle input')
            puzzle_input.write_text(session.get(f'{AOC}/2019/day/{day}/input').text)

    return puzzle_input.read_text()
