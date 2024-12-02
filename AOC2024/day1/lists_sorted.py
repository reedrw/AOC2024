from io import TextIOWrapper

def gnome_sort(arr: list[int]) -> list[int]:
    sorted: list[int] = arr.copy()
    pos: int = 0
    hold: int = 0
    while (pos < len(sorted)):
        if (pos == 0 or sorted[pos] >= sorted[pos - 1]):
            pos = pos + 1
        else:
            hold = sorted[pos]
            sorted[pos] = sorted[pos - 1]
            sorted[pos - 1] = hold
            pos = pos - 1
    return sorted

f: TextIOWrapper = open("./input.txt", "r")
nums: list[str] = f.read().split()

list1: list[int] = []
list2: list[int] = []

for i in range(len(nums)):
    if (i % 2 == 0):
        list1.append(int(nums[i]))
    else:
        list2.append(int(nums[i]))

list1 = gnome_sort(list1)
list2 = gnome_sort(list2)
