class SegmentTree:
    def __init__(self, data, size):
        def init(start, end, index):
            if start == end:
                self.ids[index] = data[start]
                return self.ids[index]

            mid = (start + end) // 2
            self.ids[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
            return self.ids[index]

        self.ids = [0 for _ in range(size * 4)]
        init(0, size - 1, 1)

    def update(self, start, end, index, what, value):
        if what < start or what > end:
            return

        self.ids[index] += value
        if start == end:
            return
        mid = (start + end) // 2
        self.update(start, mid, index * 2, what, value)
        self.update(mid + 1, end, index * 2 + 1, what, value)

    def intervalSum(self, start, end, index, target_left, target_right):
        if target_left > end or target_right < start:
            return 0

        if target_left <= start and end <= target_right:
            return self.ids[index]

        mid = (start + end) // 2
        return self.intervalSum(start, mid, index * 2, target_left, target_right) + self.intervalSum(mid + 1, end, index * 2 + 1, target_left, target_right)


import sys


input = sys.stdin.readline

N, K, M = map(int, input().split())
arr = [int(input()) for _ in range(N)]

st = SegmentTree(arr, N)
for _ in range(K + M):
    a, b, c = map(int, input().split())
    if a == 1:
        diff = c - arr[b-1]
        st.update(0, N - 1, 1, b - 1, diff)
        arr[b-1] = c
    elif a == 2:
        print(st.intervalSum(0, N - 1, 1, b - 1, c - 1))

