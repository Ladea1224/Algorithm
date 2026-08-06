
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int MAX = 1000001;
    vector<int> dp(MAX);
    dp[2020] = 1;
    dp[2021] = 1;

    for(int i= 2020;i<MAX;++i){
        if(dp[i]){
            if(i+2020<MAX) dp[i+2020] = 1;
            if(i+2021<MAX) dp[i+2021] = 1;
        }
    }

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        if(dp[n]) cout << "YES\n";
        else cout << "NO\n";
    }

    return 0;
}