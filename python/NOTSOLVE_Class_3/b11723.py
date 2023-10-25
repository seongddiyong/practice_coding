import sys
input = sys.stdin.readline

m = int(input())
s = set()
for _ in range(m):
    a = input().rstrip().split()

    if len(a) == 2:
        t = a[0][0]
        x = int(a[1])
        if t == "a":
            s.add(x)
        elif t == "r":
            s.discard(x)
        elif t == "c":
            print(1 if x in s else 0)
        elif t == "t":
            if x in s:
                s.discard(x)
            else: s.add(x)
    else:
        if a[0] == "all":
            s = set([i for i in range(1,21)])
        else:
            s = set()