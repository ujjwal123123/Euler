/*
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
*/

#include <stdio.h>

int collatzLen(long long, int);

// I had to use long long for number and i, otherwise I was getting segmentation
// fault
int main() {
  int maxlen = 0;
  long long number = 0;
  int len = 0;

  long long i;
  for (i = 1000000; i > 1; i--) {
    len = collatzLen(i, 1);
    if (len > maxlen) {
      maxlen = len;
      number = i;
    }
  }
  printf("%lld is the number which produces sequence of maximum length %d\n",
         number, maxlen);
}

// Return length of collatz sequence
int collatzLen(long long n, int length) {
  if (n == 1) {
    return length;
  }
  // even
  else if (n % 2 == 0) {
    return collatzLen(n / 2, length + 1);
  }
  // odd
  else {
    return collatzLen(3 * n + 1, length + 1);
  }
}
