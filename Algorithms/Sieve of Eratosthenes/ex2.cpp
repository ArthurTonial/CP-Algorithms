// https://codeforces.com/contest/776/problem/B
#include <bits/stdc++.h>
using namespace std;

#define N 100000
int naturals[N+1];

void solve(int n) {

	if (n < 3) printf("1\n");
	else printf("2\n");

	n += 1;

	for (int i = 2; i <= n; i++) {

		if (naturals[i] == 0 and  1ll * i * i <= n) {

			for (int j = i * i; j <= n; j += i) {
				if (naturals[j] == 0) naturals[j] = 1;
			}
		}
	}

	for (int i = 2; i <= n - 1; i++)
		printf("%d ", naturals[i] + 1);
	printf("%d", naturals[n] + 1);
}


int main() {

	int n;

	scanf("%lld", &n);

	solve(n);

	return 0;
}