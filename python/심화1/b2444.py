n = int(input())
for i in range(n*2-1):
    if i < n:
        print(" "*(n-i-1)+"*"*(i*2+1))
    else:
        print(" "*(i-n+1)+"*"*((2*n-2-i)*2+1))