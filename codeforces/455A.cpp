
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> cnt(100001);

    int maxi = 0;

    while(n--){
        int x;
        cin >> x;
        ++cnt[x];

        if(x>maxi) maxi = x;
    }

    vector<long long> dp(maxi+1);
    dp[1] = cnt[1];
    for(long long i = 2; i< maxi+1; ++i){
        dp[i] = max(dp[i-1],dp[i-2] + i*cnt[i]);
    }

    cout << dp[maxi];
    
    


    return 0;
}
