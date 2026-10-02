#include <stdio.h>

int main() {
    FILE *gnuplot = popen("gnuplot -persistent", "w");
}