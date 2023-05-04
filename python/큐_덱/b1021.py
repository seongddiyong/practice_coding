import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
num = deque([0 for _ in range(n)])
target = list(map(int, input().split()))
j = 1
for i in target:
    num[i-1] = j
    j+=1
search = 1
cnt = 0
while m > 0:
    idx = num.index(search)
    if idx <= int(len(num)//2):
        while True:
            if num[0] == search:
                num.popleft()
                break
            else:
                num.append(num.popleft())
                cnt += 1
    else:
        while True:
            if num[0] == search:
                num.popleft()
                break
            else:
                num.appendleft(num.pop())
                cnt += 1
    search += 1
    m -= 1
print(cnt)
