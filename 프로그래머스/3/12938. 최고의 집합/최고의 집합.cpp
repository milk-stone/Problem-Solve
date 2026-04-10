#include <bits/stdc++.h>

using namespace std;

vector<int> solution(int n, int s) {
    if (s < n) {
        return {-1};
    } else if (s == n) {
        vector<int> answer(s, 1);
        return answer;
    }
    
    
    vector<int> answer;
    
    int base = s / n;
    int r = s % n;
    
    for (int i = 0; i < n; i++) {
        if (r > 0) {
            r--;
            answer.push_back(base + 1);
        } else {
            answer.push_back(base);
        }
    }
    
    sort(answer.begin(), answer.end());
    return answer;
}