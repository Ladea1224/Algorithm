
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int n;
    cin >> n;
    vector<int> vec(n);
    for(auto &x : vec) cin >> x;

    vector<int> table(n,1);

    for(int i = 1; i < n; ++i){
        if(vec[i-1] <= vec[i]) table[i] = table[i-1] + 1;
    }

    cout << *max_element(table.begin(),table.end());

    return 0;
}