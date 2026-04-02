#include <stdio.h>

int Rev(int n) {
    int reverse = 0;
    while (n > 0) {
        reverse = reverse*10 + (n%10);
        n /= 10;
    }
    return reverse;
}

int main() {
    int X, Y;
    // 
    if (scanf("%d %d", &X, &Y) == 2) {
        int result = Rev(Rev(X) + Rev(Y));
        printf("%d\n", result);
    }
    return 0;
}