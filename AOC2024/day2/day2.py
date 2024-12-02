from io import TextIOWrapper

def is_safe(arr: list[int]) -> bool:
    is_increasing: bool = arr[1] > arr[0]
    for i in range(len(arr)):
        if ((i - 1) < 0): continue
        curr: int = arr[i]
        prev: int = arr[i-1]
        diff: int = curr - prev
        if (abs(diff) < 1 or abs(diff) > 3):
            return False
        if is_increasing:
            if (curr <= prev):
                return False
        else:
            if (prev <= curr):
                return False
    return True


f: TextIOWrapper = open("./input.txt", "r")
reports: list[list[int]] = [list(map(int, report.split())) for report in f.readlines()]
