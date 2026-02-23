import sys

input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

INF = float('inf')

# dp[city][visited]
# 현재 방문 도시가 visited 상태일 때, city 에서 나머지 도시를 전부 순회하고 원점으로 돌아가는 최소 비용
dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited):
    if visited == (1 << N) - 1:
        if matrix[now][0]:
            return matrix[now][0]
        else:
            return INF

    if dp[now][visited] != -1:
        return dp[now][visited]

    min_cost = INF

    for next_city in range(1, N):
        if not (visited & (1 << next_city)) and matrix[now][next_city] != 0:
            cost = matrix[now][next_city] + dfs(next_city, visited | (1 << next_city))
            min_cost = min(min_cost, cost)

    dp[now][visited] = min_cost
    return min_cost

print(dfs(0, 1))