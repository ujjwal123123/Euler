/*
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
*/

#include <stdio.h>
char isPrime(int);

long long primes[2000] = {2, 3};
int len = 2;
long long sum = 5;

int main() {
  int i;
  for (i = 5; i < 2000000; i += 6) {
    if (isPrime(i)) sum += i;
    if (isPrime(i + 2)) sum += i + 2;
  }

  printf("The sum is %lld\n", sum);
}

char isPrime(int n) {
  int i;
  for (i = 0; primes[i] * primes[i] <= n; i++) {
    if (n % primes[i] == 0) return 0;
  }

  if (primes[len-1] < 2000) {
    primes[++len-1] = n;
  }

  return 1;
}