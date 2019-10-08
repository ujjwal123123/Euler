// The prime factors of 13195 are 5, 7, 13 and 29.

// What is the largest prime factor of the number 600851475143 ?

#include <math.h>
#include <stdio.h>

int isPrime(int);

int main() {
  unsigned long num;
  scanf(" %lu", &num);

  unsigned long largestPrimeFactor = 0;

  unsigned long i;
  for (i = 2; i <= sqrt(num); i++)
    if (num % i == 0) {
      if (isPrime(i)) {
        largestPrimeFactor = i;
      }
      // There can only be at most one prime factor of n which is greater than
      // sqrt(n)
      if (isPrime(num / i)) {
        largestPrimeFactor = num / i;
        // break if the only prime factor greater than sqrt(n) is found
        break;
      }
    }

  printf("%lu is the largest prime factor of %lu\n", largestPrimeFactor, num);
}

int isPrime(int n) {
  if (n <= 3)
    return n > 1;
  else if (n % 2 == 0 || n % 3 == 0)
    return 0;

  int i;
  for (i = 5; i * i <= n; i += 6)
    if (n % i == 0 || n % (i + 2) == 0) return 0;

  return 1;
}