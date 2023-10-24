t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    a %= 10
    if a == 0:
        print(10)
    else:
        temp = [a]
        while True:
            if (temp[-1]*a)%10 not in temp:
                temp.append((temp[-1]*a)%10)
            else:
                break
        print(temp[b%len(temp)-1])