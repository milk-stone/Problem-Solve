import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

s_arr = list(set(arr))

s_arr.sort()


table = {}
for i in range(len(s_arr)):
    table[s_arr[i]] = i

for i in arr:
    print(table[i], end=" ")
print()

