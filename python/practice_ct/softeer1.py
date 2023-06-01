from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
model = deque([])
stack = []

for _ in range(n):
	temp = []
	order = input().rstrip()
	# enqueue
	if order[0] == 'e':
		en = order.split(' ')
		# en[1] 이 알파벳
		model.append(en[1])
	else:
		if not model:
			print('*', end=' ')
			continue
		setting = list(set(model))
		for i in setting:
			temp.append(model.count(i))

		while True:
			if model.count(model[0]) == max(temp):
				a = model.popleft()
				print(a, end = ' ')
				while stack:
					model.appendleft(stack.pop())
				break
			stack.append(model.popleft())
			
			