n = int(input())
s = input()
for i in range(n):
    list = [int(s[i]) for i in range(n)]
print(sum(list))