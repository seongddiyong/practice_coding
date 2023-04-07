while 1:
    a,b,c = map(int,input().split())
    if a == b == c == 0:
        break
    elif max(a,b,c) >= ((a+b+c)-max(a,b,c)):
        print("Invalid")
    elif a==b==c:
        print("Equilateral")
    elif a==b!=c or b==c!=a or a==c!=b:
        print("Isosceles")
    elif a != b != c:
        print("Scalene")