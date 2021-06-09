// https://cp-algorithms.com/algebra/primality_tests.html

// ths code was created in the intention of 
// understand how the Trial division works

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
vector<long long> factorization(long long x){

	vector<long long> fact;

	// it could be made in 'isPrime' too
	for (int d : {2,3,5}){ 
		while (x % d == 0){
			fact.push_back(d);
			n /= d;
		}
	}

	static array<int,8> increments = {4,2,4,2,4,6,2,6};
	int i = 0;
	for (long long d = 7; d * d <= x; d += increments[i++]){
		while (x % d == 0){
			fact.push_back(d);
			x /= d;
		}
		if (i == 8) i = 0;
	}
	if (x > 1) fact.push_back(x);

	return fact;
}


// This factorization works with Sieve of Eratosthenes algorithm
vector<long long> primes; // filled in Sieve algorithm

vector<long long> sieveFactorization(long long x){

	vector<long long> fact;

	for (long long d : primes){
		if (d * d > x) break;
		while (x % d == 0){
			fact.push_back(d);
			x /= d;
		}
	}
	if (x > 1) fact.push_back(x);

	return fact;
}