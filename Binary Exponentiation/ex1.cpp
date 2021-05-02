// https://codeforces.com/problemset/problem/630/I
#include <bits/stdc++.h>
using namespace std;


long long binpow(long long a, long long b){

    long long res = 1;

    while (b > 0) {
        if (b & 1) // bitwise and
            res = res * a;
        a = a * a;
        b >>= 1; // bitwise right shift
    }
    return res;
}

void solve(){
	int n, p;
	scanf("%d",&n);

	p = 2*n - 2;

	long long ans = 0;
	for (int i = 0; i <= p - n - 2; i++){
		ans += 4* binpow(3, 2) * binpow(4, p - n - 2);
	}
	ans += 2 * 4 * 3 * binpow(4, p - n - 1);

	// poderia ser:
	// ans = 2*4*3*binpow(4, n-3) + 4*3*3*(n-3)*binpow(4,n-4)

	printf("%lld", ans);
}

int main(){

	solve();

	return 0;	
}