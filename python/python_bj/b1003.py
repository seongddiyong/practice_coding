from sys import stdin

a = [1,0,1]
b = [0,1,1]

def fibo(n):
    if len(a) <= n:

t = int(stdin.readline())

for i in range(t):
    n = int(stdin.readline())
    fibo(n)

print(a," ",b)
print("test")