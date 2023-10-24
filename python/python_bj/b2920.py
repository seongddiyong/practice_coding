from sys import stdin
input = stdin.readline
t = list(map(int, input().split()))
st = t[1] - t[0]
if st > 0:
    answer = "ascending"
else:
    answer = "descending"
for i in range(2,8):
    if (t[i] - t[i-1]) != st:
        answer = "mixed"
print(answer)