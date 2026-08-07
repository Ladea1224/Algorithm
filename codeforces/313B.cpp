
#include <bits/stdc++.h>
using namespace std;

int main(){
    ios_base::sync_with_stdio(false); 
    cin.tie(NULL);

    string s;
    cin >> s;

    int n = s.length();
    vector<int> dp(n);

    for(int i=1;i<n;++i){
        dp[i] = dp[i-1];
        if(s[i-1] == s[i]) ++dp[i]; 
    }

    int m;
    cin >> m;
    while(m--){
        int a,b;
        cin >> a >> b;
        --a; --b;
        cout << dp[b] - dp[a] << '\n';
    }



    return 0;
}

// (참고) 인덱스 혼동? -> 1-based 로 변경하는 방식

/*
#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string input;
    cin >> input;

    // 문자열을 1-based로 변경
    string s = " " + input;
    int n = input.length();

    // P[i] : A[1]부터 A[i]까지의 누적 합 (1-based)
    vector<int> P(n, 0);
    for (int i = 1; i < n; ++i) {
        int a_i = (s[i] == s[i + 1]) ? 1 : 0;
        P[i] = P[i - 1] + a_i;
    }

    int m;
    cin >> m;
    while (m--) {
        int l, r;
        cin >> l >> r;
        
        // 구간 [l, r-1] 의 합 = P[r-1] - P[l-1]
        cout << P[r - 1] - P[l - 1] << '\n';
    }

    return 0;
}
*/