#include <iostream>

// Função para verificar se um número é primo
bool ehPrimo(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

int main(){
    const int TOTAL_PRIMOS = 10;
    int contador = 0;
    int numero = 2;
    int soma = 0;

    std::cout << "Os primeiros " << TOTAL_PRIMOS << " números primos são:\n";

    while (contador < TOTAL_PRIMOS) {
        if (ehPrimo(numero)) {
            std::cout << numero << (contador < TOTAL_PRIMOS - 1 ? ", " : "\n");
            soma += numero;
            contador++;
        }
        numero++;
    }

    std::cout << "Soma dos primeiros 10 primos: " << soma << std::endl;

}