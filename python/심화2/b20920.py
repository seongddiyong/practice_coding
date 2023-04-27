# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다
from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
book = {}
for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word in book:
        book[word][0] += 1
    else:
        book[word] = [1, len(word), word]
answer = sorted(book.items(), key=lambda x: (-x[1][0],-x[1][1],x[1][2]))
for i in answer:
    print(i[0])