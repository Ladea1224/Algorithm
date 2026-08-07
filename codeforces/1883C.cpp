
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t;
    cin >> t;

    auto check = [](const auto& arr,const auto& k){
        int p = 1e9;
        for(const auto& x : arr){
            if(x%k==0) return 0;
            p = min(p,k-(x%k));
        }
        return p;
    };

    auto check2 = [](const auto& arr){
        int even_count = 0;
        for(const auto& x : arr){
            if(x%4==0) return 0;
            if(x%2==0) ++even_count;
        }
        if(even_count>=2) return 0;
        if(even_count==1) return 1;
        else return 2;
    };

    while(t--){
        int n,k;
        cin >> n >> k;

        vector<int> arr(n);
        for(int i=0;i<n;++i) cin >> arr[i];
        
        if(k==4) cout << min(check(arr,k),check2(arr)) << '\n';
        else cout << check(arr,k) << '\n';
    }   

    return 0;
}
