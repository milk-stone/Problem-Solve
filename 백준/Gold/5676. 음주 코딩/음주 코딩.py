class SegmentTree:
    def __init__(self, data, size):
        def init(start, end, index):
            if start == end:
                if data[start] < 0:
                    self.ids[index] = -1
                elif data[start] == 0:
                    self.ids[index] = 0
                else:
                    self.ids[index] = 1
                return self.ids[index]

            mid = (start + end) // 2
            self.ids[index] = init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)
            return self.ids[index]

        self.ids = [0 for _ in range(size * 4)]
        init(0, size - 1, 1)

    def swimup(self, index):

        return

    def update(self, start, end, index, what, value):
        if what < start or what > end:
            return
        if self.ids[index] == 0:
            self.ids[index] += value
        else:
            self.ids[index] *= value
        if start == end:
            temp = index
            while temp // 2 > 0:
                if temp % 2 == 0:
                    self.ids[temp // 2] = self.ids[temp] * self.ids[temp + 1]
                else:
                    self.ids[temp // 2] = self.ids[temp - 1] * self.ids[temp]
                temp = temp // 2
            return
        mid = (start + end) // 2
        self.update(start, mid, index * 2, what, value)
        self.update(mid + 1, end, index * 2 + 1, what, value)

    def intervalMulti(self, start, end, index, target_left, target_right):
        if target_left > end or target_right < start:
            return 1

        if target_left <= start and end <= target_right:
            return self.ids[index]

        mid = (start + end) // 2
        return self.intervalMulti(start, mid, index * 2, target_left, target_right) * self.intervalMulti(mid + 1, end, index * 2 + 1, target_left, target_right)


if __name__ == '__main__':
    import sys
    input = sys.stdin.readline

    while True:
        try:
            N, K = map(int, input().split())
            data = list(map(int, input().split()))
            size = len(data)
            st = SegmentTree(data, size)
            for _ in range(K):
                cmd, a, b = input().split()
                a, b = int(a), int(b)
                if cmd == 'C':
                    if b == 0:
                        st.update(0, size - 1, 1, a - 1, 0)
                        data[a-1] = 0
                    elif b > 0:
                        if data[a-1] < 0:
                            st.update(0, size - 1, 1, a - 1, -1)
                            data[a - 1] = 1
                        else:
                            st.update(0, size - 1, 1, a - 1, 1)
                            data[a-1] = 1
                    else:
                        if data[a-1] < 0:
                            st.update(0, size - 1, 1, a - 1, 1)
                            data[a - 1] = -1
                        else:
                            st.update(0, size - 1, 1, a - 1, -1)
                            data[a-1] = -1

                elif cmd == 'P':
                    res = st.intervalMulti(0, size - 1, 1, a - 1, b - 1)
                    if res > 0:
                        print("+", end='')
                    elif res == 0:
                        print("0", end='')
                    else:
                        print("-", end='')
                # print(st.ids)
                # print(data)
            print()
        except Exception:
            break