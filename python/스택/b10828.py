from sys import stdin
input = stdin.readline

n = int(input())
temp = []
for i in range(n):
    a = input().strip()
    b = a.split(" ")
    match b[0]:
        case "push":
            temp.append(int(b[1]))
        case "top":
            if len(temp) == 0:
                print(-1)
            else: print(temp[-1])
        case "pop":
            if len(temp) == 0:
                print(-1)
            else:
                print(temp[-1])
                del temp[-1]
        case "size":
            print(len(temp))
        case "empty":
            if len(temp) == 0:
                print(1)
            else: print(0)