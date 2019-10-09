// 2520 is the smallest number that can be divided by each of the numbers from 1
// to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the
// numbers from 1 to 20?

#include <stdio.h>

// Any number which is multiple of {1,...,20} must also be multiple of each
// number out of {1,...,10}. Therefore each number must be a multiple of 2520.
int main() {
  int ans = 2520;
  while (1) {
    int i = 11;
    int isAns = 1;

    // Check if the number is a multiple of each number out of {11,...,20}
    for (i = 20; i > 10; i--) {
      if (ans % i != 0) {
        isAns = 0;
        break;
      }
    }

    if (isAns) break;
    ans += 2520;
  }

  printf("The smallest positive multiple is %d\n", ans);
}