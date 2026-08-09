
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,k;
    cin >> n >> k;
    vector<int> coins(n);
    for(auto& x : coins) cin >> x;

    vector<vector<bool>> dp(k+1,vector<bool>(k+1));
    dp[0][0] = true;

    for(auto& a : coins){
        for(int i = k; i>=0; --i){
            for(int j = k; j>=0; --j){
                if(dp[i][j] && i+a<=k){
                    dp[i+a][j] = true;
                    dp[i+a][j+a] = true;
                } 
            }
        }
    }


    // for(auto& v : dp){
    //     for(const auto& x : v){
    //         cout << x << ' ';
    //     }
    //     cout << '\n';
    // }





    vector<int> answer;
    for(int i = 0; i<=k; ++i){
        if(dp[k][i]) answer.push_back(i);
    }
    sort(answer.begin(),answer.end());

    cout << answer.size() << '\n';
    for(auto x : answer) cout << x << ' ';


    return 0;
}
