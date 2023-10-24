n = int(input())
a = 0
cnt = 0
while True:
    cnt += 1
    a += cnt
    if a > n:
        break
print(cnt-1)