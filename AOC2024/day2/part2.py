#! /usr/bin/env python3

from day2 import is_safe, reports

num_safe: int = 0
for report in reports:
    if is_safe(report):
        num_safe += 1
    else:
        for i in range(len(report)):
            copy: list[int] = report.copy()
            copy.pop(i)
            if (is_safe(copy)):
                num_safe += 1
                break

print(num_safe)
