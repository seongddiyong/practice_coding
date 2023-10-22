import math
def solution(fees, records):
    dict = {}
    cost = {}
    answer = []
    for i in records:
        time,number,io = i.split()
        hour, minute = time.split(':')
        time = int(hour)*60 + int(minute)
        if io == "IN":
            dict[number] = time
            if number not in cost:
                cost[number] = [0,0]
        else:
            dif = time - dict[number]
            cost[number][0] += dif
            del dict[number]
    for car_num, time in dict.items():
        dif = (23*60 + 59) - time
        cost[car_num][0] += dif
    for k,v in cost.items():
        if v[0] - fees[0] > 0:
            cost[k] = fees[1] + (math.ceil((v[0] - fees[0])/fees[2]))*fees[3]
        else:
            cost[k] = fees[1]
    answer = [i[1] for i in sorted(cost.items(), key = lambda x: x[0])]
    return answer