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

int main() {
    const int totalPrimos = 20;
    std::vector<int> primos = gerarPrimeirosPrimos(totalPrimos);

    std::cout << "========================================================\n";
    std::cout << "        PLOT DOS 20 PRIMEIROS NUMEROS PRIMOS            \n";
    std::cout << "========================================================\n\n";

    // Plotagem gráfica simples via terminal (Gráfico de Barras)
    for (size_t i = 0; i < primos.size(); ++i) {
        // Exibe o índice e o valor do número primo
        std::cout << "P" << std::setw(2) << std::setfill('0') << i + 1 
                  << " (" << std::setw(2) << std::setfill(' ') << primos[i] << ") | ";

        // Imprime barras de acordo com o valor do número primo
        for (int j = 0; j < primos[i]; ++j) {
            std::cout << "█";
        }
        std::cout << "\n";
    }

    std::cout << "========================================================\n";

    return 0;
}