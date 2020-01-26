// Let d(n) be defined as the sum of proper divisors of n (numbers less than n
// which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
// and b are an amicable pair and each of a and b are called amicable numbers.

// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
// 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
// 71 and 142; so d(284) = 220.

// Evaluate the sum of all the amicable numbers under 10000.

#include <assert.h>
#include <stdio.h>

int sumDivisors(int n);

int main() {
  assert(sumDivisors(1) == 1);
  assert(sumDivisors(5) == 1);
  assert(sumDivisors(4) == 3);

  int answer = 0;

  for (int i = 1; i <= 10000; i++) {
    assert(284 == sumDivisors(sumDivisors(284)));

    int sumdiv = sumDivisors(i);
    if (i < sumdiv) {
      if (i == sumDivisors(sumdiv)) {
        printf("%d and %d are amicable numbers\n", i, sumdiv);
        answer += i + sumdiv;
      }
    }
  }

  printf("The sum of the amicable numbers is %d\n", answer);
}

int sumDivisors(int n) {
  int sum = 1;

  int i = 0;
  for (i = 2; i * i < n; i++) {
    if (n % i == 0) {
      sum += i + n / i;
    }
  }

  if (n == i * i) {
    sum += i;
  }

  return sum;
}
