import sys

input = sys.stdin.readline

choices = input().strip()

dice = list(map(int, input().split()))
counts = [0 for _ in range(7)]
for i in dice:
    counts[i] += 1

maxScore = 0
if choices[0] == 'Y':
    maxScore = max(maxScore, (dice.count(1) + 2) * 1)
if choices[1] == 'Y':
    maxScore = max(maxScore, (dice.count(2) + 2) * 2)
if choices[2] == 'Y':
    maxScore = max(maxScore, (dice.count(3) + 2) * 3)
if choices[3] == 'Y':
    maxScore = max(maxScore, (dice.count(4) + 2) * 4)
if choices[4] == 'Y':
    maxScore = max(maxScore, (dice.count(5) + 2) * 5)
if choices[5] == 'Y':
    maxScore = max(maxScore, (dice.count(6) + 2) * 6)
if choices[6] == 'Y':
    ret = 0
    for i in range(1, 7):
        if counts[i] >= 2:
            ret = max(ret, 4 * i)
    maxScore = max(maxScore, ret)
if choices[7] == 'Y':
    if counts.count(0) == 5:
        components = []
        for i in range(1, 7):
            if counts[i] > 0:
                components.append(i)
        maxScore = max(maxScore, max(components) * 3 + min(components) * 2)
    elif counts.count(0) == 6:
        components = []
        for i in range(1, 7):
            if counts[i] > 0:
                components.append(i)
        if components[0] < 6:
            maxScore = max(maxScore, components[0] * 3 + 6 * 2)
        else:
            maxScore = max(maxScore, 5 * 2 + components[0] * 3)
if choices[8] == 'Y':
    all_zero_or_one = True
    for i in range(1, 7):
        if not 0 <= counts[i] <= 1:
            all_zero_or_one = False
    if all_zero_or_one and counts[6] == 0:
        maxScore = max(maxScore, 30)
if choices[9] == 'Y':
    all_zero_or_one = True
    for i in range(1, 7):
        if not 0 <= counts[i] <= 1:
            all_zero_or_one = False
    if all_zero_or_one and counts[1] == 0:
        maxScore = max(maxScore, 30)
if choices[10] == 'Y':
    for i in range(1, 7):
        if counts[i] == 3:
            maxScore = max(maxScore, 50)
            break
if choices[11] == 'Y':
    maxScore = max(maxScore, sum(dice) + 12)
print(maxScore)