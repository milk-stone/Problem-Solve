import sys

input = sys.stdin.readline
w1 = input().strip()
w2 = input().strip()
matrix = [["" for _ in range(len(w2)+1)] for _ in range(len(w1)+1)]
for i in range(1, len(w1)+1):
	for j in range(1, len(w2)+1):
		if w1[i-1] == w2[j-1]:
			matrix[i][j] = matrix[i-1][j-1] + w1[i-1]
		else:
			if len(matrix[i-1][j]) > len(matrix[i][j-1]):
				matrix[i][j] = matrix[i-1][j]
			else:
				matrix[i][j] = matrix[i][j-1]

print(len(matrix[-1][-1]))
if len(matrix[-1][-1]) != 0:
	print(''.join(matrix[-1][-1]))