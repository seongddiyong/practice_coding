import sys
input = sys.stdin.readline

def gcd(x,y):
    if x < y:
        temp = x
        x = y
        y = temp
    while y != 0:
        r = x%y
        x = y
        y = r
    return x
        
n = int(input())    # 심어져 있는 가로수
a = int(input())    # 첫 가로수 위치
temp = []           # 가로수 사이 값을 입력할 리스트
for i in range(n-1):    # 가로수 간격 저장
    num = int(input())
    temp.append(num-a)
    a = num
for_gcd = temp[0]   # 처음 값을 할당하여 최대공약수 찾기
for j in range(1,len(temp)):
    for_gcd = gcd(for_gcd,temp[j])
result = 0
for z in temp:
    result += z//for_gcd-1
print(result)