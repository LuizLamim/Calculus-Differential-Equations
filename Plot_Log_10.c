#include <stdio.h>
#include <math.h>

#define WIDTH 60   // Largura do gráfico (eixo X)
#define HEIGHT 20  // Altura do gráfico (eixo Y)

int main() {
    char grid[HEIGHT][WIDTH];

    // Inicializa a matriz do gráfico com espaços em branco
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = ' ';
        }
    }

    // Definindo os limites do gráfico
    double x_min = 1.0;
    double x_max = 100.0;
    double y_min = 0.0;   // log10(1) = 0
    double y_max = 2.0;   // log10(100) = 2

    // Calcula e posiciona os pontos da função log10(x) na matriz
    for (int j = 0; j < WIDTH; j++) {
        // Mapeia a coluna j para um valor de x entre x_min e x_max
        double x = x_min + (j / (double)(WIDTH - 1)) * (x_max - x_min);
        double y = log10(x);
        
        // Mapeia o valor de y para a linha correspondente na matriz (invertido pois o eixo Y do terminal cresce para baixo)
        int i = HEIGHT - 1 - (int)(((y - y_min) / (y_max - y_min)) * (HEIGHT - 1));
        
        // Garante que o ponto está dentro dos limites da matriz antes de plotar
        if (i >= 0 && i < HEIGHT) {
            grid[i][j] = '*';
        }
    }

    // Exibe o gráfico no terminal com o eixo Y
    printf("=== Grafico da Funcao Log10(x) ===\n\n");
    for (int i = 0; i < HEIGHT; i++) {
        double y_val = y_max - (i / (double)(HEIGHT - 1)) * (y_max - y_min);
        printf("%4.1f |", y_val);
        for (int j = 0; j < WIDTH; j++) {
            putchar(grid[i][j]);
        }
        putchar('\n');
    }

    return 0;
}