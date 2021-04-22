// https://codeforces.com/problemset/problem/17/A
#include <bits/stdc++.h>
using namespace std;

#define N 1000

int naturals[N+1];
vector<int> pr;

void solve(int k){

	for (int i = 2; i < 1*pr.size() and k; i++){

		int tst = pr[i] - 1;

		int x = 0;
		while (x + 1 < i and pr[x] + pr[x+1] < tst){
			x++;
		}

		if (pr[x] + pr[x+1] == tst){
			k--;
		} 
	}

	if (k) printf("NO");
	else  printf("YES");
}


int main(){

	int n;
	scanf("%d", &n);

	int k;
	scanf("%d", &k);

	for (int i = 2; i <= n; i++){

		if (naturals[i] == 0){
			
			pr.push_back(i);

			if (i * i <= n){

				for (int j = i * i; j <= n; j += i){
					naturals[j] = 1;
				}
			}
			
		}
	}

	solve(k);

	return 0;
}