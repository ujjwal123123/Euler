// Starting in the top left corner of a 2×2 grid, and only being able to move to
// the right and down, there are exactly 6 routes to the bottom right corner.

// How many such routes are there through a 20×20 grid?

#include <stdio.h>

unsigned long long int fact(int n) {
  if (n == 1 || n == 0)
    return 1;
  else
    return (n * fact(n - 1));
}

int main() {
  int n;
  scanf(" %d", &n);

  printf("%llu\n", fact(2 * n) / (fact(n) * fact(n)));
}