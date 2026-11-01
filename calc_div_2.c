#include <stdio.h>

int main() {
    float numero, resultado;

    printf("Digite um numero: ");
    scanf("%f", &numero);

    resultado = numero / 2.0;

    printf("A metade de %.2f e %.2f\n", numero, resultado);

    return 0;
}