from sys import stdin
n = int(stdin.readline().rstrip())
a = list(map(int, stdin.readline().rstrip().split()))
print(min(a),max(a))