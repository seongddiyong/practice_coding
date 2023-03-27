a = int(input())
b = int(input())

x = b%10                # 1의 자리
y = ((b%100)-x)/10      # 10의 자리
z = (b - (b%100))/100   # 100의 자리

print(round(a*x))
print(round(a*y))
print(round(a*z))
print(round(a*b))
