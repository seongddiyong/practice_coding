# N, M, K 를 공백으로 구분해서 받기
n, m, k = map(int, input().split())

# n개의 수를 공백으로 구분하여 입력받기
data = list(map(int,input().split()))

data.sort() # 수 정렬
first = data[n-1]   # 가장 큰 수
second = data[n-2]  # 두번째 큰 수

result = 0

# 큰 수가 나올 수 있는 횟수
## 반복적인 것을 세어낼 때
count = int(m/(k+1))*k
## 반복이 끝나고 나머지를 세어낼 때
count += m % (k+1)

# 큰 수가 반복된 횟수만큼 큰 수를 곱해준다.
result += count * first
# 위의 반복 횟수를 전체 횟수에서 빼주고 두번째 큰 수를 곱해준다.
result += (m-count) * second

print(result)
    

