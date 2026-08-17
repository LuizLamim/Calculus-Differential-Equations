#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main() {
    // Dimensões da tela em pixels
    int largura = 800;
    int altura = 600;
    
    // Centro da elipse
    double centroX = largura / 2.0;
    double centroY = altura / 2.0;
    
    // Semieixos da elipse
    double rx = 300.0; // Raio horizontal (a)
    double ry = 180.0; // Raio vertical (b)
    
    // Nome do arquivo de saída
    const char *nomeArquivo = "elipse.svg";
    FILE *fp = fopen(nomeArquivo, "w");
    
    if (fp == NULL) {
        printf("Erro ao criar o arquivo %s\n", nomeArquivo);
        return 1;
    }
    
    // Cabeçalho do SVG
    fprintf(fp, "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n");
    fprintf(fp, "<svg width=\"%d\" height=\"%d\" xmlns=\"http://www.w3.org/2000/svg\">\n", largura, altura);
    
    // Fundo escuro
    fprintf(fp, "  <rect width=\"100%%\" height=\"100%%\" fill=\"#1e1e2e\" />\n");
    
    // Grade de fundo (opcional)
    fprintf(fp, "  <g stroke=\"#313244\" stroke-width=\"1\" stroke-dasharray=\"5,5\">\n");
    for (int x = 100; x < largura; x += 100) {
        fprintf(fp, "    <line x1=\"%d\" y1=\"0\" x2=\"%d\" y2=\"%d\" />\n", x, x, altura);
    }
    for (int y = 100; y < altura; y += 100) {
        fprintf(fp, "    <line x1=\"0\" y1=\"%d\" x2=\"%d\" y2=\"%d\" />\n", y, largura, y);
    }
    fprintf(fp, "  </g>\n");
    
    // Eixos Cartesianos
    fprintf(fp, "  <line x1=\"%.1f\" y1=\"0\" x2=\"%.1f\" y2=\"%d\" stroke=\"#585b70\" stroke-width=\"2\" />\n", centroX, centroX, altura);
    fprintf(fp, "  <line x1=\"0\" y1=\"%.1f\" x2=\"%d\" y2=\"%.1f\" stroke=\"#585b70\" stroke-width=\"2\" />\n", centroY, largura, centroY);
    
    // Desenho da Elipse
    fprintf(fp, "  <ellipse cx=\"%.1f\" cy=\"%.1f\" rx=\"%.1f\" ry=\"%.1f\"\n", centroX, centroY, rx, ry);
    fprintf(fp, "           fill=\"rgba(137, 180, 250, 0.25)\"\n");
    fprintf(fp, "           stroke=\"#89b4fa\" stroke-width=\"4\" />\n");
    
    // Marcadores dos Focos
    double c = sqrt(rx * rx - ry * ry); // Distância focal
    fprintf(fp, "  <circle cx=\"%.1f\" cy=\"%.1f\" r=\"6\" fill=\"#f38ba8\" />\n", centroX - c, centroY);
    fprintf(fp, "  <circle cx=\"%.1f\" cy=\"%.1f\" r=\"6\" fill=\"#f38ba8\" />\n", centroX + c, centroY);
    
    // Centro
    fprintf(fp, "  <circle cx=\"%.1f\" cy=\"%.1f\" r=\"5\" fill=\"#a6e3a1\" />\n", centroX, centroY);
    
    // Título e Legenda
    fprintf(fp, "  <text x=\"20\" y=\"40\" font-family=\"sans-serif\" font-size=\"20\" fill=\"#cdd6f4\" font-weight=\"bold\">Plotagem de Elipse em C (SVG)</text>\n");
    fprintf(fp, "  <text x=\"20\" y=\"70\" font-family=\"sans-serif\" font-size=\"14\" fill=\"#bac2de\">Centro: (%.0f, %.0f) | Raio X (a): %.0f | Raio Y (b): %.0f</text>\n", centroX, centroY, rx, ry);
    
    fprintf(fp, "</svg>\n");
    
    fclose(fp);
    printf("Arquivo '%s' gerado com sucesso!\n", nomeArquivo);
    return 0;
}