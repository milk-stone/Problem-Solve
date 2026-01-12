import sys

input = sys.stdin.readline

N = int(input())

power_of_two = 1
while power_of_two < N:
    power_of_two *= 2

SIZE = power_of_two

tree = [0] * (2 * SIZE)
hashmap = {}
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(N):
    hashmap[B[i]] = i

def update(index):
    i = index + SIZE
    tree[i] = 1
    i //= 2
    while i > 0:
        tree[i] = tree[2 * i] + tree[2 * i + 1]
        i //= 2


def search(left, right):
    ret = 0
    l = left + SIZE
    r = right + SIZE
    while l <= r:
        if l % 2 == 1:
            ret += tree[l]
            l += 1
        if r % 2 == 0:
            ret += tree[r]
            r -= 1
        l //= 2
        r //= 2
    return ret


result = 0
for i in range(N):
    target = hashmap[A[i]]
    result += search(target, N)
    update(target)
print(result)