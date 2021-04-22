// https://codeforces.com/problemset/problem/154/B
#include <bits/stdc++.h>
using namespace std;

#define N 100000

int lp[N+1];
vector<int> pr;

int on_off[N+1];
int outro[N+1];

int n;

void solve(){

	char signal;
	int collider;

	scanf(" %c %d", &signal, &collider);

	if (signal == '+'){

		if (on_off[collider] == 1){

			printf("Already on");
			return;
		}	

		int i = collider;
		while (lp[i] != 1){

			if (outro[lp[i]] != 0){

				printf("Conflict with %d\n", outro[lp[i]]);
				return;
			}
			i = i / lp[i];
		}

		printf("Success");
		on_off[collider] = 1;

		i = collider;
		while (lp[i] != 1){

			outro[lp[i]] = collider;
			i = i / lp[i];
		}
	}

	else {

		if (on_off[collider] == 1)	{

			printf("Success"); 
			on_off[collider] = 0;

			int i = collider;
			while (lp[i] != 1){
				outro[lp[i]] = 0;
				i = i / lp[i];
			}
		}
		else printf("Already off");
	}
	printf("\n");
}

int main(){

	int m;
	scanf("%d %d", &n, &m);

	lp[1] = lp[0] = 1;
	for (int i = 2; i <= N; i++){

		if (lp[i] == 0){
			lp[i] = i;
			pr.push_back(i);
		}

		for (int j = 0; j < (int)pr.size() and pr[j] <= lp[i] and i*pr[j] <= N; ++j)
			lp[i * pr[j]] = pr[j];
	}

	while (m--)	solve();

	return 0;
}
