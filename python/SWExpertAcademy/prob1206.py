for t in range(10):
    N = int(input())
    s = list(map(int, input().split()))
    ans = 0
    i = 2
    while i < N-1:
        if s[i+1] < s[i] and s[i+2] < s[i] and s[i-1] < s[i] and s[i-2] < s[i]:
            temp = max(s[i+1],s[i+2],s[i-1],s[i-2])
            ans += (s[i] - temp)
            i += 3
        else:
            i += 1
    print(f'#{t+1} {ans}')