#include <stdio.h>

int main() {
    int contadorPrimos = 0;
    int numeroAtual = 2;

    printf("Os 25 primeiros numeros primos sao:\n");

    // Continua o loop até encontrar 25 números primos
    while (contadorPrimos < 25) {
        int ehPrimo = 1; // Assume que o número é primo inicialmente

        // Testa se o númeroAtual é divisível por algum número entre 2 e a raiz dele (ou até a metade)
        for (int i = 2; i <= numeroAtual / 2; i++) {
            if (numeroAtual % i == 0) {
                ehPrimo = 0; // Não é primo
                break;
            }
        }

        // Se for primo, exibe e incrementa o contador
        if (ehPrimo) {
            contadorPrimos++;
            printf("%dº primo: %d\n", contadorPrimos, numeroAtual);
        }

        numeroAtual++;
    }

    return 0;
}