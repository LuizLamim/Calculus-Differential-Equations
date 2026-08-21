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
}