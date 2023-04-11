import sys

input = sys.stdin.readline

n = int(input())
chu = [0] + list(map(int, input().split()))
k = int(input())
things = list(map(int, input().split()))
dp = set()

for weight in chu:
    new = set({weight})
    for num in dp:
        new.add(abs(num-weight))
        new.add(num+weight)
    dp = dp.union(new)

for gem in things:
    print("Y" if gem in dp else "N", end = ' ')
print()