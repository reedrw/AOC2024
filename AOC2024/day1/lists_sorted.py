def gnomeSort(arr):
    pos = 0
    hold = 0
    while (pos < len(arr)):
        if (pos == 0 or arr[pos] >= arr[pos - 1]):
            pos = pos + 1
        else:
            hold = arr[pos]
            arr[pos] = arr[pos - 1]
            arr[pos - 1] = hold
            pos = pos - 1

f = open("./input.txt", "r")
nums = f.read().split()

list1 = []
list2 = []

for i in range(len(nums)):
    if (i % 2 == 0):
        list1.append(nums[int(i)])
    else:
        list2.append(nums[int(i)])

gnomeSort(list1)
gnomeSort(list2)

list1 = [int(i) for i in list1]
list2 = [int(i) for i in list2]
