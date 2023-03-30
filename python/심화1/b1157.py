from sys import stdin
word = list(stdin.readline().rstrip())
word = [word[i].upper() for i in range(len(word))]
compare = list(set(word))
temp = [word.count(i) for i in compare]

if temp.count(max(temp)) > 1:
    print("?")
else:
    result = compare[temp.index(max(temp))]
    print(result)