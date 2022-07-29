#!/usr/bin/python3
"""a script that reads stdin line by line and computes metrics"""
import sys

accepted_codes = [200, 301, 400, 401, 403, 404, 405, 500]
codes = {}
number_of_lines = 0
size = 0
try:
    for line in sys.stdin:
        if number_of_lines < 10:
            number_of_lines += 1
        else:
            print(f"File size: {size}")
            for i in sorted(codes):
                print(f"{i}: {codes[i]}")
            number_of_lines = 1
        line_list = line.split()
        try:
            size += int(line_list[-1])
        except (TypeError, ValueError):
            pass
        try:
            code = int(line_list[-2])
            if code in accepted_codes:
                if codes.get(str(code), -10) == -10:
                    codes[str(code)] = 1
                else:
                    codes[str(code)] = codes[str(code)] + 1
        except (IndexError, ValueError):
            pass
    print(f"File size: {size}")
    for i in sorted(codes):
        print(f"{i}: {codes[i]}")
except KeyboardInterrupt:
    print(f"File size: {size}")
    for i in sorted(codes):
        print(f"{i}: {codes[i]}")
    raise
