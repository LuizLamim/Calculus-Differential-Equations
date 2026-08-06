#include <matplot/matplot.h>
#include <cmath>
#include <vector>

int main() {
    using namespace matplot;

    // 1. Criar os vetores de domínio (-5 a 5)
    std::vector<double> x = linspace(-5, 5, 100);
    std::vector<double> y = linspace(-5, 5, 100);

    // 2. Criar a grade bidimensional (Meshgrid)
    auto [X, Y] = meshgrid(x, y);

    // 3. Calcular Z = sin(sqrt(x^2 + y^2))
    auto Z = transform(X, Y, [](double x, double y) {
        return std::sin(std::sqrt(x * x + y * y));
    });

    // 4. Criar o gráfico de curvas de nível preenchido
    figure();
    contourf(X, Y, Z)->number_of_levels(20);

    // Personalização
    title("Curvas de Nivel: z = sin(sqrt(x^2 + y^2))");
    xlabel("Eixo X");
    ylabel("Eixo Y");
    colorbar();

    // 5. Exibir o gráfico
    show();

    return 0;
}