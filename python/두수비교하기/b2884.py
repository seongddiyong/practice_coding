h,m = map(int, input().split())

if h>0:
    if (m-45) >= 0:
        print(h,m-45)
    else:
        print(h-1,m+60-45)
else:
    if (m-45) >= 0:
        print(h,m-45)
    else:
        print(23,m+60-45)