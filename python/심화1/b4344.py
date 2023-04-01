from sys import stdin
input = stdin.readline

c = int(input())
for i in range(c):
    result = 0
    score = list(map(int, input().split()))
    avg = sum(score[1:])/score[0]
    for j in score[1:]:
        if avg < j:
            result += 1

    a = "{:.3f}%".format(round((result/score[0])*100,3))
    print(a)

