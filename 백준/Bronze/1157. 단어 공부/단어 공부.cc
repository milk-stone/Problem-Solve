#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    string s;

    cin >> s;

    unordered_map<char, int> map;
    for (int i = 0; i < s.length(); i++)
    {
        map[tolower(s[i])]++;
    }

    int maxUsedCount = -1;
    char maxUsedChar;
    bool duplicated = false;
    for (auto [key, value] : map)
    {
        if (value > maxUsedCount)
        {
            maxUsedChar = key;
            maxUsedCount = value;
            duplicated = false;
        }
        else if (value == maxUsedCount)
        {
            duplicated = true;
        }
    }

    if (duplicated)
    {
        cout << "?" << "\n";
    }
    else
    {
        char output = toupper(maxUsedChar);
        cout << output << "\n";
    }

    return 0;
}