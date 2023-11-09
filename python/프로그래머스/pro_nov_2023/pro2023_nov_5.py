def solution(record):
    dict = {}
    id_list = []
    order_list = []
    answer = []
    for i in record:
        if i[0] == "E":
            t, idx, name = i.split()
            dict[idx] = name
            id_list.append(idx)
            order_list.append("님이 들어왔습니다.")
        elif i[0] == "C":
            t, idx, name = i.split()
            dict[idx] = name
        if i[0] == "L":
            t, idx = i.split()
            id_list.append(idx)
            order_list.append("님이 나갔습니다.")
    for i in range(len(order_list)):
        answer.append(dict[id_list[i]]+order_list[i])
    return answer