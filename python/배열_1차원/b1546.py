n = int(input())
avg = 0
score = list(map(int, input().split()))
max_score = max(score)
for a in score:
    avg += (a/max_score)*100
print(avg/n)