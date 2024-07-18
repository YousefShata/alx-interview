#!/usr/bin/python3
"""
Log parsing module
"""
import sys
import signal
import re


total_size = 0
lines_num = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

log_pattern = re.compile(
    r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    r' - \[(.*?)\]'
    r' "GET /projects/260 HTTP/1.1"'
    r' (\d{3})'
    r' (\d+)$'
)


def print_statistics():
    """
    Print the collected statistics
    """
    print(f"File size: {total_size}")
    for status in sorted(status_count):
        if status_count[status] > 0:
            print(f"{status}: {status_count[status]}")


def signal_handler(sig, frame):
    """Handle keyboard interruption to print statistics."""
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    match = log_pattern.match(line.strip())
    if match:
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        total_size += file_size

        if status_code in status_count:
            status_count[status_code] += 1

        lines_num += 1

        if lines_num % 10 == 0:
            print_statistics()

print_statistics()
