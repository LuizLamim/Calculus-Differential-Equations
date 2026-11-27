import math


def calcular_volume_semiesfera(raio: float) -> float:
    """Calcula o volume de uma semiesfera dado o seu raio."""
    if raio < 0:
        raise ValueError("O raio não pode ser um valor negativo.")

    volume = (2 / 3) * math.pi * (raio**3)
    return volume


def main():
    try:
        entrada = input("Digite o valor do raio da semiesfera: ").replace(
            ",", "."
        )
        raio = float(entrada)

        volume = calcular_volume_semiesfera(raio)
        print(f"O volume da semiesfera é: {volume:.2f} unidades cúbicas")

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()