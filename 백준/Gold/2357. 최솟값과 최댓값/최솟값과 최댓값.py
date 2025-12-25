import sys

input = sys.stdin.readline

N, M = map(int, input().split())

"""
Segment Tree 구현 - Bottom-up Approach
: Update 기능이 필요하지 않기 때문에 Bottom-up Approach 적용
"""
# Step 0. 트리 배열 선언 - 길이: 2 * N
minTree = [0] * (2 * N)
maxTree = [0] * (2 * N)

# Step 1. 배열의 후반부에 목표 배열을 순차적으로 담기
index = N
for _ in range(N):
    inputValue = int(input())
    minTree[index] = inputValue
    maxTree[index] = inputValue
    index += 1

# Step 2. Bottom-up 방식으로 Segment Tree 구현
for i in range(2 * N - 2, 1, -2):
    minTree[i // 2] = min(minTree[i], minTree[i + 1])
    maxTree[i // 2] = max(maxTree[i], maxTree[i + 1])

# Step 3. minTree, maxTree 각각에 대한 탐색 함수 정의
def minSearch(a, b, tree): # [a, b] 구간
    l, r = a + N - 1, b + N - 1
    res = float('inf')

    while l <= r:
        if l % 2 == 1: # l 번째 노드가 <우측> 자식일 경우, 더 위로 전파하면 안됨.
            res = min(res, tree[l])
            l += 1
        if r % 2 == 0: # r 번째 노드가 <좌측> 자식일 경우, 더 위로 전파하면 안됨.
            res = min(res, tree[r])
            r -= 1
        l //= 2
        r //= 2

    return res


def maxSearch(a, b, tree):  # [a, b] 구간
    l, r = a + N - 1, b + N - 1
    res = -1

    while l <= r:
        if l % 2 == 1:  # l 번째 노드가 <우측> 자식일 경우, 더 위로 전파하면 안됨.
            res = max(res, tree[l])
            l += 1
        if r % 2 == 0:  # r 번째 노드가 <좌측> 자식일 경우, 더 위로 전파하면 안됨.
            res = max(res, tree[r])
            r -= 1
        l //= 2
        r //= 2

    return res

# Step 4. M 가지 query 상황에 대한 탐색
for _ in range(M):
    a, b = map(int, input().split())
    minValue = minSearch(a, b, minTree)
    maxValue = maxSearch(a, b, maxTree)
    print(f"{minValue} {maxValue}")
