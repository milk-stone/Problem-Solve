import sys

input = sys.stdin.readline

N, M = map(int, input().split())

wordDict = {}

memo = []
for _ in range(N):
    word = input().strip()

    size = len(word)
    if size < M:
        continue

    if word not in wordDict.keys():
        wordDict[word] = 1
    else:
        wordDict[word] += 1

for word in wordDict.keys():
    memo.append([wordDict[word], len(word), word])

memo.sort(key=lambda x: (-x[0], -x[1], x[2]))

for count, length, word in memo:
    print(word)
