#include <stdio.h>
#include <math.h>

#define WIDTH 60   // Largura do gráfico (colunas)
#define HEIGHT 20  // Altura do gráfico (linhas)

int main() {
    double x_min = 0.0;
    double x_max = 3.0;
    double y_min = 0.0;
    double y_max = exp(x_max); // e^3 ≈ 20.08
    
    char grid[HEIGHT][WIDTH];
    
    // Inicializa a matriz do grid com espaços em branco
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = ' ';
        }
    }
    
    // Calcula os pontos da função e mapeia para o grid
    for (int j = 0; j < WIDTH; j++) {
        // Mapeia a coluna j para o valor de x
        double x = x_min + (j / (double)(WIDTH - 1)) * (x_max - x_min);
        double y = exp(x); // Função e^x
        
        // Mapeia o valor de y para a linha i correspondente
        int i = HEIGHT - 1 - (int)((y - y_min) / (y_max - y_min) * (HEIGHT - 1));
        
        // Se o ponto estiver dentro dos limites do grid, desenha o caractere '*'
        if (i >= 0 && i < HEIGHT) {
            grid[i][j] = '*';
        }
    }
    
    // Imprime o cabeçalho
    printf("========================================\n");
    printf("       Grafico da Funcao f(x) = e^x     \n");
    printf("========================================\n\n");
    
    // Imprime o gráfico linha por linha junto com o eixo Y
    for (int i = 0; i < HEIGHT; i++) {
        double y_val = y_max - (i / (double)(HEIGHT - 1)) * (y_max - y_min);
        printf("%5.1f |", y_val);
        
        for (int j = 0; j < WIDTH; j++) {
            putchar(grid[i][j]);
        }
        putchar('\n');
    }
    
    // Desenha o eixo X inferior
    printf("      +");
    for (int j = 0; j < WIDTH; j++) {
        putchar('-');
    }
    printf("\n");
    
    // Imprime os rótulos do eixo X
    printf("        %.1f", x_min);
    for (int j = 0; j < WIDTH - 12; j++) {
        putchar(' ');
    }
    printf("%.1f\n", x_max);
    
    return 0;
}