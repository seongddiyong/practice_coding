def solution(id_list, report, k):
    cnt_report = [0 for _ in range(len(id_list))]   # 신고 당한 횟수
    reporting = [[] for _ in range(len(id_list))]   # 신고한 사람들
    black = []
    answer = cnt_report.copy()
    for i in report:
        ring, red = i.split()
        idxOfId = id_list.index(ring)
        if red not in reporting[idxOfId]:
            reporting[idxOfId].append(red)
            cnt_report[id_list.index(red)] += 1
    for i, cnt in enumerate(cnt_report):
        if cnt >= k:
            black.append(id_list[i])
    for i,user in enumerate(reporting):
        for b in black:
            if b in user:
                answer[i] += 1
    return answer

def solution2(id_list, report, k):
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}

    for r in set(report):
        reports[r.split()[1]] += 1

    for r in set(report):
        if reports[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1

    return answer

id = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id,report,k))