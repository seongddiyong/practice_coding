#include <iostream>
using namespace std;
int dp[5001];
// dp 문제
int main() {
    unsigned int N = 0;
    while(N < 2 || N > 5001){
        cin >> N;
    }
    dp[3] = dp[5] = 1;  // 최소 봉지 수가 1이다.
    for(int i=6; i<=N; i++) {
        if(dp[i-3]) dp[i] = dp[i-3] + 1;
        if(dp[i-5]) dp[i] = dp[i] ? min(dp[i], dp[i-5]+1) : dp[i-5]+1;
    }
    cout << N;
}