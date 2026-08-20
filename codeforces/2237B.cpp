#include <bits/stdc++.h>
using namespace std;

int n;

int inv(vector<int>& v,vector<int>& v2){
    int count = 0;

    for(auto &x : v2){
        for(int i=0;i<v.size();++i){
            if(v[i] <= x){
                count += i;
                v.erase(v.begin()+i);
                break;
            }
        }
    }

    return count;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        bool impossible = false;
        cin >> n;
        vector<int> A0(n),A1(n);
        for(auto& x : A0) cin >> x;
        for(auto& x : A1) cin >> x;

        vector<int> sortedA0 = A0;
        sort(sortedA0.begin(),sortedA0.end());

        for(int i = 0; i<n; ++i){
            if(sortedA0[i] > A1[i]){
                impossible = true;
                break;
            }
        }

        if(impossible){
            cout << -1 << "\n";
            continue;
        }

        
        cout << inv(A0,A1) << "\n";


    }

    return 0;
}
