import sys

input = sys.stdin.readline


factor = 1_000_000_007
N, M, K = map(int, input().split())

mulTree = [0] * (2 * N)
index = N
for _ in range(N):
    mulTree[index] = int(input())
    index += 1

for i in range(2 * N - 2, 1, -2):
    mulTree[i // 2] = mulTree[i] * mulTree[i + 1] % factor

# print(f"[DEBUG] init - mulTree : {mulTree}")


# 함수 정의
def updateTree(b, c, tree):  # a == 1 일 때 실행
    target = b + N - 1
    tree[target] = c
    target //= 2
    while target > 0:
        tree[target] = tree[2 * target] * tree[2 * target + 1] % factor
        target //= 2

def search(a, b, tree):  # a == 2 일 때 실행
    l, r = a + N - 1, b + N - 1
    res = 1

    while l <= r:
        if l % 2 == 1:
            res *= tree[l]
            l += 1
        if r % 2 == 0:
            res *= tree[r]
            r -= 1
        l //= 2
        r //= 2
        res %= factor

    return res


# 추론

for _ in range(M + K):
    # print(f"[DEBUG] infer #{_} - mulTree : {mulTree}")
    a, b, c = map(int, input().split())
    if a == 1:
        updateTree(b, c, mulTree)
        continue
    if a == 2:
        print(search(b, c, mulTree))
        continue
