from sys import stdin
input = stdin.readline

n = int(input())
result = []

for i in range(2,n+1):
        if n%i == 0:
            while n%i ==0:
                print(i)
                n /= i

# i = 2
# while n!=1:
#     if n%i == 0:
#         print(i)
#         n /= i
#     else:
#         i+=1