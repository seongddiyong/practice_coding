from collections import deque

def sol(s):
        stack = []
        for i in s:
            if len(stack) == 0: stack.append(i)
            else:
                if i == ")" and stack[-1] == "(":   stack.pop()
                elif i == "]" and stack[-1] == "[":   stack.pop()
                elif i == "}" and stack[-1] == "{":   stack.pop()
                else: stack.append(i)
        return 1 if len(stack) == 0 else 0
        
def solution(s):
    answer = 0
    s = deque(s)
    for i in range(len(s)):
        if sol(s):  answer +=1
        s.rotate(-1)
    return answer