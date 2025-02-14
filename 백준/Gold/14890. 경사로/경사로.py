import sys

input = sys.stdin.readline

n, l = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


# 가로 왼->오
ans = 0
for i in range(n):
	# 경사로 분석
	data = []
	now = board[i][0]
	count = 1
	start = 0
	for j in range(1, n):
		if board[i][j-1] == board[i][j]:
			count += 1
		else:
			data.append((now, count, start, j-1))
			now = board[i][j]
			count = 1
			start = j
	data.append((now, count, start, n-1))
	# 경사로를 못 놓는 상황 case 1 : 높이 차이가 1이 아닐 때
	flag = True
	for i in range(1, len(data)):
		if abs(data[i][0] - data[i-1][0]) != 1:
			flag = False
			break
	if not flag:
		continue
	# 경사로를 못 놓는 상황 case 2 : 지형에 따라
	if len(data) <= 1:
		ans += 1
		continue
	else:
		possible = True
		for i in range(len(data)):
			if i == 0:
				if data[i][0] < data[i+1][0]:
					if data[i][1] < l:
						possible = False
						break
				else:
					if data[i+1][1] < l:
						possible = False
						break
			elif i == len(data)-1:
				if data[i][0] > data[i-1][0]:
					if data[i-1][1] < l:
						possible = False
						break
				else:
					if data[i][1] < l:
						possible = False
						break
			else:
				if data[i-1][0] > data[i][0]:
					if data[i-1][0] == data[i+1][0]:
						if data[i][1] < 2*l:
							possible = False
							break
					else:
						if data[i][1] < l:
							possible = False
							break
		if possible:
			ans += 1

# 세로 위->아래
for i in range(n):
	data = []
	now = board[0][i]
	count = 1
	start = 0
	for j in range(1, n):
		if board[j-1][i] == board[j][i]:
			count += 1
		else:
			data.append((now, count, start, j-1))
			now = board[j][i]
			count = 1
			start = j
	data.append((now, count, start, n-1))
	# 경사로를 못 놓는 상황 case 1 : 높이 차이가 1이 아닐 때
	flag = True
	for i in range(1, len(data)):
		if abs(data[i][0] - data[i-1][0]) != 1:
			flag = False
			break
	if not flag:
		continue
	# 경사로를 못 놓는 상황 case 2 : 지형에 따라
	if len(data) <= 1:
		ans += 1
		continue
	else:
		possible = True
		for i in range(len(data)):
			if i == 0:
				if data[i][0] < data[i+1][0]:
					if data[i][1] < l:
						possible = False
						break
				else:
					if data[i+1][1] < l:
						possible = False
						break
			elif i == len(data)-1:
				if data[i][0] > data[i-1][0]:
					if data[i-1][1] < l:
						possible = False
						break
				else:
					if data[i][1] < l:
						possible = False
						break
			else:
				if data[i-1][0] > data[i][0]:
					if data[i-1][0] == data[i+1][0]:
						if data[i][1] < 2*l:
							possible = False
							break
					else:
						if data[i][1] < l:
							possible = False
							break
		if possible:
			ans += 1
print(ans)