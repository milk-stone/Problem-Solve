import sys

input = sys.stdin.readline

N, C = map(int, input().split())
houses = []
for _ in range(N):
    houses.append(int(input()))

houses.sort()

start = 1
end = houses[-1] - houses[0]


ans = -1
while start <= end:
    mid = (start + end) // 2
    count = 1
    last_installed = houses[0]

    for i in range(1, N):
        if houses[i] - last_installed >= mid:
            count += 1
            last_installed = houses[i]

    if count >= C:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)