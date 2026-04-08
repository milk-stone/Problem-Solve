#include <bits/stdc++.h>

using namespace std;

struct minNode {
    int id;
    int value;
    
    bool const operator<(const minNode& a) const {
        return value > a.value;
    }
};

struct maxNode {
    int id;
    int value;
    
    bool const operator<(const maxNode& a) const {
        return value < a.value;
    }
};

vector<int> solution(vector<string> operations) {
    
    int id = 0;
    int size = (int) operations.size();
    char command;
    int value;
    
    unordered_map<int, bool> table;
    priority_queue<minNode> min_pq;
    priority_queue<maxNode> max_pq;
    
    for (int i = 0; i < size; i++) {
        stringstream ss(operations[i]);
        ss >> command >> value;
        
        if (command == 'D') {
            if (value == 1) { // 최댓값 삭제
                maxNode cur;
                while (!max_pq.empty()) {
                    cur = max_pq.top();
                    if (table[cur.id]) break;
                    max_pq.pop();
                }
                if (max_pq.empty()) continue;
                table[cur.id] = false;
                // cout << cur.value << "\n";
                max_pq.pop();
            } else if (value == -1) { // 최솟값 삭제
                minNode cur;
                while (!min_pq.empty()) {
                    cur = min_pq.top();
                    if (table[cur.id]) break;
                    min_pq.pop();
                }
                if (min_pq.empty()) continue;
                table[cur.id] = false;
                // cout << cur.value << "\n";
                min_pq.pop();
            }
        } else if (command == 'I') {
            table[id] = true;
            min_pq.push({id, value});
            max_pq.push({id, value});
            id++;
        }
    }
    
    vector<int> answer;
    
    maxNode trash1;
    while (!max_pq.empty()) {
        trash1 = max_pq.top();
        if (table[trash1.id]) break;
        max_pq.pop();
    }
    if (max_pq.empty()) {
        answer.push_back(0);
    } else {
        answer.push_back(max_pq.top().value);
    }
    
    minNode trash2;
    while (!min_pq.empty()) {
        trash2 = min_pq.top();
        if (table[trash2.id]) break;
        min_pq.pop();
    }
    if (min_pq.empty()) {
        answer.push_back(0);
    } else {
        answer.push_back(min_pq.top().value);
    }
    
    return answer;
}