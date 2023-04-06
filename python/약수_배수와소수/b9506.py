import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == -1:
        break
    test = []
    for k in range(1,n):
        if n%k == 0:
            test.append(k)
    if sum(test) == n:
        print(n, " = ", " + ".join(str(i) for i in test), sep="")
    else:
        print(n, "is NOT perfect.")
