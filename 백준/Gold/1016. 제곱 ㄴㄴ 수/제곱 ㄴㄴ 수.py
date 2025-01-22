import sys
import math

input = sys.stdin.readline

a, b = map(int, input().split())

answer = b - a + 1

checkList = [False for _ in range(b - a + 1)]

for i in range(2, int(b ** 0.5) + 1):
    d_factor = i ** 2
    for j in range(math.ceil(a / d_factor) * d_factor, b + 1, d_factor):
        if not checkList[j - a]:
            checkList[j-a] = True
            answer -= 1


print(answer)
