#include <stdio.h>

int main(void) {
    int sum = 0;

    int x = 1;
    int y = 2;

    while (y <= 4000000) {
        sum += y;

        int tempx = x;
        int tempy = y;

        x = tempx + 2*tempy;
        y = 2*tempx + 3*tempy;
    }

    printf("%d\n", sum);

    return 0;
}