# import sys
# input = sys.stdin.readline

# while True:
#     n = int(input())+1
#     if n == 1:
#         break
#     if n == 2:
#         print(1)
#         continue
#     m = 2*(n-1)
#     result = [True]*(m+1)
#     for i in range(2,int(m**0.5)+1):
#         if result[i]:
#             for j in range(i*2,m+1,i):
#                 result[j] = False
#     print(result[n:m+1].count(True)) 

## 위가 내 코드 아래가 다른 사람 코드
# 훨씬 간단하고 시간도 몇 배로 빠르다. 메모리 또한 근소하게 적음
numbers = [0, 0] + [1 for i in range(2*123456-1)]
for i in range(2, 2*123456+1):
    if numbers[i]:
        for j in range(2*i, 2*123456+1, i):
            numbers[j] = 0

while True:
    n = int(input())
    if n == 0:
        break
    print(sum(numbers[n+1:2*n+1]))