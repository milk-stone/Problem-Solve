#include <iostream>
#include <vector>
#include <string>

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

    for (int i = 0; i < N; i++)
    {
        string target = v[i];
        for (int j = 0; j < target.length() - K + 1; j++)
        {
            string key = target.substr(j, K);

            int curSum = 0;

            for (int k = 0; k < N; k++)
            {
                string now = v[k];
                for (int l = 0; l < now.length() - K + 1; l++)
                {
                    if (key == now.substr(l, K))
                    {
                        curSum += 1;
                    }
                }
            }

            maxValue = max(curSum, maxValue);
        }
    }
    cout << maxValue << "\n";
    return 0;
}