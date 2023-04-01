# 우선순위 큐 라이브러리를 활용한 힙 정렬 구현 예제
## 출처 :: 이 것이 코딩테스트다 - 나동빈

from sys import stdin
import heapq

input = stdin.readline

# min heap sort
def heapsort(iterable):
    h = []
    result = []
    
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i], end=" ")