n = int(input())
test = list(map(int, input().split()))
answer = 0
for i in test:
    result = 0
    for k in range(1,i):
        if i%k == 0:
            result += 1
    if result == 1:
        answer += 1
print(answer)