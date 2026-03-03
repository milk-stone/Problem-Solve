import sys

input = sys.stdin.readline

N = int(input())
A, B, C, D = [], [], [], []

for _ in range(N):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB, CD = [], []

for l1, l2, res in [[A, B, AB], [C, D, CD]]:
    for i in range(N):
        for j in range(N):
            res.append(l1[i] + l2[j])

AB.sort()
CD.sort()

ans = 0
left = 0
right = N * N - 1
while left < N * N and right >= 0:
    cur = AB[left] + CD[right]
    if cur > 0:
        right -= 1
    elif cur == 0:
        ABcount = 1
        CDcount = 1
        i = left + 1
        while i < N * N and AB[i] == AB[left]:
            ABcount += 1
            i += 1

        i = right - 1
        while i >= 0 and CD[i] == CD[right]:
            CDcount += 1
            i -= 1

        left += ABcount
        right -= CDcount
        ans += ABcount * CDcount
    else:
        left += 1

print(ans)
