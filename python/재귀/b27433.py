def fac(a):
    if a > 1:
        return a * fac(a-1)
    return a
n = int(input())
if n == 0:
    print(1)
else:
    print(fac(n))