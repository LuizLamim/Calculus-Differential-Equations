#include <iostream>
#include <iomanip> // Necessário para formatar as casas decimais

int main() {
    double num1, num2, resultado;

    // Entrada dos números usando std::cin
    std::cout << "Digite o primeiro número (dividendo): ";
    std::cin >> num1;

    std::cout << "Digite o segundo número (divisor): ";
    std::cin >> num2;

    // Verificação essencial para evitar divisão por zero
    if (num2 == 0) {
        std::cout << "Erro: Não é possível realizar divisão por zero!\n";
    } else {
        resultado = num1 / num2;
        
        // Configura a exibição para 2 casas decimais
        std::cout << std::fixed << std::setprecision(2);
        std::cout << "O resultado de " << num1 << " / " << num2 << " é: " << resultado << "\n";
    }

    return 0;
}