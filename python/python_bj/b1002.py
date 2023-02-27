# 터렛
from sys import stdin
import math

t = int(stdin.readline())
for i in range(t):
    x1,y1,r1,x2,y2,r2 = map(int, stdin.readline().split())

    distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))

    ## 원이 동심원일 때 혹은 일치
    if distance == 0 and r2 == r1 :
        print("-1")
    ## 원이 내접할 때 / 원이 외접할 때
    elif abs(r2-r1) == distance or (r2+r1) == distance :
        print("1")
    ## 원이 두 점에서 만날 때
    elif abs(r2-r1) < distance < (r2+r1)  :
        print("2")
    else :
        print("0")