
#include <bits/stdc++.h>
using namespace std;
//dp 전체를 저장하지 않아도 된다.
int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,k;
    cin >> n >> k;

    vector<int> v(n);
    for(auto &x : v) cin >> x;

    vector<int> dp(1);

    for(int i=0; i<k;++i) dp[0] += v[i];
    for(int i = 1; i < n-k+1; ++i){
        dp.push_back(dp[i-1] - v[i-1] + v[i+k-1]);
    }

    cout << min_element(dp.begin(),dp.end()) - dp.begin() + 1;
    return 0;
}