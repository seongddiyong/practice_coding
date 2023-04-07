a = list(map(int, input().split()))

indexOfMax = a.index(max(a))
if max(a) >= (sum(a) - max(a)):     # 더 작은 두 변의 합
    a[indexOfMax] =  (sum(a)-max(a)-1)
print(sum(a))