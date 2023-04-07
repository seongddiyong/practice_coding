a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("Equilateral")
elif a+b+c != 180:
    print("Error")
elif a == b != c or b == c != a or a == c != b:
    print("Isosceles")
else:
    print("Scalene")