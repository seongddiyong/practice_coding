import time
from sys import stdin

a = stdin.readline()

one_start_time = time.time()
data1 = list(map(int, stdin.readline().split()))
print(data1)
one_end_time = time.time()
print(one_end_time-one_start_time)

start_time = time.time()
data2 = list(map(int, input().split()))
print(data2)
end_time = time.time()
print(end_time-start_time)