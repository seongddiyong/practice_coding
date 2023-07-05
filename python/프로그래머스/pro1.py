def solution(babbling):
    answer = 0
    for i in babbling:
        i = i.replace('aya', '.')
        i = i.replace('ye', '.')
        i = i.replace('woo', '.')
        i = i.replace('ma', '.')
        i = i.strip('.')
        if len(i) == 0:
            answer += 1
    return answer


def solution2(babbling):
    c = 0
    for b in babbling:
        for w in [ "aya", "ye", "woo", "ma" ]:
            temp = w*2
            if w * 2 not in b:
                b = b.replace(w, ' ')
        if len(b.strip()) == 0:
            c += 1
    return c

babbling = ["aya", "yee", "u", "maa", "wyeoo"]
print(solution2(babbling))
