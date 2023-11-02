import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temp = list(map(int, input().split()))
for _ in range(k):
  start, end = map(int,input().split())
  print('{:.2f}'.format(sum(temp[start-1:end])/(end-start+1)))