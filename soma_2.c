#include <stdio.h>

int main()

    float num1, num2, soma;

    // Leitura dos dados de entrada
    printf("Digite o primeiro número: ");
    scanf("%f", &num1);

    printf("Digite o segundo número: ");
    scanf("%f", &num2);

    // Cálculo da soma
    soma = num1 + num2;

    // Exibição do resultado
    printf("A soma entre %.2f e %.2f é: %.2f\n", num1, num2, soma);