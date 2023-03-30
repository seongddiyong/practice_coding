res = list(map(int,input().split()))
ans = [1,1,2,2,2,8]
a = []
for i in range(len(res)):
    print(ans[i]-res[i],end=' ')
