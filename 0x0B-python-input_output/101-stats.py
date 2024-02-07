#!/usr/bin/python3
"""Read stdin module."""
import sys


def print_stats(total_size, status_counts):
    """Function definition."""
    print("File size: {:d}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))


def main():
    """Function definition."""
    total_size = 0
    status_counts = {'200': 0, '301': 0, '400': 0, '401': 0,
                     '403': 0, '404': 0, '405': 0, '500': 0}
    count = 0

    try:
        for line in sys.stdin:
            count += 1
            split_line = line.split()
            total_size += int(split_line[-1])

            status_code = split_line[-2]
            if status_code in status_counts:
                status_counts[status_code] += 1

            if count % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)


if __name__ == "__main__":
    main()
