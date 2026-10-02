#include <stdio.h>

int main() {
    FILE *gnuplot = popen("gnuplot -persistent", "w");
    if (gnuplot == NULL) {
        printf("Erro ao abrir o Gnuplot.\n");
        return 1;
    }

    fprintf(gnuplot, "set title 'Grafico da funcao f(x) = e^x'\n");
    fprintf(gnuplot, "set xlabel 'Eixo X'\n");
    fprintf(gnuplot, "set ylabel 'Eixo Y'\n");
    fprintf(gnuplot, "plot exp(x) with lines title 'e^x'\n");
}