import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
X = int(input())

arr.sort()

count = 0

left = 0
right = N - 1

while left < right:
    if arr[left] + arr[right] > X:
        right -= 1
    elif arr[left] + arr[right] == X:
        count += 1
        left += 1
        right -= 1
    else:
        left += 1
print(count)