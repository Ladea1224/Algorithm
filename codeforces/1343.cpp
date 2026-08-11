
#include <bits/stdc++.h>
using namespace std;


long long run(vector<int>& v){
    long long sum = 0;

    int sign = v[0]>0 ? 1 : -1; 
    int maxi = v[0];

    for(int i = 1; i<v.size(); ++i){
        if(v[i]*sign < 0){
            sum += maxi;
            sign = v[i]>0 ? 1 : -1;
            maxi = v[i];
        } else{
            maxi = max(maxi,v[i]);
        }
    }

    sum += maxi;

    return sum;
}

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        vector<int> v(n);
        for(auto& x : v) cin >> x;

        cout << run(v) << '\n';
    }

    return 0;
}
