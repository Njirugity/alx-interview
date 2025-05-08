#!/usr/bin/env python3
"""A script that reads stdin line by line and computes metrics"""
import sys
import re


def print_log():
    """
     Return:
            -Total file size
            -Status code and its count
    """

    print(f'File size: {total}')
    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")


total = 0
status_count = {}
line_count = 0


try:
    for line in sys.stdin:
        match = re.search(r'"[^"]+" (\d{3}) (\d+)', line)
        if match:
            code = match.group(1)
            file_size = match.group(2)
            total += int(file_size)
            if code in status_count:
                status_count[code] += 1
            else:
                status_count[code] = 1

        line_count += 1
        if line_count % 10 == 0:
            print_log()

except KeyboardInterrupt:
    print_log()
    raise

print_log()
