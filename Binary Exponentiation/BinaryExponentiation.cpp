// https://cp-algorithms.com/algebra/binary-exp.html
// this code was creatad with the intention of 
// understand how the Binary Exponentiation works

#include <bits/stdc++.h>
using namespace std;

// function that gives a^b in O(log n)
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

// x^n % m

/*long long binpow(long long a, long long b, long long m) {
    a %= m;
    long long res = 1;
    while (b > 0) {
        if (b & 1)
            res = res * a % m;
        a = a * a % m;
        b >>= 1;
    }
    return res;
}*/