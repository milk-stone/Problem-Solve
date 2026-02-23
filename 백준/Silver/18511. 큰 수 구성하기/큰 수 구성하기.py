import sys

input = sys.stdin.readline


N, K = map(int, input().split())
kList = list(map(int, input().split()))

minValue = 987654321
minGap = 987654321

def tracking(value):
    global minValue, minGap
    gap = N - value
    if gap < 0:
        return
    if gap < minGap:
        minGap = gap
        minValue = value

    value *= 10
    for i in kList:
        value += i
        tracking(value)
        value -= i

for i in kList:
    tracking(i)

print(minValue)