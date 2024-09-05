t = int(input())
for _ in range(t):
    a, string = input().split()
    for i in range(len(string)):
        for _ in range(int(a)):
            print(string[i], end="")
    print()