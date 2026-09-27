#include <iostream>
#include <cmath>

// Função para verificar se um número é primo
bool ehPrimo(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0 || n % 3 == 0) return false;
    
    for (int i = 5; i * i <= n; i += 6) {
        if (n % i == 0 || n % (i + 2) == n % i) // Otimização para testar apenas fatores possíveis
            return false;
    }
    // Simplificação mais limpa do loop acima:
    // for (int i = 2; i <= sqrt(n); i++) {
    //     if (n % i == 0) return false;
    // }
    
    return true;
}