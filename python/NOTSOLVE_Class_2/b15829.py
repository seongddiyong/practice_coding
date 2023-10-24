from sys import stdin
from string import ascii_lowercase
input = stdin.readline
n = int(input())
s = input().rstrip()
d = {}
for k,i in enumerate(ascii_lowercase):
	d[i] = k+1
m = [d[s[i]]*(31**i) for i in range(n)]
print(sum(m)%1234567891)