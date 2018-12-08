from .sleepy_guards import *

guard_logs = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
""".strip().splitlines()

def test_parse_log_line():
    assert parse_log_line(guard_logs[0]) == (
        datetime(1518, 11, 1, 0, 0), 'Guard #10 begins shift'
    )
    assert parse_log_line(guard_logs[1]) == (
        datetime(1518, 11, 1, 0, 5), 'falls asleep'
    )


unsorted_logs = """
[1518-06-25 23:58] Guard #1069 begins shift
[1518-09-16 00:24] falls asleep
[1518-04-06 00:56] wakes up
[1518-11-04 00:48] wakes up
""".strip().splitlines()

sorted_logs = [
    (datetime(1518, 4, 6, 0, 56), 'wakes up'),
    (datetime(1518, 6, 25, 23, 58), 'Guard #1069 begins shift'),
    (datetime(1518, 9, 16, 0, 24), 'falls asleep'),
    (datetime(1518, 11, 4, 0, 48), 'wakes up')
]

def test_sort_logs_by_date():
    assert parse_guard_logs(unsorted_logs) == sorted_logs

def test_strategy_one():
    assert best_guard_strategy_one(guard_logs) == (10, 24)

def test_strategy_two():
    assert best_guard_strategy_two(guard_logs) == (99, 45)