def solution(s):
    s = s.upper()
    if s.count('P') != s.count('Y'):
        return False
    else: return True