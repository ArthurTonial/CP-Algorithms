// https://cp-algorithms.com/algebra/primality_tests.html

// ths code was created in the intention of 
// understand how the Trial division works

// Complexity: O(sqrt(N))

#include <bits/stdc++.h>
using namespace std;

// Trial division to verify if x is prime
bool isPrime(int x){

	// prevent checking all even numbers later
	if (x % 2) return false;

	for (int d = 3; d * d <= x; d += 2){
		if (x % d) return false;
	}
	return true;
}


// Trial division to make a vector with the factorization of x
vector<long long> factors(long long n) {

    vector<long long> f;

    for (long long d = 2; d * d <= n; d++) {

        while (n % d == 0) {
            f.push_back(d);
            n /= d;
        }
    }

    if (n > 1) f.push_back(n);
    return f;
}


// This factorization works with Sieve of Eratosthenes algorithm
vector<long long> primes; // filled in Sieve algorithm

vector<long long> factorsSieve(long long x){

	vector<long long> f;

	for (long long d : primes){
		if (d * d > x) break;
		while (x % d == 0){
			f.push_back(d);
			x /= d;
		}
	}
	if (x > 1) f.push_back(x);

	return f;
}