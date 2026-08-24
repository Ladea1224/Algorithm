#include <bits/stdc++.h>
using namespace std;

vector<int> v;
int n=5, k=3;

void print(vector<int>& v){
    for(int x : v) cout << x << ' ';
    cout << '\n';
}

void comb(int s, int cnt){
    if(cnt==k){
        print(v);
        return;
    }

    for(int i=s; i<=n ;++i){
        v.push_back(i);
        comb(i+1,cnt+1);
        v.pop_back();
    }

}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    comb(1,0);
    return 0;
}
