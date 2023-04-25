n = int(input())
time = sorted(list(map(int,input().split())))
temp = [time[0]]
for i in range(1,len(time)):
    temp.append(temp[i-1]+time[i])
print(sum(temp))