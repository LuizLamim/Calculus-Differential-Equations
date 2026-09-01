#include <stdio.h>

int main() {
    double num1, num2, resultado;

    // Entrada dos números
    printf("Digite o primeiro número (dividendo): ");
    scanf("%lf", &num1);

    printf("Digite o segundo número (divisor): ");
    scanf("%lf", &num2);

    // Verificação essencial para evitar divisão por zero
    if (num2 == 0) {
        printf("Erro: Não é possível realizar divisão por zero!\n");
    } else {
        resultado = num1 / num2;
        printf("O resultado de %.2lf / %.2lf é: %.2lf\n", num1, num2, resultado);
    }

    return 0;
}