def solution(history, option, keyword):
    answer = []
    
    # 1. 검색 옵션에 따라서 일치하는 검색 기록을 찾습니다.
    for i in range(len(history)):
        is_matched = True
        for j in range(len(option)):
            if option[j][1] == "T":
                if option[j][0] == "W":  # 완전 일치
                    if keyword not in history[i].split():  # 단어 일치 여부 확인
                        is_matched = False
                        break
                # 다른 옵션이 있다면 추가 구현이 필요합니다.
        if is_matched:
            answer.append(history[i])
    
    # 2. 찾은 검색 기록 중에서 검색 키워드와 일치하는 기록을 찾습니다.
    if keyword != "":
        filtered = []
        for i in range(len(answer)):
            if keyword in answer[i].split():
                filtered.append(answer[i])
        answer = filtered
    
    # 3. 일치하는 검색 기록을 answer 리스트에 추가하고, answer를 반환합니다.
    if len(answer) == 0:
        return ["empty"]
    else:
        return answer
