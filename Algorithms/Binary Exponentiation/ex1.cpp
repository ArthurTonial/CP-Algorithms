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
	int n;
	scanf("%d",&n);

	long long ans = 2*4*3*binpow(4, n-3) + 4*3*3*(n-3)*binpow(4, n-4);

	printf("%lld", ans);
}

int main(){

	solve();

	return 0;	
}