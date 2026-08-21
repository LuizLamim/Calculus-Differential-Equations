#include <stdio.h>

#define LARGURA 60
#define ALTURA 20

int main() {
    char grade[ALTURA][LARGURA];

    // 1. Inicializa a grade com espaços em branco
    for (int i = 0; i < ALTURA; i++) {
        for (int j = 0; j < LARGURA; j++) {
            grade[i][j] = ' ';
        }
    }

    // 2. Define o intervalo do eixo X
    double x_min = -15.0;
    double x_max = 15.0;
    
    // O valor mínimo de y ocorre quando x = 0 (y = 458)
    // O valor máximo ocorre nos extremos de x (y = 15^2 + 458 = 683)
    double y_min = 458.0;
    double y_max = (x_max * x_max) + 458.0; 
    
    // 3. Calcula os pontos da parábola e os coloca na grade
    for (int j = 0; j < LARGURA; j++) {
        // Encontra qual é o 'x' correspondente a esta coluna
        double x = x_min + (x_max - x_min) * ((double)j / (LARGURA - 1));
        
        // Aplica a equação
        double y = (x * x) + 458.0;
        
        // Converte o valor de 'y' para a linha correspondente na matriz
        // (Invertemos a linha porque no terminal a linha 0 fica no topo)
        int i = ALTURA - 1 - (int)((y - y_min) / (y_max - y_min) * (ALTURA - 1));
        
        if (i >= 0 && i < ALTURA) {
            grade[i][j] = '*';
        }
    }
}