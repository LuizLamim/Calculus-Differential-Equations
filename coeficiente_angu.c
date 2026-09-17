#include <stdio.h>

int main(){
    float x1, y1, x2, y2, m;

    printf("--- Calculadora de Coeficiente Angular ---\n\n");

    // Entrada dos dados do primeiro ponto
    printf("Digite as coordenadas do Ponto A (x1 y1): ");
    scanf("%f %f", &x1, &y1);

    // Entrada dos dados do segundo ponto
    printf("Digite as coordenadas do Ponto B (x2 y2): ");
    scanf("%f %f", &x2, &y2);

    // Verificação para evitar divisão por zero (reta vertical)
    if (x1 == x2) {
        printf("\nErro: A reta e vertical (x1 = x2). O coeficiente angular e indefinido.\n");
    } else {
        // Cálculo do coeficiente angular
        m = (y2 - y1) / (x2 - x1);
        printf("\nO coeficiente angular (m) da reta e: %.2f\n", m);
    }

}