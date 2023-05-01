import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    stack = []
    # .만 있는 경우엔 stop
    if sentence == ".":
        break
    for i in sentence:
        # i가 괄호면 스택에 쌓는다.
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
    if len(stack) == 0:
        print("yes")
    else:
        print("no")