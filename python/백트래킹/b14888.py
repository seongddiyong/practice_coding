from sys import stdin
from itertools import permutations
input = stdin.readline

mmax = -1000000000
mmin = 1000000000
n = int(input())
a = list(map(int,input().split()))
temp = list(map(int, input().split()))
w = ['+','-','*','/']
operate = []
for i in range(len(w)):
    for j in range(temp[i]):
        operate.append(w[i])

for op in permutations(operate,n-1):
    total = a[0]
    for i in range(1,n):
        t = op[i-1]
        if t == "+":
            total += a[i]
        elif t == "-":
            total -= a[i]
        elif t == "*":
            total *= a[i]
        else:
            total = int(total/a[i])
    if total < mmin:
        mmin = total
    if total > mmax:
        mmax = total
print(mmax, mmin)