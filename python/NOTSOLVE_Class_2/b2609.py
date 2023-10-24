def gcd(a,b):
    while b > 0:
        a,b = b,a%b
    print(a)
    return a

def lcm(a,b):
    g = gcd(a,b)
    print(int(a*b/g))

a,b = map(int,input().split())
lcm(a,b)