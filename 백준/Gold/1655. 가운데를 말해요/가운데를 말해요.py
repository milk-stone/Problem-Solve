import heapq
import sys
import copy

input = sys.stdin.readline

N = int(input())
left = [] # Max Heap
right = [] # Min Heap

heapq.heappush(right, int(input()))
print(right[0])

sizeL = len(left)
sizeR = len(right)

for _ in range(1, N):
    target = int(input())
    if len(left) > len(right): # right에 추가해야함 (추가하면 짝수)
        if target < -left[0]:
            move = heapq.heappop(left)
            heapq.heappush(right, -move)
            heapq.heappush(left, -target)
        else:
            heapq.heappush(right, target)
        sizeR += 1
        print(-left[0])
    elif len(left) == len(right): # 둘 중 선택 (추가하면 홀수)
        if target < -left[0]:
            heapq.heappush(left, -target)
            print(-left[0])
        else:
            heapq.heappush(right, target)
            print(right[0])
    else: # left에 추가해야함 (추가하면 짝수)
        if target > right[0]:
            move = heapq.heappop(right)
            heapq.heappush(left, -move)
            heapq.heappush(right, target)
        else:
            heapq.heappush(left, -target)
        sizeL += 1
        print(-left[0])
