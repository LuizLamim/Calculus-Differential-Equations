#include <stdio.h>
#include <math.h> // Necessário para a função cbrt()

int main() {
    double numero, resultado;

    // Solicita o número ao usuário
    printf("Digite um numero para calcular a raiz cubica: ");
    if (scanf("%lf", &numero) == 1) {
        
        // Calcula a raiz cúbica
        resultado = cbrt(numero);

        // Exibe o resultado formatado
        printf("A raiz cubica de %.2lf e %.4lf\n", numero, resultado);
        
    } else {
        printf("Por favor, insira um numero valido.\n");
    }

    return 0;
}