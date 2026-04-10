#include <string>
#include <vector>
#include <unordered_map>
#include <queue>

using namespace std;

int solution(string begin, string target, vector<string> words) {
    unordered_map<string, bool> used;
    
    int word_size = words[0].length();
    
    bool inWords = false;
    for (int i = 0; i < words.size(); i++) {
        if (words[i] == begin) {
            used[words[i]] = true;
        } else {
            used[words[i]] = false;
        }
        if (words[i] == target) {
            inWords = true;
            break;
        }
    }
    
    if (!inWords) {
        return 0;
    }
    
    queue<pair<string, int>> q;
    q.push({begin, 0});
    
    string now, nextWord;
    int diff_count = 0;
    while (!q.empty()) {
        auto[now, count] = q.front(); q.pop();
        if (now == target) {
            return count;
        }
        
        for (int i = 0; i < words.size(); i++) {
            nextWord = words[i];
            diff_count = 0;
            for (int j = 0; j < word_size; j++){
                if (now[j] != nextWord[j]) {
                    diff_count++;
                    if (diff_count > 1) {
                        break;
                    }
                }
            }
            if (diff_count > 1) continue;
            if (used[nextWord]) continue;
            
            used[nextWord] = true;
            q.push({nextWord, count + 1});
        }
    }
    
    return 0;
}