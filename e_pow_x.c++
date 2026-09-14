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
}