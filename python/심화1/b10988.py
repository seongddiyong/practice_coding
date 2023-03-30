from sys import stdin
word = list(stdin.readline().rstrip())

if list(reversed(word)) == word:
    print(1)
else:
    print(0)

