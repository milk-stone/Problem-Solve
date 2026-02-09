T = int(input())
for _ in range(T):
    N = int(input())
    members = []
    for __ in range(N):
        a, b = map(int, input().split())
        members.append((a, b))
    members.sort(key=lambda x:x[0])
    count = 1
    top = members[0]
    for i in range(N):
        if members[i][1] < top[1]:
            count += 1
            top = members[i]
    print(count)