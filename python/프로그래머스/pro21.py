def solution(n, words):
    li = [words[0]]
    cnt1 = 2
    cnt2 = 1
    for i,j in enumerate(words[1:]):
        if j not in li and li[-1][-1] == j[0]:
            li.append(j)
            cnt1 += 1
            if cnt1 > n:
                cnt1 = 1
                cnt2 += 1
        else:
            return [cnt1,cnt2]
    return [0,0]