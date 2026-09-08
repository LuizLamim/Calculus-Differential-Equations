#include <stdio.h>
#include <math.h>

int main() {
    double base, expoente, resultado;

    // Solicita os dados ao usuário
    printf("Digite a base: ");
    scanf("%lf", &base);

    printf("Digite o expoente: ");
    scanf("%lf", &expoente);

    // Calcula a potência (base elevada ao expoente)
    resultado = pow(base, expoente);

    // Exibe o resultado
    printf("%.2lf elevado a %.2lf e igual a: %.2lf\n", base, expoente, resultado);

    return 0;
}