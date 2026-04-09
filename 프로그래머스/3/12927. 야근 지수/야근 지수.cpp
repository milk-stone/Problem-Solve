#include <string>
#include <vector>
#include <iostream>
#include <queue>

using namespace std;

long long solution(int N, vector<int> works) {
    long long sumValue = 0;
    
    int W = works.size();
    int total = 0;
    priority_queue<int> pq;
    
    for (int i = 0; i < W; i++) {
        pq.push(works[i]);
        total += works[i];
    }
    
    if (total <= N) {
        return 0;
    }
    
    int now;
    while (!pq.empty()) {
        if (N <= 0) {
            break;
        }
        
        now = pq.top(); pq.pop();
        if (now - 1 > 0) {
            pq.push(now - 1);
        }
        N--;
    }
    
    long long answer = 0;
    while (!pq.empty()) {
        answer += (pq.top() * pq.top());
        pq.pop();
    }
    
    
    return answer;
}