#include <iostream>
#include <vector>
#include <string>

int main() {
    const int LARGURA = 40;
    const int ALTURA = 20;

    // Matriz para o gráfico no terminal
    std::vector<std::string> tela(ALTURA, std::string(LARGURA, ' '));

    // Desenha os eixos cartesianos
    int centro_x = LARGURA / 2;
    int centro_y = ALTURA / 2;

    for (int i = 0; i < LARGURA; ++i) tela[centro_y][i] = '-'; // Eixo X
    for (int i = 0; i < ALTURA; ++i) tela[i][centro_x] = '|';  // Eixo Y
    tela[centro_y][centro_x] = '+';

    // Mapeamento e plotagem da função f(x) = 32x
    // Escala ajustada para caber no terminal
    for (int px = 0; px < LARGURA; ++px) {
        double x = (px - centro_x) * 0.5; // Escala do eixo X
        double y = 32.0 * x;               // f(x) = 32x

        int py = centro_y - static_cast<int>(y / 16.0); // Ajuste de escala vertical

        if (py >= 0 && py < ALTURA) {
            tela[py][px] = '*';
        }
    }

    // Exibe o gráfico no terminal
    std::cout << "--- Gráfico de f(x) = 32x (Terminal) ---\n\n";
    for (const auto& linha : tela) {
        std::cout << linha << "\n";
    }

    return 0;
}