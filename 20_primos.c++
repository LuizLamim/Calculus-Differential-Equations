#include <iostream>
#include <vector>
#include <iomanip>

// Função para verificar se um número é primo
bool ehPrimo(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) return false;
    }
    return true;
}

// Função para gerar os N primeiros números primos
std::vector<int> gerarPrimeirosPrimos(int quantidade) {
    std::vector<int> primos;
    int numero = 2;

    while (primos.size() < quantidade) {
        if (ehPrimo(numero)) {
            primos.push_back(numero);
        }
        numero++;
    }

    return primos;
}