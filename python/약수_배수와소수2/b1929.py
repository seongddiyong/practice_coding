from sys import stdin
input = stdin.readline

m,n=map(int,input().split())

prime_list = [True]*(n+1)
prime_list[0] = False
prime_list[1] = False
for i in range(2,int(n**0.5)+1):
    if prime_list[i]:
        for j in range(i*2,n+1,i):
            prime_list[j] = False
for i in range(m,n+1):
    if prime_list[i]:
        print(i)