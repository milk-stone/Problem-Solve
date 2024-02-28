import sys

input = sys.stdin.readline


n = int(input())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
visited = [False for _ in range(n)]
team_1 = []
team_2 = []
minValue = 123456789


def calMinValue():
    team_1_score = 0
    for i in range(n//2):
        for j in range(i + 1, n//2):
            team_1_score += graph[team_1[i]][team_1[j]]
            team_1_score += graph[team_1[j]][team_1[i]]

    team_2_score = 0
    for i in range(n // 2):
        for j in range(i + 1, n // 2):
            team_2_score += graph[team_2[i]][team_2[j]]
            team_2_score += graph[team_2[j]][team_2[i]]

    return abs(team_1_score - team_2_score)

def setTeam(k, prev):
    global minValue
    if k == n//2:
        for i in range(n):
            if not visited[i]:
                team_2.append(i)
        minValue = min(calMinValue(), minValue)
        #print(team_1, team_2, minValue)
        team_2.clear()
        return
    for i in range(prev + 1, n):
        if not visited[i]:
            visited[i] = True
            team_1.append(i)
            setTeam(k+1, i)
            team_1.pop()
            visited[i] = False



setTeam(0, -1)
print(minValue)