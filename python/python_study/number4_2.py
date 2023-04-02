n,k = map(int,input().split())
result = 0

# n 이 k보다 크거나 같을 때 : 나눌 수 있다
while n >= k :
    # 이 중 나누어 떨어지지 않으면 1씩 빼서 맞춘다.
    while n % k != 0:
        n -= 1
        result += 1
    # k 로 나누어 떨어질 때는 나눈다.
    n //= k
    result += 1

# n이 k보다 작을 때는 1이 될 때까지 빼준다.
while n > 1:
    n -= 1
    result += 1

print(result)