#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    vector<int> v{1,2,3};
    do{
        for(int x : v) cout << x << ' ';
        cout << '\n';
    } while(next_permutation(v.begin(),v.end()));

    
    return 0;
}
