
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int t;
    cin >> t;

    while(t--){
        int one = 0, two = 0;
        int n;
        cin >> n;

        while(n--){
            int p;
            cin >> p;
            if(p==1) ++one;
            else ++two;
        }

        if(one%2 == 1) cout << "NO\n";
        else if(one==0 && two%2 ==1) cout << "NO\n";
        else cout << "YES\n";
    }





    return 0;
}