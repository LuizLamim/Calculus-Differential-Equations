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
    
    # 10 iterações são mais que suficientes para gerar milhares de casas decimais
    for _ in range(10):
        a_next = (a + b) / Decimal(2)
        b = (a * b).sqrt()
        t -= p * (a - a_next) ** 2
        a = a_next
        p *= 2
        
    pi = ((a + b) ** 2) / (Decimal(4) * t)
    
    # Ajusta a precisão final para o valor exato desejado (200 casas decimais + o '3')
    getcontext().prec = casas_decimais + 1
    return +pi # O operador '+' aplica a precisão final ao número

# Calcula e imprime o valor
pi_200 = calcular_pi(200)
print("Valor de Pi com 200 casas decimais:")
print(pi_200)