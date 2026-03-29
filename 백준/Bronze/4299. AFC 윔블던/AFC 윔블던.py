apb, amb = map(int, input().split())

a = (apb + amb) // 2
if a * 2 != apb + amb or a < 0:
    print(-1)
    exit(0)
b = (apb - amb) // 2
if b * 2 != apb - amb or b < 0:
    print(-1)
    exit(0)
if a > b:
    print(a, b, sep=" ")
else:
    print(b, a, sep=" ")