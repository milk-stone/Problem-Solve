import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().split())

jewels = []
for _ in range(N):
    m, v = map(int, input().split())
    jewels.append((m, v))

bags = []
for _ in range(K):
    bag = int(input())
    bags.append(bag)

jewels.sort()
bags.sort()

ans = 0
candidate_jewels = []
jewel_idx = 0

for bag in bags:
    while jewel_idx < N and jewels[jewel_idx][0] <= bag:
        heapq.heappush(candidate_jewels, -jewels[jewel_idx][1])  # 가치가 클 수록 우선순위 높음
        jewel_idx += 1
    if candidate_jewels:
        ans += -heapq.heappop(candidate_jewels)  # 가장 가치가 큰 값을 합산
print(ans)
