#include <stdio.h>
#include <math.h>

int main(){
    float x1, y1, x2, y2, distancia;

    // Entrada dos dados do primeiro ponto
    printf("Digite as coordenadas do Ponto 1 (x1 y1): ");
    scanf("%f %f", &x1, &y1);

    // Entrada dos dados do segundo ponto
    printf("Digite as coordenadas do Ponto 2 (x2 y2): ");
    scanf("%f %f", &x2, &y2);

    // Calculo da distancia usando sqrt() para a raiz e pow() para a potencia
    distancia = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2));

    // Exibicao do resultado com 2 casas decimais
    printf("\nA distancia entre os pontos (%.2f, %.2f) e (%.2f, %.2f) e: %.2f\n", 
            x1, y1, x2, y2, distancia);
}