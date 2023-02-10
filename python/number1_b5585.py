

price = int(input())
answer = 0

result = 1000 - price
# 720
coin_type = [500, 100, 50, 10, 5, 1]
for cost in coin_type :
    answer += result // cost # 720 / 500 = 1
    result %= cost

print(answer)