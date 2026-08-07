
#include <bits/stdc++.h>
using namespace std;
int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    int m;
    cin >> m;
    vector<int> men(m);
    for(int i=0;i<m;++i){
        cin >> men[i];
    }

    int w;
    cin >> w;
    vector<int> women(w);
    for(int i=0;i<w;++i){
        cin >> women[i];
    }

    sort(men.begin(),men.end());
    sort(women.begin(),women.end());

    int mp=0, wp=0, count=0;

    while(mp<m && wp<w){
        int mv = men[mp];
        int wv = women[wp];
        if( abs(mv-wv) <= 1 ){
            ++count; ++mp; ++wp;
        }
        else if(mv < wv) ++mp;
        else if(wv < mv) ++wp;
    }

    cout << count;


    return 0;
}