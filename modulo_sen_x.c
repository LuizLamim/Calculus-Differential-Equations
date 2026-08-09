#include <stdio.h>
#include <math.h>

// Define a largura máxima do gráfico no terminal (amplitude)
#define LARGURA 60 
#define PI 3.14159265358979323846

int main() {
    double x;
    double passo = 0.15;        // O incremento de X a cada linha
    double max_x = 2 * PI;      // Vai plotar um ciclo completo de 0 a 2π

    printf("Grafico de f(x) = |sen(x)|\n");
    printf("---------------------------\n");
    printf("Eixo Y (0 a 1) -> Direita\n");
    printf("Eixo X (0 a 2pi) v Baixo\n\n");

    // Loop percorrendo os valores de X
    for (x = 0; x <= max_x; x += passo) {
        // Calcula o valor absoluto do seno de X
        double y = fabs(sin(x));
        
        // Mapeia o valor de Y (que vai de 0 a 1) para a largura da tela
        int posicao = (int)(y * LARGURA);

        // Imprime o valor de X no eixo vertical
        printf("%5.2f |", x);

        // Imprime os espaços em branco até a posição calculada
        for (int i = 0; i < posicao; i++) {
            printf(" ");
        }

        // Imprime o ponto da curva
        printf("*\n");
    }

    return 0;
}