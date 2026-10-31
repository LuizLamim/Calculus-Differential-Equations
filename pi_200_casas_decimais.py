from decimal import Decimal, getcontext

def calcular_pi(casas_decimais):
    # A precisão total é o número de casas decimais + 1 (para o dígito '3' antes da vírgula).
    # Adicionamos mais 2 dígitos extras durante o cálculo para evitar erros de arredondamento.
    getcontext().prec = casas_decimais + 3