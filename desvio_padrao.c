#include <stdio.h>
#include <math.h>

int main() {
    int n, i;
    float soma = 0.0, media, soma_diferencas_quadrado = 0.0;
    float desvio_padrao_amostral, desvio_padrao_populacional;

    // Solicita o número de elementos
    printf("Digite a quantidade de elementos: ");
    scanf("%d", &n);

    // Validação da quantidade de elementos
    if (n <= 1) {
        printf("Para calcular o desvio padrao, informe pelo menos 2 elementos.\n");
        return 1;
    }

    float dados[n];

    // Entrada dos dados
    printf("Digite os %d elementos:\n", n);
    for (i = 0; i < n; i++) {
        printf("Elemento %d: ", i + 1);
        scanf("%f", &dados[i]);
        soma += dados[i];
    }

    // 1. Passo: Calcular a média
    media = soma / n;

    // 2. Passo: Calcular o somatório do quadrado das diferenças em relação à média
    for (i = 0; i < n; i++) {
        soma_diferencas_quadrado += pow(dados[i] - media, 2);
    }

    // 3. Passo: Calcular o desvio padrão
    // Amostral: divide por (n - 1)
    desvio_padrao_amostral = sqrt(soma_diferencas_quadrado / (n - 1));
    
    // Populacional: divide por n
    desvio_padrao_populacional = sqrt(soma_diferencas_quadrado / n);

    // Exibição dos resultados
    printf("\n--- Resultados ---\n");
    printf("Media: %.2f\n", media);
    printf("Desvio Padrao Amostral (n-1): %.4f\n", desvio_padrao_amostral);
    printf("Desvio Padrao Populacional (n): %.4f\n", desvio_padrao_populacional);

    return 0;
}