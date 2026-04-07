#include <iostream>
#include <queue>

using namespace std;

struct Node
{
    long long num;
    long long abs_num;

    bool const operator<(const Node &a) const
    {
        if (abs_num == a.abs_num)
        {
            return num > a.num;
        }
        else
        {
            return abs_num > a.abs_num;
        }
    }
};

int main(void)
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;

    priority_queue<Node> pq;

    long long target;
    for (int i = 0; i < N; i++)
    {
        cin >> target;
        if (target == 0)
        {
            if (pq.size() == 0)
            {
                cout << 0 << "\n";
                continue;
            }
            long long ans = pq.top().num;
            cout << ans << "\n";
            pq.pop();
            continue;
        }
        pq.push({target, abs(target)});
    }

    return 0;
}