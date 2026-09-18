#include <iostream>
#include <fstream>

int main() {
    // Abre o arquivo para escrita
    std::ofstream arquivo("grafico_32x.csv");

    if (!arquivo.is_open()) {
        std::cerr << "Erro ao criar o arquivo!" << std::endl;
        return 1;
    }

    // Escreve os cabeçalhos das colunas
    arquivo << "x,f(x)\n";

    // Gera os pontos de x de -10 até 10 com passo de 1
    int x_inicio = -10;
    int x_fim = 10;
    int passo = 1;

    for (int x = x_inicio; x <= x_fim; x += passo) {
        double y = 32.0 * x; // f(x) = 32x
        arquivo << x << "," << y << "\n";
    }

    arquivo.close();

    std::cout << "Dados gerados com sucesso no arquivo 'grafico_32x.csv'!\n";
    std::cout << "Abra este arquivo no Excel ou Google Sheets para exibir o gráfico de linha.\n";

    return 0;
}