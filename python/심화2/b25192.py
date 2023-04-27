from sys import stdin
input = stdin.readline

n = int(input())
record = set()
result = 0
for _ in range(n):
    name = input().strip()
    if name == 'ENTER':
        record = set()
    elif name not in record:
        record.add(name)
        result += 1
print(result)