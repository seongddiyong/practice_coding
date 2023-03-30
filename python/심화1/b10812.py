from sys import stdin

n,m = map(int, stdin.readline().split())
basket = [i+1 for i in range(n)]
for x in range(m):
    i,j,k = map(int, stdin.readline().split())
    i,j,k = i-1,j-1,k-1
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]
for _ in range(n):
    print(basket[_],end= " ")
