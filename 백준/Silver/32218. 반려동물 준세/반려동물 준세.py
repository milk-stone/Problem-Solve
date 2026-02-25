import sys

input = sys.stdin.readline

N = int(input())
a = list(map(int, input().split()))

def cal_b(a):
    b = []
    for i in range(N):
        count = 0
        for j in range(i + 1, N):
            if a[i] < a[j]:
                count += 1
        b.append(count)
    return b

phase = 1
while True:
    b = cal_b(a)
    allSame = True
    for i in range(N):
        if a[i] != b[i]:
            allSame = False
            break
    if allSame: break
    phase += 1
    a = b

print(phase)