#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int main(void)
{
    int L, N;
    cin >> L >> N;

    vector<string> v;
    string s;

    int index = N;
    while (index--)
    {
        cin >> s;
        v.push_back(s);
    }

    int K;
    cin >> K;

    int maxValue = 0;

    unordered_map<string, int> um;

    for (int i = 0; i < N; i++)
    {
        string target = v[i];
        for (int j = 0; j < target.length() - K + 1; j++)
        {
            string key = target.substr(j, K);

            um[key]++;

            maxValue = max(um[key], maxValue);
        }
    }
    cout << maxValue << "\n";
    return 0;
}