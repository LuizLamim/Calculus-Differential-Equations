#include <stdio.h>
#include <math.h>

#define WIDTH 60   // Largura do gráfico (colunas)
#define HEIGHT 20  // Altura do gráfico (linhas)

int main() {
    double x_min = 0.0;
    double x_max = 3.0;
    double y_min = 0.0;
    double y_max = exp(x_max); // e^3 ≈ 20.08
}

char grid[HEIGHT][WIDTH];
    
    // Inicializa a matriz do grid com espaços em branco
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            grid[i][j] = ' ';
        }
    }