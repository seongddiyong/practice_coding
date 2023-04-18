import math

a,b = map(int, input().split())
x,y = map(int, input().split())

lcm = math.lcm(b,y)
top = a*(lcm//b) + x*(lcm//y)
gcd = math.gcd(lcm,top)
print(top//gcd, lcm//gcd)