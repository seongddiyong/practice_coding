n = int(input())
if n < 100:
    print(n)
elif 100 <= n < 111:
    print(99)
else:
    cnt = 99
    for i in range(111,n+1):
        temp = str(i)
        s = int(temp[0]) - int(temp[1])
        if (int(temp[1]) - int(temp[2])) == s:
            cnt += 1
    print(cnt)