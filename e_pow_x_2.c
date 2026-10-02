#include <stdio.h>

int main() {
    FILE *gnuplot = popen("gnuplot -persistent", "w");
    if (gnuplot == NULL) {
        printf("Erro ao abrir o Gnuplot.\n");
        return 1;
    }
}