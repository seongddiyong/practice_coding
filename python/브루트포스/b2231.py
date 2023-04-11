# from sys import stdin
# input = stdin.readline

# n = int(input())

# for i in range(1, n+1):
#     num = sum(map(int, str(i)))
#     num_plus = i + num
#     if num_plus == n:
#         print(i)
#         break
#     if i == n:
#         print(0)

from sys import stdin
input = stdin.readline

n = int(input())

for i in range(max(1, n-63), n+1):
    num = 0
    j = i
    while j > 0:
        num += j % 10
        j //= 10
    num_plus = i + num
    if num_plus == n:
        print(i)
        break
    if i == n:
        print(0)