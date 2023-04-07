a = []
b = []
for _ in range(3):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
for i in a:
    if a.count(i) == 1:
        x = i
        break
for j in b:
    if b.count(j) == 1:
        y = j
        break
print(x,y)