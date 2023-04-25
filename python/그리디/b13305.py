n = int(input())
distance = list(map(int,input().split()))
price = list(map(int,input().split()))

minPrice = price[0]
cost = 0
for i in range(n-1):
    if price[i] < minPrice:
        minPrice = price[i]
    cost += (minPrice * distance[i])
print(cost)