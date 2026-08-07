
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> arr1(n+1);
    for(int i=1;i<n+1;++i){
        cin >> arr1[i];
    }   

    auto arr2 = arr1;
    sort(arr2.begin()+1,arr2.end());  // 1-based 주의

    auto buildDp = [&](const auto& arr){
        vector<long long> dp(n+1);
        dp[1] = arr[1];
        for(int i=2;i<n+1;++i){
            dp[i] = dp[i-1] + arr[i];
        }
        return dp;
    };

    vector<vector<long long>> dps = {buildDp(arr1),buildDp(arr2)};

    int m;
    cin >> m;
    while(m--){
        int q,a,b;
        cin >> q >> a >> b;
        cout << dps[q-1][b] - dps[q-1][a-1] << '\n';
    }

    return 0;
}
