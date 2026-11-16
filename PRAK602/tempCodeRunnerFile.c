#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    int angka[n];

    for (int i = 0; i < n; i++) {
        scanf("%d", &angka[i]);
    }

    for (int i = 0; i < n; i++) {
        int hasil = angka[i] * (i + 1);
        printf("%d ", hasil);
    }
    return 0;
}