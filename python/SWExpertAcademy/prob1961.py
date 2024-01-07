T = int(input())
for t in range(1,T+1):
    n = int(input())
    sq = [list(map(int, input().split())) for _ in range(n)]
    dict = {i:[] for i in range(1,n+1)}
    for i in range(3):
        nextSquare = []
        for j in range(n):
            nxt = []
            for k in range(n):
                nxt.append(sq[k][j])
            nxt = nxt[::-1]
            nextSquare.append(nxt)
            temp = ""
            for k in nxt:
                temp += str(k)
            dict[j+1].append(temp)
        sq = nextSquare.copy()
    print(f"#{t}")
    for i in dict:
        for j in dict[i]:
            print(j, end=" ")
        print("")