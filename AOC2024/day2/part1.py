#! /usr/bin/env python3

from io import TextIOWrapper
from day2 import is_safe, reports

num_safe: int = 0
for report in reports:
    if is_safe(report): num_safe += 1

print(num_safe)
