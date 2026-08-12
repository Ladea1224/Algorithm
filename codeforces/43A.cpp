#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    map<string,int> scores;

    while(n--){
        string s;
        cin >> s;
        scores[s]++;
    }
    int maxi = 0;
    string answer = "";
    for(auto& [k,v] : scores){
        if(v > maxi){
            maxi = v;
            answer = k;
        }
    }

    cout << answer;

    return 0;
}
