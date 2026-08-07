
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;

    vector<int> arr(n);
    for(int i=0;i<n;++i){
        cin >> arr[i];
    }

    vector<int> dp(n);
    dp[0] = 1;
    for(int i=1;i<n;++i){
        if(arr[i]>arr[i-1]) dp[i] = dp[i-1] + 1;
        else dp[i] = 1;
    }

    cout << *max_element(dp.begin(),dp.end());
    
    return 0;
}