#include <stdio.h>

int main() {
    int x = 1;
    int y = 2;

    x, y = y, x;

    printf("x is %d and y is %d\n", x, y);
}