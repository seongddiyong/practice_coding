from collections import deque
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities)*5
    cache = deque()
    cities = cities[::-1]
    answer = 0
    while cities:
        city = cities.pop().upper()
        if len(cache) != cacheSize:
            if city not in cache:
                cache.append(city)
                answer += 5
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1
        else:
            if city not in cache:
                cache.popleft()
                cache.append(city)
                answer += 5
            else:
                cache.remove(city)
                cache.append(city)
                answer += 1
    return answer