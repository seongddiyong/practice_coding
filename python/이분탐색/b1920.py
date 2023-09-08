from sys import stdin
input = stdin.readline

def binary_search(target, data):
    start = 0
    end = len(data)-1
    while start <= end:
        mid = (start+end)//2
        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1
    return 0

n = int(input())
data = list(sorted(list(map(int, input().split()))))
m = int(input())
target = list(map(int, input().split()))

for i in target:
    print(binary_search(i, data))