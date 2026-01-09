import sys

input = sys.stdin.readline


def appendCandy(candy_rank, value):
    index = candy_rank + SIZE - 1
    tree[index] += value
    now = index // 2
    while now > 0:
        tree[now] = tree[now * 2] + tree[now * 2 + 1]
        now //= 2
    return


def searchCandy(targetIndex):
    now = 1
    while now < SIZE:
        if tree[now * 2] >= targetIndex:
            now = 2 * now
        else:
            targetIndex = targetIndex - tree[now * 2]
            now = 2 * now + 1
    result_candy_rank = now - SIZE + 1
    appendCandy(result_candy_rank, -1)
    return result_candy_rank


SIZE = 2 ** 20
tree = [0] * (2 * SIZE)

N = int(input())
for _ in range(N):
    l = list(map(int, input().split()))
    if l[0] == 1:
        print(searchCandy(l[1]))
    elif l[0] == 2:
        appendCandy(l[1], l[2])
