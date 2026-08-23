#include <iostream>
#include <cmath>
#include <iomanip>

// Constantes físicas
const double G = 6.67430e-11;      // Constante gravitacional em m^3 kg^-1 s^-2
const double c = 299792458.0;      // Velocidade da luz em m/s
const double mass_sun = 1.989e30;  // Massa do sol em kg

int main() {
    double solar_masses;

    std::cout << "--- Calculadora de Raio de Schwarzschild ---" << std::endl;
    std::cout << "Digite a massa do objeto (em massas solares): ";
    
    // Verifica se a entrada é válida
    if (!(std::cin >> solar_masses) || solar_masses <= 0) {
        std::cerr << "Erro: Por favor, insira um numero positivo valido." << std::endl;
        return 1;
    }

    // Conversão de massas solares para quilogramas
    double mass_kg = solar_masses * mass_sun;
    
    // Cálculo do raio
    double radius = (2 * G * mass_kg) / std::pow(c, 2);

    std::cout << "\nPara um objeto com " << solar_masses << " massa(s) solar(es):" << std::endl;
    std::cout << std::fixed << std::setprecision(2);
    std::cout << "O raio do buraco negro seria: " << radius << " metros." << std::endl;

    return 0;
}