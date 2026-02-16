import sys

input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

power_of_two = 1
while power_of_two <= N:
    power_of_two *= 2

tree = [1_000_000_001] * (2 * power_of_two)
for i in range(N):
    tree[power_of_two + i] = arr[i]

for i in range(2 * power_of_two - 2, 0, -2):
    tree[i // 2] = min(tree[i], tree[i + 1])


def search(left, right):
    l = left + power_of_two
    r = right + power_of_two
    ans = 1_000_000_001
    while l <= r:
        if l % 2 == 1:
            ans = min(ans, tree[l])
            l += 1
        if r % 2 == 0:
            ans = min(ans, tree[r])
            r -= 1
        l //= 2
        r //= 2
    return ans

for i in range(N):
    if i - (L - 1) < 0:
        print(search(0, i), end=" ")
    else:
        print(search(i - L + 1, i), end=" ")
