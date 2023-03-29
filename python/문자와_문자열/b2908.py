num1, num2 = input().split()
num1 = int(num1[::-1])  # [::-1] : 역순
num2 = int(num2[::-1])

print(num1) if num1 > num2 else print(num2)


## 아래는 내 코드, [::-1]이 있으면 훨씬 간편한 것 같다.
## 역순 : [::-1]
# a,b = input().split()
# a = [a[i] for i in range(3)]
# b = [b[i] for i in range(3)]
# a.reverse()
# b.reverse()
# a_re = 0
# b_re = 0
# for i in range(3):
#     a_re += int(a[i])*pow(10,2-i)
#     b_re += int(b[i])*pow(10,2-i)
# print(max(a_re,b_re))