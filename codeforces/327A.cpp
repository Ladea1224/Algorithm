
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> v(n+1);

    for(int i = 1;i<n+1;++i) cin >> v[i];

    vector<vector<int>> dp(n+1,vector<int>(n+1));
    
    int begin = count(v.begin()+1,v.end(),1);

    int answer = 0;

    for(int i = 1; i < n+1; ++i){
        for(int j = i; j< n+1; ++j){
            if(i==j){
                dp[i][i] = begin - v[i] + (1-v[i]);
                answer = max(answer,dp[i][i]);
            } else{
                dp[i][j] = dp[i][j-1] - v[j] + (1-v[j]);
                answer = max(answer,dp[i][j]);
            }
        }
    }

    cout << answer;

    return 0;
}
