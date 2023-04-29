from sys import stdin
input= stdin.readline
n = int(input())
for _ in range(n):
    data = list(input().rstrip())
    ans = []
    for i in data:
        if i == "(":
            ans.append(1)
        elif i == ")":
            if ans:
                ans.pop()
            else:
                print("NO")
                break
    else:
        if not ans:
            print("YES")
        else:
            print("NO")