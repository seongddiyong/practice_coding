n = int(input())
a = list(map(int, input().split()))
find = int(input())
result = 0

for i in a:
    if i == find:
        result += 1
print(result)

## 아래의 코드가 더 짧고 편하다.
# n = int(input())
# a = list(map(int, input().split()))
# find = int(input())

# print(a.count(find))