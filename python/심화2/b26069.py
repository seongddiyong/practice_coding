from sys import stdin
input = stdin.readline

n = int(input())
record = set()
turn = 0
for _ in range(n):
    a,b = input().strip().split()
    if a == "ChongChong" or b == "ChongChong":
        record.add(a)
        record.add(b)
    if a in record and b not in record:
        record.add(b)
    elif a not in record and b in record:
        record.add(a)
print(len(record))