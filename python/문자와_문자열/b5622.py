s = input()
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0
for i in range(len(s)):
    for j in dial:
        if s[i] in j:
            result += dial.index(j)+3
print(result)