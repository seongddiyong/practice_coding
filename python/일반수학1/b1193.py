import sys
input = sys.stdin.readline

n = int(input())

line = 0
end = 0
while n > end:
    line += 1
    end += line

diff = end - n
if line%2 == 0:         # 짝수일 때
    top = line - diff   # 분자는 line - (끝) 수(end = line) - n(입력))
    bottom = diff + 1   # 분모
else:
    top = diff + 1
    bottom = line - diff

print(f"{top}/{bottom}")
