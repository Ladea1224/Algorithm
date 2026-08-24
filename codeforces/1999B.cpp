#include <bits/stdc++.h>
using namespace std;

bool game(int x1,int x2,int y1,int y2){
    if(x1 >= y1 && x2 >= y2){
        if(x1==y1 && x2==y2) return false;
        return true;
    }
    return false;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;
    while(t--){
        int a1,a2,b1,b2, result=0;
        cin >> a1 >> a2 >> b1 >> b2;
        if(game(a1,a2,b1,b2)) ++result;
        if(game(a1,a2,b2,b1)) ++result;
        cout << result*2 << '\n';
    }

    return 0;
}
