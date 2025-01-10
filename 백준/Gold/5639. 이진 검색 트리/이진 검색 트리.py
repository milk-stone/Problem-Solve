import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline


def make_tree(l):
    if len(l) == 0:
        return

    parent = l[0]
    left = True
    rightIndex = 1
    for i in range(1, len(l)):
        if l[i] > parent:
            left = False
        if not left:
            rightIndex = i
            break
    make_tree(l[1:rightIndex])
    make_tree(l[rightIndex:])
    print(parent)
    return


nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break

make_tree(nodes)