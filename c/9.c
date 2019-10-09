/*
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
*/

#include <stdio.h>

int main() {
  int i, j, k;

  for (i = 1; i <= 1000; i++) {
    for (j = i + 1; j <= 1000; j++) {
      k = 1000 - i - j;
      if (k > i && k > j)
        if (i * i + j * j == k * k) {
          printf("%d^2 + %d^2 = %d^2\n", i, j, k);
          printf("The product is %d\n", i * j * k);
        }
    }
  }
}
