import sys
from collections import defaultdict

LOG_LEVELS = ("INFO", "DEBUG", "ERROR", "WARNING")


# decorator for handling file opening
def file_error(func):
    def inner_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError:
            sys.exit("File not found")
        except PermissionError:
            sys.exit("No permissions")
        except IsADirectoryError:
            sys.exit("Provide a file, not a directory")

    return inner_func


# reads all lines from file, returns a list of parsed lines
@file_error
def load_logs(file_path: str) -> list:
    logs = []
    with open(file_path, encoding="utf-8") as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                logs.append(parsed)
    return logs


# return a dictionary with parsed values
def parse_log_line(line: str) -> dict:
    try:
        date, time, log_level, info = line.strip().split(maxsplit=3)
        if log_level not in LOG_LEVELS:
            return {}
        return {
            "date": date,
            "time": time,
            "log_level": log_level,
            "info": info,
        }
    except ValueError:
        return {}


# returns a list of filtered logs by level
def filter_logs_by_level(logs: list, level: str) -> list:
    return [log for log in logs if log["log_level"] == level.upper()]


# returns a dictionary with log level and its count
def count_logs_by_level(logs: list) -> dict:
    if not logs:
        return {}

    level_count_dict = defaultdict(int)

    for log in logs:
        level_count_dict[log["log_level"]] += 1
    return dict(level_count_dict)


# displays log levels and corresponding counts
def display_log_counts(counts: dict):
    print(f"{'log level':<13}| count")
    print("-" * 13 + "|" + "-" * 10)
    for level, count in counts.items():
        print(f"{level:<13}| {count}")


if __name__ == "__main__":
    try:
        path = sys.argv[1]
    except IndexError:
        sys.exit("please enter file name")

    logs = load_logs(path)
    if not logs:
        sys.exit("no valid log records found")

    counts = count_logs_by_level(logs)
    display_log_counts(counts)

    if len(sys.argv) > 2:
        level = sys.argv[2]
        filtered = filter_logs_by_level(logs, level)
        if filtered:
            print(f"Log details for {level.upper()}")
            for log in filtered:
                print(f"{log['date']} {log['time']} - {log['info']}")
        else:
            print(f"no records for {level}")
