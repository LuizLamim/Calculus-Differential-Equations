#include <stdio.h>
#include <math.h>

int main() {
    // Configurações do gráfico
    int resolucao_y = 50;         // Largura máxima (colunas) para y = 1
    int passos_x = 40;            // Quantidade de linhas (pontos no eixo X)
    double limite_x = 4 * M_PI;   // Plotar de 0 a 4π (dois ciclos completos)

    // Cabeçalho
    printf("Eixo X | Grafico de f(x) = |sen(x)|\n");
    printf("-------+---------------------------------------------------\n");

    for (int i = 0; i <= passos_x; i++) {
        // Calcula o valor de x
        double x = (double)i / passos_x * limite_x;
        
        // Calcula f(x) = |sen(x)|
        double y = fabs(sin(x));
        
        // Converte o valor de y (0 a 1) para a posição na tela (0 a resolucao_y)
        int posicao = (int)(y * resolucao_y);

        // Imprime o valor de X formatado e a barra do eixo
        printf("%5.2f  |", x);

        // Imprime os espaços até o ponto da curva
        for (int j = 0; j < posicao; j++) {
            printf(" ");
        }
        
        // Imprime o ponto
        printf("*\n");
    }

    return 0;
}