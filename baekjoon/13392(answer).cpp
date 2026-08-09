
/*

// top-down

#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int INF = 1e9;

int N;
string nowNum, targetNum;
int dp[10001][10];

int solve(int idx, int rot) {

    // 모든 나사를 맞춘 경우
    if (idx == N)
        return 0;

    // 이미 계산한 상태
    if (dp[idx][rot] != -1)
        return dp[idx][rot];

    // 현재 보이는 숫자
    int cur = (nowNum[idx] - '0' + rot) % 10;

    // 왼쪽으로 몇 칸 돌려야 하는가
    int left = (targetNum[idx] - '0' - cur + 10) % 10;

    // 오른쪽으로 몇 칸 돌려야 하는가
    int right = (10 - left) % 10;

    // 왼쪽 선택
    int leftCost = left + solve(idx + 1, (rot + left) % 10);

    // 오른쪽 선택
    int rightCost = right + solve(idx + 1, rot);

    return dp[idx][rot] = min(leftCost, rightCost);
}

int main() {

    cin >> N;
    cin >> nowNum >> targetNum;

    memset(dp, -1, sizeof(dp));

    cout << solve(0, 0);

    return 0;
}




//bottom-up

#include <iostream>
#include <algorithm>
using namespace std;

const int INF = 1e9;

int dp[10001][10];

int main() {

    int N;
    cin >> N;

    string now, target;
    cin >> now >> target;

    // 초기화
    for (int i = 0; i <= N; i++)
        for (int j = 0; j < 10; j++)
            dp[i][j] = INF;

    // 아직 아무것도 처리 안 함
    dp[0][0] = 0;

    for (int i = 0; i < N; i++) {

        for (int rot = 0; rot < 10; rot++) {

            if (dp[i][rot] == INF)
                continue;

            // 현재 보이는 숫자
            int cur = (now[i] - '0' + rot) % 10;

            // 왼쪽 회전 수(= 목표-현재)
            int left = (target[i] - '0' - cur + 10) % 10;

            // 오른쪽 회전 수(= 현재-목표)
            int right = (10 - left) % 10;

            // 왼쪽 선택
            dp[i + 1][(rot + left) % 10] =
                min(dp[i + 1][(rot + left) % 10],
                    dp[i][rot] + left);

            // 오른쪽 선택
            dp[i + 1][rot] =
                min(dp[i + 1][rot],
                    dp[i][rot] + right);
        }
    }

    int ans = INF;

    for (int rot = 0; rot < 10; rot++)
        ans = min(ans, dp[N][rot]);

    cout << ans;
}

*/