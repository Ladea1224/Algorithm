
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    vector<int> dp(100003);

    int n;
    cin >> n;    
    int max_num = 0;
    for(int i=0;i<n;++i){
        int t;
        cin >> t;
        if(max_num < t) max_num = t;
        dp[t]++;
    }

    for(int i = 1; i<100003; ++i){
        dp[i] += dp[i-1];
    }

    int q;
    cin >> q;
    while(q--){
        int m;
        cin >> m;
        if(m > max_num) cout << n << '\n';
        else cout << dp[m] << '\n';
    }


    return 0;
}