from sys import stdin
n,b = map(int, stdin.readline().rstrip().split())

temp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
li = []
while True:
    li.append(temp[n%b])
    n //= b
    if n//b == 0:
        a = n%b
        break
li.append(temp[a])
for i in li:
    print(i, end="")
