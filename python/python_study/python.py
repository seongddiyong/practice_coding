## 수의 지수 표현
a = 1e9
b = 75.25e1
c = 3954e-3

print("수의 지수 표현")
print(a,b,c)

## 반올림 함수
a = round(12.456,2)     #12.46

print("반올림 함수 - round")
print(a)

## 리스트 컴프리핸션

# 0 부터 19까지 수 중 홀수만 포함하는 리스트 생성
array = [i for i in range(20) if i%2==1]
print("리스트 컴프리핸션")
print(array)

# 초기화는?
## 기존에 있는 리스트
print("리스트 초기화")
### 아예 비워버리기
array = []
print(array)

## 2차원 리스트 초기화
n = 3
m = 3
array = [[0] * m for _ in range(n)]
print("2차원 리스트 초기화")
print(array)
a = array.count()