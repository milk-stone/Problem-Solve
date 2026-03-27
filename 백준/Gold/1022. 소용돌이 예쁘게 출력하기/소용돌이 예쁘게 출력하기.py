import sys

input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

def get_value(r, c):
    m = max(abs(r), abs(c))
    max_val = (2 * m + 1) ** 2

    if r == m: # 아랫 변
        return max_val - (m - c)
    elif r == -m: # 윗 변
        return max_val - 4 * m - (c + m)
    elif c == -m: # 왼쪽 변
        return max_val - 2 * m - (m - r)
    elif c == m: # 오른쪽 변
        return max_val - 6 * m - (r + m)

b = []
maxValue = -1
for y in range(r1, r2 + 1):
    line = []
    for x in range(c1, c2 + 1):
        now = get_value(y, x)
        line.append(now)
        if now > maxValue:
            maxValue = now
    b.append(line)

maxLength = len(str(maxValue))

for line in b:
    for item in line:
        print(f"{item:{maxLength}}", end=" ")
    print()