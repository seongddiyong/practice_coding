## 숫자 카드 게임

# 공백으로 구분하여 입력받기
n,m = map(int, input().split())

result = 0
for i in range(n) :
    # 데이터 입력 받는다.
    data = list(map(int,input().split()))
    # 가장 작은 수 찾기
    min_value = min(data)
    # 가장 작은 수끼리 비교해서 큰 수를 찾기
    result = max(result,min_value)
print(result)
