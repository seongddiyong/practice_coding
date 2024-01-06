from collections import Counter
T = int(input())
for t in range(1,T+1):
    temp = int(input())
    li = list(map(int, input().split()))
    answer = Counter(li).most_common()
    print(f"#{temp} {answer[0][0]}")