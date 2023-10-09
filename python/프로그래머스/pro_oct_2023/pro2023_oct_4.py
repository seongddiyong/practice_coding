def solution(id_pw, db):
    for i,j in db:
        if id_pw[0] == i:
            if id_pw[1] == j:
                return "login"
            else:
                return "wrong pw"
    return "fail"