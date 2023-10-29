import sys
input = sys.stdin.readline
n = int(input())
f = int(input())
n = (n//100)*100
for i in range(100):
    if (n+i)%f == 0:
        answer = str(i)
        break
print(answer if len(answer)==2 else '0'+answer)