t = int(input())
for i in range(t):
    num, s = input().split()
    text = ''
    for i in s:
        text += int(num) * i
    print(text)

## 내가 작성한 코드 - 위 코드가 훨씬 간단한 코드이다.
# from sys import stdin
# t = int(input())
# for i in range(t):
#     list = []
#     r,s = stdin.readline().rstrip().split()
#     s_len = len(s)
#     for j in range(s_len):
#         print(s[j]*int(r),end="")
#     print("\n", end="")