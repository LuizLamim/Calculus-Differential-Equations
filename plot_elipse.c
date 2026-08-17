#include <stdio.h>
#include <math.h>

#define LARGURA 60
#define ALTURA 30

int main() {
    // Tela de caracteres
    char tela[ALTURA][LARGURA];

    // Parâmetros da elipse
    double a = 20.0; // Raio horizontal (em caracteres)
    double b = 8.0;  // Raio vertical (em linhas)

    // Centro da tela
    int centroX = LARGURA / 2;
    int centroY = ALTURA / 2;

    // Fator de correção de aspecto do terminal (caracteres são ~2x mais altos)
    double aspectoTerminal = 2.0;

    // Inicializa a tela com espaços em branco
    for (int y = 0; y < ALTURA; y++) {
        for (int x = 0; x < LARGURA; x++) {
            tela[y][x] = ' ';
        }
    }

    // Desenha o contorno da elipse
    for (int y = 0; y < ALTURA; y++) {
        for (int x = 0; x < LARGURA; x++) {
            // Relativo ao centro e ajustado para o aspecto dos caracteres
            double dx = (x - centroX) / aspectoTerminal;
            double dy = (y - centroY);

            // Equação da elipse: (x^2 / a^2) + (y^2 / b^2)
            double valor = (dx * dx) / (a * a) + (dy * dy) / (b * b);

            // Tolerância para desenhar apenas a borda (linhas)
            if (valor >= 0.85 && valor <= 1.15) {
                tela[y][x] = '*';
            }
        }
    }

    // Imprime a tela no terminal
    for (int y = 0; y < ALTURA; y++) {
        for (int x = 0; x < LARGURA; x++) {
            putchar(tela[y][x]);
        }
        putchar('\n');
    }

    return 0;
}