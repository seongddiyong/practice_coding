n,m = map(int, input().split())
answer = 0
if n < 11:
    answer += (10 - n)
    n = 11
for i in range(n,m+1):
    if str(i)[::-1] == str(i):
        answer += 1
print(answer)