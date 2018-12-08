from pprint import pprint
from datetime import datetime
from collections import defaultdict, Counter
from operator import itemgetter
import re


DATE_FORMAT = '%Y-%m-%d %H:%M'
GUARD_LOG_REGEX = re.compile(r"\[(\d*-\d*-\d* \d*:\d*)] (.*)")

def parse_log_line(log_line):
    timestamp, entry = GUARD_LOG_REGEX.match(log_line).groups()

    return datetime.strptime(timestamp, DATE_FORMAT), entry

def parse_guard_logs(list_of_logs):
    parsed_logs = [
        parse_log_line(log)
        for log in list_of_logs
    ]
    # https://stackoverflow.com/a/19901707
    return sorted(parsed_logs, key=itemgetter(0))


def most_minutes_asleep(list_of_logs):
    current_guard = asleep_at = None
    sleep_count = defaultdict(int)
    minutes_asleep = defaultdict(list)

    for timestamp, entry in parse_guard_logs(list_of_logs):
        if 'begins shift' in entry:
            current_guard = int(re.match(r"Guard #(\d*) begins shift", entry).groups()[0])
        elif 'falls asleep' in entry:
            # print(f"{current_guard} sleeps at {timestamp.minute}")
            asleep_at = timestamp.minute
        elif 'wakes up' in entry:
            # print(f"{current_guard} woke up at {timestamp.minute}")
            # print(f"{current_guard} slept for {timestamp.minute - asleep_at} minutes")
            sleep_count[current_guard] += timestamp.minute - asleep_at
            asleep_minutes = range(asleep_at, timestamp.minute)
            minutes_asleep[current_guard].extend(asleep_minutes)
            # print(f"{current_guard} was asleep for these minutes: {list(asleep_minutes)}")
            # print(f"{minutes_asleep}")

    return sleep_count, minutes_asleep


def best_guard_strategy_one(list_of_logs):
    sleep_count, minutes_asleep = most_minutes_asleep(list_of_logs)

    sleepiest_guard = sorted(sleep_count.items(), key=itemgetter(1), reverse=True)[0][0]
    sleepiest_minute = Counter(minutes_asleep[sleepiest_guard]).most_common()[0][0]

    return sleepiest_guard, sleepiest_minute


def best_guard_strategy_two(list_of_logs):
    _, minutes_asleep = most_minutes_asleep(list_of_logs)

    x = sorted(
        [
            (guard, Counter(minutes).most_common()[0])
            for guard, minutes in minutes_asleep.items()
        ],
        key=lambda y: y[1][1],
        reverse=True
    )
    best_guard = x[0]
    return best_guard[0], best_guard[1][0]