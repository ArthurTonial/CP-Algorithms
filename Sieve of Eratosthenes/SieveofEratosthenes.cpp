// https://cp-algorithms.com/algebra/sieve-of-eratosthenes.html
// this code was creator with the intention of 
// understand how the Sieve of Eratosthenes works

#include <bits/stdc++.h>
using namespace std;

#define N 100
int natural_numbers[N+1];

// function that make a vector with the primes 
// between 1 and n (parameter)
vector<int> primes(long long n) {

	vector<int> pr;

	for (long long i = 2; i <= n; i++) {

		if (natural_numbers[i] == 0 and i * i <= n) {	
			
			pr.push_back(i);

			for (long long j = i * i; j <= n; j += i) {
				natural_numbers[j] = 1;
			}
		}
	}
	return pr;
}

/*
// says if the index i is prime (true or false)
int n;
vector<bool> is_prime(n+1, true);
is_prime[0] = is_prime[1] = false;
for (int i = 2; i * i <= n; i++) {
    if (is_prime[i] && (long long)i * i <= n) {
        for (int j = i * i; j <= n; j += i)
            is_prime[j] = false;
    }
}
*/