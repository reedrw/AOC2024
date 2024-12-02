#! /usr/bin/env python3

from lists_sorted import list1, list2

diff: int = 0
for i in range(len(list1)):
    diff += abs(list1[i] - list2[i])

print(diff)
