## 거스름 돈 문제 (책)

n = 1260
coin_type = [500, 100, 50, 10]
answer = 0

for coin in coin_type:
    answer += n // coin # 최대한 거슬러 줄 수 있는 만큼
    n %= coin

print(answer)