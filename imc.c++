#include <iostream>
#include <iomanip>

int main() {
    double peso, altura, imc;

    std::cout << "--- Calculadora de IMC ---" << std::endl;

    // Entrada de dados
    std::cout << "Digite o seu peso (em kg): ";
    std::cin >> peso;

    std::cout << "Digite a sua altura (em metros, ex: 1.75): ";
    std::cin >> altura;

    // Validação básica para evitar divisão por zero
    if (altura <= 0 || peso <= 0) {
        std::cout << "\nErro: O peso e a altura devem ser valores maiores que zero." << std::endl;
        return 1;
    }

    // Cálculo do IMC: peso / (altura * altura)
    imc = peso / (altura * altura);

    // Configura a exibição de números para mostrar apenas 2 casas decimais
    std::cout << std::fixed << std::setprecision(2);

    // Exibição do resultado
    std::cout << "\nSeu IMC e: " << imc << std::endl;
    std::cout << "Classificacao: ";
}