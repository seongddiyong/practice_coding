T = int(input())
for t in range(1,T+1):
    print(f"#{t} {max(list(map(int, input().split())))}")