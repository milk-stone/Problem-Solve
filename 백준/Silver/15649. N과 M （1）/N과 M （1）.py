import sys

def back_tracking(count, idx):
    if count==m:
        print(' '.join(list(map(str, answer))))
    for i in range(1, n+1):
        if not visited[i]:
            answer.append(i)
            visited[i]=True
            back_tracking(count+1,i+1)
            answer.pop()
            visited[i]=False

n, m = list(map(int, sys.stdin.readline().split()))
visited=[False for _ in range(n+1)]
answer=[]
back_tracking(0,1)