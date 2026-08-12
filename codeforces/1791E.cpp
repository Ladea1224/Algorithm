
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
   
    int t;
    cin >> t;
    while(t--){
        int n;
        cin >> n;
        int sign = 1;
        bool isZero = false;
        vector<int> a(n);
        for(auto& x : a) {
            cin >> x;
            if(x<0) sign *= -1;
            if(x==0) isZero = true;
        }

        long long result = 0;
        int minAbs = 1e9;
        for(auto& x : a){
            result += abs(x);
            minAbs = min(minAbs,abs(x));
        }

        if(sign > 0 || isZero){
            cout << result << "\n";
            continue;
        } else{
            cout << result - minAbs*2 << "\n";
            continue;
        }
    }
    return 0;
}
