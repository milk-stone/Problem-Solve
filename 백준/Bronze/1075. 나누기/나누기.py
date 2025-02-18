import sys

input = sys.stdin.readline

n = int(input())
f = int(input())

a = (n // 100) * 100
for i in range(a, a + 100):
    if i % f == 0:
        temp = i % 100
        if temp < 10:
            print(0, temp, sep='')
        else:
            print(temp)
        break