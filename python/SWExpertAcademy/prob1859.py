T = int(input())
for t in range(1,T+1):
    n = int(input())
    num = list(map(int, input().split()))
    spend = pocket = earn = 0
    while True:
        if len(num) == 1:
            break
        maxIdx = num.index(max(num))
        front = num[:maxIdx]
        spend += sum(front)
        earn += len(front)*num[maxIdx]
        if maxIdx != len(num)-1:
            num = num[maxIdx+1:]
        else: break
    print(f'#{t} {earn - spend}')