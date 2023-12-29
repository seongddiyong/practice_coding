T = int(input())
for t in range(1,T+1):
    l = list(map(int, input().split()))
    answer = 0
    print(f"#{t} {sum([i for i in l if i%2 == 1])}")