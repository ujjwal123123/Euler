#include <stdio.h>

int multiple();

int main() {
    int mul3 = multiple(3, 999);

    int mul5 = multiple(5, 999);

    int mul15 = multiple(15, 999);

    printf("%d\n", mul3 + mul5 - mul15);

    return 0;

}

int multiple(int number, int limit) {
    int n = 999/number;

    return ( number * n * (n + 1) ) / 2; 
}