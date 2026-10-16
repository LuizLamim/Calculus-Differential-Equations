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

    // Tabela de classificação da OMS
    if (imc < 18.5) {
        std::cout << "Abaixo do peso" << std::endl;
    } else if (imc >= 18.5 && imc < 25.0) {
        std::cout << "Peso normal" << std::endl;
    } else if (imc >= 25.0 && imc < 30.0) {
        std::cout << "Sobrepeso" << std::endl;
    } else if (imc >= 30.0 && imc < 35.0) {
        std::cout << "Obesidade Grau I" << std::endl;
    } else if (imc >= 35.0 && imc < 40.0) {
        std::cout << "Obesidade Grau II" << std::endl;
    } else {
        std::cout << "Obesidade Grau III (morbida)" << std::endl;
    }

    return 0;
}