from sys import stdin
input = stdin.readline

x,y,w,h = map(int, input().split())
answer = [x,(w-x),y,(h-y)]
print(min(answer))