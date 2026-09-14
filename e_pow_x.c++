#include <iostream>
#include <cmath>
#include <vector>

int main() {
    // Configurações do gráfico
    const int LARGURA = 60;   // Resolução horizontal
    const int ALTURA = 20;    // Resolução vertical
    
    const double X_MIN = -2.0;
    const double X_MAX = 2.5;
    const double Y_MIN = 0.0;
    const double Y_MAX = 12.0;

    // Cria a matriz preenchida com espaços em branco
    std::vector<std::string> grade(ALTURA, std::string(LARGURA, ' '));

    // 1. Desenha os eixos X e Y
    for (int i = 0; i < ALTURA; ++i) {
        for (int j = 0; j < LARGURA; ++j) {
            // Mapeia coordenadas do gráfico para o plano de texto
            double x = X_MIN + j * (X_MAX - X_MIN) / (LARGURA - 1);
            double y = Y_MAX - i * (Y_MAX - Y_MIN) / (ALTURA - 1);

            // Linha do eixo X (onde y se aproxima de 0)
            if (std::abs(y) < (Y_MAX - Y_MIN) / (2 * ALTURA)) grade[i][j] = '-';
            // Linha do eixo Y (onde x se aproxima de 0)
            if (std::abs(x) < (X_MAX - X_MIN) / (2 * LARGURA)) grade[i][j] = '|';
            // Cruzamento dos eixos
            if (std::abs(x) < (X_MAX - X_MIN) / (2 * LARGURA) && 
                std::abs(y) < (Y_MAX - Y_MIN) / (2 * ALTURA)) grade[i][j] = '+';
        }
    }
}