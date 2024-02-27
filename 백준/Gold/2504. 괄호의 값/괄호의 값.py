import sys

input = sys.stdin.readline

q = list(input().strip())
stack = []
ans = 0
value = 0


def isNumber(token):
    if token != '(' and token != ')' and token != '[' and token != ']':
        return True
    return False


for i in range(len(q)):
    value = 0
    if q[i] == '(' or q[i] == '[':
        stack.append(q[i])
        continue
    if q[i] == ')':
        while len(stack) != 0 and isNumber(stack[-1]):
            value += stack.pop()
        if len(stack) == 0:
            print(0)
            exit(0)
        if stack[-1] != '(':
            print(0)
            exit(0)
        temp = stack.pop()
        if value == 0:
            value += 2
        else:
            value *= 2
    if q[i] == ']':
        while len(stack) != 0 and isNumber(stack[-1]):
            value += stack.pop()
        if len(stack) == 0:
            print(0)
            exit(0)
        if stack[-1] != '[':
            print(0)
            exit(0)
        temp = stack.pop()
        if value == 0:
            value += 3
        else:
            value *= 3
    stack.append(value)

for i in stack:
    if not isNumber(i):
        print(0)
        exit(0)
    ans += i

print(ans)