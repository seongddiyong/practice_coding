h,m = map(int, input().split())
time = int(input())

a = m+time
b = a//60
c = a%60

if a>59:
    if h+b-24 >= 0:
        h = h-24
    print(h+b,c)
else:
    print(h,a)