
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,a,b,c;
    cin >> n >> a >> b >> c;

    set<int> s = {a,b,c};

    vector<int> dp(5000);
    for(auto x : s){
        dp[x] = 1;
    }

    for(int i = 0; i<n; ++i){
        if(dp[i]==0) continue;
        for(auto x : s){
            if(n < i+x) continue;
            dp[i+x] = max(dp[i+x],dp[i] + 1);
        }
    }

    cout << dp[n];


    return 0;
}
