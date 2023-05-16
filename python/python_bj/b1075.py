from sys import stdin
input = stdin.readline
n,f = map(int,input().split())
str_n = list(str(n))
print(str_n[-2::])