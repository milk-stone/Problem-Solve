import sys

input = sys.stdin.readline

N = int(input())
lt_zero = []
gt_one = []
zeroCount = 0
oneCount = 0
for _ in range(N):
    now = int(input())
    if now < 0:
        lt_zero.append(now)
    elif now == 0:
        zeroCount += 1
    elif now == 1:
        oneCount += 1
    else:
        gt_one.append(now)

lt_zero.sort()
gt_one.sort(reverse=True)

ans = oneCount

if len(lt_zero) > 0:
    if len(lt_zero) % 2:
        if zeroCount > 0:
            lt_zero.pop()
            zeroCount -= 1
        else:
            ans += lt_zero.pop()
    for i in range(1, len(lt_zero), 2):
        ans += lt_zero[i - 1] * lt_zero[i]

if len(gt_one) > 0:
    if len(gt_one) % 2:
        ans += gt_one.pop()
    for i in range(1, len(gt_one), 2):
        ans += gt_one[i - 1] * gt_one[i]

print(ans)
