// https://codeforces.com/contest/1512/problem/G
#include <bits/stdc++.h>
using namespace std;

#define N 10000000

long long somas[N+1];
long long dp[N+1];


void solve() {

	int c; 
	scanf("%d", &c);
	printf("%lld\n", dp[c]);
}


int main() {

	int t;
	scanf("%d", &t);

	memset(dp, -1, sizeof(dp));

	for (int i = 1; i <= N; i++) {
		for (int j = i; j <= N; j += i) {
			somas[j] += i;
		}
		if (somas[i] <= N && dp[somas[i]] == -1) 
			dp[somas[i]] = i;
	}
	
	while (t--){
		solve();
	}

	return 0;
}