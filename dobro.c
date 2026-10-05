#include <stdio.h>

// Função que recebe um número e retorna o seu dobro
int dobrar(int numero) {
    return numero * 2;
}

int main() {
    int num, resultado;

    // Solicita o número ao usuário
    printf("Digite um número inteiro: ");
    scanf("%d", &num);

    // Chama a função para calcular o dobro
    resultado = dobrar(num);

    // Mostra o resultado
    printf("O dobro de %d é: %d\n", num, resultado);

    return 0;
}