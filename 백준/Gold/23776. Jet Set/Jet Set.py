import sys

input = sys.stdin.readline

N = int(input())
visited = [False for _ in range(360 * 2)]
last = (int(input().split()[1]) + 180) % 360
first = last

def fill(f, t):
    for i in range(f, t):
        visited[i] = True

def doit(cur, last):
    mini = min(cur, last)
    maxi = max(cur, last)
    diff = maxi - mini

    if diff == 0:
        return
    # if diff % 180 == 0: # diff == 180 이랑 똑같은 효과를 낼 듯
    if diff == 180:
        print("yes")
        exit(0)
    if diff < 180:
        fill(mini * 2, maxi * 2 + 1)
    else:
        fill(0, mini * 2 + 1)
        fill(maxi * 2, 360 * 2)

for i in range(1, N):
    cur = (int(input().split()[1]) + 180) % 360
    doit(cur, last)
    last = cur
doit(first, last)

for i in range(0, 720):
    if not visited[i]:
        i = (i / 2) - 180
        # print(type(i))
        print("no %s" % (i))
        exit(0)
print("yes")