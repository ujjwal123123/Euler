// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
// that the 6th prime is 13.

// What is the 10 001st prime number?

#include <stdio.h>

int isPrime(int);

int primes[10011] = {2, 3};
int len = 2;

int main() {
  int i = 5;
  while (len <= 10001) {
    if (isPrime(i)) primes[++len - 1] = i;

    if (isPrime(i + 2)) primes[++len - 1] = i + 2;

    i += 6;
  }

  printf("100001st prime number is %d\n", primes[10000]);
}

int isPrime(int n) {
  int isPrime = 1;
  int j;
  for (j = 0; primes[j] * primes[j] <= n; j++) {
    if (n % primes[j] == 0) {
      isPrime = 0;
    }
  }

  return isPrime;
}