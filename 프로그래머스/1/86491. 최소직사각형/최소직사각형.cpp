#include <bits/stdc++.h>

using namespace std;

int solution(vector<vector<int>> sizes) {
    int N, M;
    N = sizes.size();
    
    int ver, hor;
    ver = -1;
    hor = -1;
    
    for (int i = 0; i < N; i++) {
        int less = min(sizes[i][0], sizes[i][1]);
        int great = max(sizes[i][0], sizes[i][1]);
        
        
        if (less > ver) {
            ver = less;
        }
        if (great > hor) {
            hor = great;
        }
    }
    
    int answer = ver * hor;
    
    
    return answer;
}