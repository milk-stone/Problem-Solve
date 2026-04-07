#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> triangle) {
    int N = triangle.size();
    
    vector<vector<int>> dp(N, vector<int>(N));
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            dp[i][j] = 0;
        }
    }
    
    for (int i = 0; i < N; i++) {
        vector<int> layer = triangle[i];
        int size = layer.size();
        if (i == 0) {
            dp[i][0] = triangle[i][0];
            continue;
        }
        for (int j = 0; j < size; j++) {
            if (j == 0) {
                dp[i][j] = dp[i - 1][j] + triangle[i][j];
            } else if (j == size - 1) {
                dp[i][j] = dp[i - 1][j - 1] + triangle[i][j];
            } else {
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j];
            }
        }
    }
    
    int answer = -1;
    for (int i = 0; i < N; i++){
        if (dp[N - 1][i] > answer) {
            answer = dp[N - 1][i];
        }
    }
    return answer;
}