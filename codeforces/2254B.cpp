#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);



    int t;
    cin >> t;
    while(t--){
        int n;
        string s;
        cin >> n >> s;
        int r=0;
        for(int i=1; i<s.length()-1;++i){
            if(s[i-1] == s[i+1]){
                if(s[i-1] == s[i]){
                    continue;    
                } else{
                    r=2;
                }
            } else{
                if(s[i-1] == s[i] || s[i+1] == s[i]){
                    continue;
                } else{
                    r=max(r,1);
                }
            }
        }
        int cnt = 1;
        for(int i = 1; i<s.length(); ++i){
            if(s[i] != s[i-1]) ++cnt;
        }

        cout << cnt-r << "\n";
    }

    return 0;
}
