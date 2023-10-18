num = [True] * 10001
for i in range(1,10,2):
    num[i] = False
    print(i)
x = 10
while x < 10001:
    s = x
    temp = str(x)
    for i in range(len(temp)):
        s += int(temp[i])
    if s < 10001:
        num[s] = False
    x += 1
for i in range(19,len(num)):
    if num[i]:
        print(i)