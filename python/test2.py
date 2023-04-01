cur_y,cur_x = (0,0)

for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
    next_y = cur_y + dy
    next_x = cur_x + dx
    print("dy::",dy,"dx::",dx)
