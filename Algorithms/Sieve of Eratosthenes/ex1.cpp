// https://codeforces.com/contest/26/problem/A
#include <bits/stdc++.h>
using namespace std;

#define N 3000
int natural_numbers[N+1];


void solve (int n) {

	int count = 0;

	for (int i = 2; i <= n; i++) {
		if (natural_numbers[i] == 0 and 2*i <= n)
			for (int j = 2*i; j <= n; j += i)
				natural_numbers[j] += 1;		
	
		if (natural_numbers[i] == 2) count++;
	}
	
	printf("%d", count);
}


int main(){

	int n;
	scanf("%d", &n);

	solve(n);

	return 0;
}