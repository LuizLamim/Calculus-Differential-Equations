import matplotlib.pyplot as plt

def eh_primo(n):
    """Verifica se um número n é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def obter_primeiros_primos(qtd):
    """Retorna uma lista com a quantidade (qtd) desejada de números primos."""
    primos = []
    numero = 2
    while len(primos) < qtd:
        if eh_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# 1. Obter os 26 primeiros números primos
quantidade = 26
primos = obter_primeiros_primos(quantidade)
posicoes = list(range(1, quantidade + 1))  # Índice de 1 a 26

# 2. Configurar e exibir o gráfico
plt.figure(figsize=(10, 6))
plt.plot(
    posicoes,
    primos,
    marker="o",
    color="b",
    linestyle="-",
    linewidth=1.5,
    markersize=6,
)

# Adicionar o valor exato acima de cada ponto no gráfico
for i, valor in enumerate(primos):
    plt.text(
        posicoes[i],
        valor + 1,
        str(valor),
        ha="center",
        va="bottom",
        fontsize=8,
    )