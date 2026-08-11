
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n,m;
    cin >> n >> m;
    vector<int> a(n);
    for(auto& x : a) cin >> x;


    set<int> s;
    vector<int> dp(n);

    dp[n-1] = 1;
    s.insert(a[n-1]);

    for(int i = n-2;i>=0; --i){
        int v = a[i];
        if(s.find(v) == s.end()){
            s.insert(v);
            dp[i] = dp[i+1] + 1;
        } else{
            dp[i] = dp[i+1];
        }
    }

    while(m--){
        int x;
        cin >> x;
        cout << dp[x-1] << '\n';
    }

    return 0;
}
