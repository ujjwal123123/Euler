// Starting with the number 1 and moving to the right in a clockwise direction a
// 5 by 5 spiral is formed as follows:

// 21 22 23 24 25
// 20  7  8  9 10
// 19  6  1  2 11
// 18  5  4  3 12
// 17 16 15 14 13

// It can be verified that the sum of the numbers on the diagonals is 101.

// What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral
// formed in the same way?

#include <stdio.h>

int main() {
  int answer = 1;
  int dimension = 0;
  scanf(" %d", &dimension);

  int layers = dimension / 2;

  // The sequence we get is
  //             1
  //    3  5  7  9   +2 in every term
  //   13 17 21 25   +4 in every term
  //   31 37 43 49   +6 in every term

  int add1 = 1;
  int add2 = 2;
  for (int i = 0; i < layers; i++) {
    for (int j = 0; j < 4; j++) {
      add1 += add2;
      answer += add1;
    }
    add2 += 2;
  }

  printf("The answer is %d\n", answer);
}

// Alternate way to do this is to use (as per Euler) is
// First I noted that for an n by n grid, and n being odd, the number in the top
// right corner is n2. A little mathematical analysis told me that the other
// corners are given by: n2-n+1, n2-2n+2, and n2-3n+3. Adding these together
// gives the quadratic, 4n2-6n+6. Then all I had to do was create a loop from 3
// to 1001 in steps of 2 and find the running total (starting from 1) of the
// quadratic.