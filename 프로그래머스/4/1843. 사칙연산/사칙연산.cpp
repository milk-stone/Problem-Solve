#include<bits/stdc++.h>

using namespace std;

int solution(vector<string> arr)
{
    vector<int> nums = {};
    vector<string> operators = {};
    
    for (int i = 0; i < arr.size(); i++) {
        if (arr[i] == "-" or arr[i] == "+") {
            operators.push_back(arr[i]);
        }
        else {
            nums.push_back(stoi(arr[i]));
        }
    }
    
    int N = (int) nums.size();
    
    vector<vector<int>> max_dp(N, vector<int>(N));
    vector<vector<int>> min_dp(N, vector<int>(N));
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                max_dp[i][i] = nums[i];
                min_dp[i][i] = nums[i];
            } else {
                max_dp[i][j] = -100000000;
                min_dp[i][j] = 100000000;
            }
        }
    }
    
    for (int index = 1; index < N; index++) {
        for (int left = 0; left < N - index; left++) {
            int right = left + index;
            for (int mid = left; mid < right; mid++) {
                if (operators[mid] == "+") {
                    max_dp[left][right] = max(max_dp[left][right], max_dp[left][mid] + max_dp[mid + 1][right]);
                    min_dp[left][right] = min(min_dp[left][right], min_dp[left][mid] + min_dp[mid + 1][right]);
                } else if (operators[mid] == "-") {
                    max_dp[left][right] = max(max_dp[left][right], max_dp[left][mid] - min_dp[mid + 1][right]);
                    min_dp[left][right] = min(min_dp[left][right], min_dp[left][mid] - max_dp[mid + 1][right]);
                }
            }
        }
    }
    return max_dp[0][N - 1];
}