import sys
input  = sys.stdin.readline
import re

p = re.compile('(100+1+|01)+')
for i in range(int(input())):
   s = input().strip()
   if p.fullmatch(s):
       print("YES")
   else:
       print("NO")

## 이 코드에 대해 import re 를 파악하지 못했음