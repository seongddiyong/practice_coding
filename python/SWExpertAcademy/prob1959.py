T = int(input())
for t in range(1,T+1):
    g1, g2 = map(int, input().split())
    n = list(map(int, input().split()))
    m = list(map(int, input().split()))
    answer = []
    if len(n) > len(m):
        m,n = n,m
    for i in range(len(m)-len(n)+1):
        a=0
        for j in range(len(n)):
            a += m[i+j]*n[j]
        answer.append(a)
    print(f"#{t} {max(answer)}")