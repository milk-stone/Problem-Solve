import sys

input = sys.stdin.readline

N = int(input())

sequence = []
for _ in range(N):
    sequence.append(int(input()))

curNum = 1
stack = []
index = 0

tracking = []
while curNum <= N:
    if curNum < sequence[index]:
        stack.append(curNum)
        tracking.append("+")
    elif curNum == sequence[index]:
        tracking.append("+")
        tracking.append("-")
        index += 1
        while stack and stack[-1] == sequence[index]:
            stack.pop()
            tracking.append("-")
            index += 1
    else:
        tracking.append("Wrong")
        break
    curNum += 1

while stack and stack[-1] == sequence[index]:
    tracking.append("-")
    stack.pop()
    index += 1

if stack:
    print("NO")
    exit(0)

for i in tracking:
    print(i)