#include <stdio.h>
#include <math.h>

int main() {
    double base, resultado;

    printf("Digite o numero base: ");
    if (scanf("%lf", &base) != 1) {
        printf("Entrada invalida!\n");
        return 1;
    }

    // Calcula base^300
    resultado = pow(base, 300);

    // Exibe em notacao cientifica e decimal padrao
    printf("\nResultado de %.2lf elevado a 300:\n", base);
    printf("Notacao Cientifica: %e\n", resultado);
    printf("Notacao Decimal:    %.2f\n", resultado);

    return 0;
}