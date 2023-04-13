from sys import stdin
input = stdin.readline().rstrip
n = input()
num = []
for i in range(len(n)):
    num.append(int(n[i]))
for i in sorted(num, reverse=True):
    print(i, end="")