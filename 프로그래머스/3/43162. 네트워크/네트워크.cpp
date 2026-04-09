#include <string>
#include <vector>

using namespace std;

void dfs(int n, int start, vector<bool>& visited, vector<vector<int>>& graph) {
    for (int i = 0; i < graph[start].size(); i++) {
        int nextNode = graph[start][i];
        if (!visited[nextNode]) {
            visited[nextNode] = true;
            dfs(n, nextNode, visited, graph);
        }
    }
    return;
}

int solution(int n, vector<vector<int>> computers) {
    vector<vector<int>> graph(n);
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i != j && computers[i][j] == 1) {
                graph[i].push_back(j);
                graph[j].push_back(i);
            }
        }
    }
    
    vector<bool> visited(n, false);
    
    int answer = 0;
    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            answer++;
            visited[i] = true;
            dfs(n, i, visited, graph);
        }
    }
    
    return answer;
}