#너의 평점은
from sys import stdin

grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

result = 0
cnt = 0
for i in range(20):
    a,b,c = stdin.readline().split()
    if c != 'P':
        cnt += float(b)
        result += float(b)*score[grade.index(c)]
    
print("{:.6f}".format(result/cnt))
