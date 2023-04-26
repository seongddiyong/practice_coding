# num = [0,1,2,3,4,5,6,6,7,8,9,9]
num = [0 for _ in range(0,10)]
n = input()
n = [int(i) for i in n]
for i in n:
    if i == 6 or i == 9:
        if num[6] == num[9]:
            num[i] += 1
        elif num[6] > num[9]:
            num[9] += 1
        else:
            num[6] += 1
    else:
        num[i] += 1
print(max(num))