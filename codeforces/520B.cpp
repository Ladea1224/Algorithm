#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n,m;
    cin >> n >> m;
    if(n==m){
        cout << 0;
        return 0;
    }

    deque<int> deque = {n};
    vector<int> dp(20000);

    int x = 0;
    while(!deque.empty()){
        x = deque.front(); deque.pop_front();
        if(x-1 >= 1 && !dp[x-1]){
            dp[x-1] = dp[x] + 1;
            if(x-1 == m) break;
            deque.push_back(x-1);
        }
        if(x*2 < 20000 && !dp[x*2]){
            dp[x*2] = dp[x] + 1;
            if(x*2 == m) break;
            deque.push_back(x*2);
        }
    }

    cout << dp[m];

    return 0;
}
