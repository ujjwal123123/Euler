// A palindromic number reads the same both ways. The largest palindrome made
// from the product of two 2-digit numbers is 9009 = 91 × 99.

// Find the largest palindrome made from the product of two 3-digit numbers.

#include <stdio.h>

int isPalindrome(int n);

// At least one of i and j must be the multiple of 11 because
// a*e5 + b*e4 + c*e3 + c*e2 + b*e1 + a == 11*[9091a + 91b + 100c]
int main() {
  int largestPalindrome = 0;
  int i, j;
  int product;
  for (i = 100; i < 1000; i++) {
    // j must be the multiple of 11
    for (j = 110; j < 1000; j += 11) {
      product = i * j;
      if (product > largestPalindrome)
        if (isPalindrome(product)) largestPalindrome = product;
    }
  }

  printf("The largest palindrome is %d\n", largestPalindrome);
}

int isPalindrome(int n) {
  int reversed = 0;
  int original = n;

  // Find reverse of the number
  while (n != 0) {
    reversed = reversed * 10 + n % 10;
    n /= 10;
  }

  return (reversed == original);
}