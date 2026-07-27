
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int a;
    cin >> a;
    
    int deno[] = {100,20,10,5,1};
    int cnt = 0;
    for(int i = 0; i < 5; ++i){
        while(deno[i]<=a){
            a -= deno[i];
            ++cnt;
        }
    }

    cout << cnt;
    return 0;
}