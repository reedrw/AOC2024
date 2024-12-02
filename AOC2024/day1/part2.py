#! /usr/bin/env python3

from lists_sorted import list1, list2

data = {}

for i in range(len(list1)):
    data[list1[i]] = 0

for i in range(len(list2)):
    if list2[i] in data:
        data[list2[i]] += 1

data = dict((k,v) for k,v in data.items() if v > 0)

similarity_score = 0
for k,v in data.items():
    similarity_score += k * v

print(similarity_score)
