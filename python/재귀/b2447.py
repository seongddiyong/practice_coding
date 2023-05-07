import sys

def append_star(n):
    if n == 1:
        return['*']
    
    stars = append_star(n//3)
    temp = []

    for i in stars:
        temp.append(i*3)
    for i in stars:
        temp.append(i + ' '*(n//3) + i)
    for i in stars:
        temp.append(i*3)
    
    return temp

n = int(sys.stdin.readline().strip())
print('\n'.join(append_star(n)))