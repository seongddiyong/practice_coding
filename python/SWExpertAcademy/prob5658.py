T = int(input())
for t in range(1,T+1):
    N, K = map(int, input().split())
    s = list(input())
    standard = len(s)//4
    temp = []
    for rotations in range(standard):
        for i in range(0,len(s),standard):
            a = int(''.join(s[i:i+standard]),16)
            if a not in temp:
                temp.append(a)
        s.append(s.pop(0))
    temp.sort(reverse=True)
    print(f'#{t} {temp[K-1]}')