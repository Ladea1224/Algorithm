#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int n,k;
        string s;
        cin >> n >> k >> s;

        int cnt=0;
        for(int i=0; i<=k-1;++i){
            if(s[i] == 'W') ++cnt;
        }
        int p1=0, p2=k-1, result=cnt;

        while(p2 < n-1){
            if(s[p1] == 'W') --cnt;
            ++p1; ++p2;
            if(s[p2] == 'W') ++cnt;
            result = min(result,cnt);
        }
        cout << result << '\n';
    }

    return 0;
}
