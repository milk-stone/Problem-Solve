import sys

input = sys.stdin.readline

trie = {}


def insert(words):
    node = trie
    for word in words:
        if word not in node.keys():
            node[word] = {}
        node = node[word]


def printResult(node, depth):
    for k in sorted(node.keys()):
        print("--" * depth, end='')
        print(k)
        printResult(node[k], depth + 1)


N = int(input())

for _ in range(N):
    arr = input().split()
    insert(arr[1:])

printResult(trie, 0)


