a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
if a1+a0/n0 <= c and c>=a0:
    print(1)
else:
    print(0)

## 두 코드의 차이도 모르겠고 문제도 모르겠습니다.
# a,b=map(int,input().split())
# c=int(input())
# n=int(input())
# r=1 if a*n+b<=c*n and c>=a else 0
# print(r)