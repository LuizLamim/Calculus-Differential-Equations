from decimal import Decimal, getcontext

def calcular_pi(casas_decimais):
    # A precisão total é o número de casas decimais + 1 (para o dígito '3' antes da vírgula).
    # Adicionamos mais 2 dígitos extras durante o cálculo para evitar erros de arredondamento.
    getcontext().prec = casas_decimais + 3

    # Valores iniciais do algoritmo de Gauss-Legendre
    a = Decimal(1)
    b = Decimal(1) / Decimal(2).sqrt()
    t = Decimal(1) / Decimal(4)
    p = Decimal(1)