## 1번 코드는 블로그에서 가져옴. 몇 배는 빠르다.
### set함수를 써서 O(1)의 속도로 다룬다. (for 제외)
import sys
input = sys.stdin.readline
n = int(input())
arr = set(map(int,input().split()))
m = int(input())
m_arr= list(map(int,input().split()))



for i in range(m):
    if m_arr[i] in arr : 
        print(1,end=' ')
    else : print(0,end=' ')


## 2번 코드는 이분법을 사용한 코드이다.

# from sys import stdin
# input = stdin.readline

# n = int(input())
# n_num = sorted(list(map(int, input().split())))
# m = int(input())
# m_num = list(map(int, input().split()))

# for i in m_num:
#     start = 0
#     end = n-1
#     exist = 0
#     while start <= end:
#         mid = (start+end)//2
#         if n_num[mid] == i:
#             exist = 1
#             break
#         elif n_num[mid] > i:
#             end = mid-1
#         else:
#             start = mid+1
#     print(exist, end = ' ')