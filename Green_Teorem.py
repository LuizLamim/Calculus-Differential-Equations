import sympy as sp

def demonstrar_teorema_green():
    # 1. Definindo as variáveis simbólicas
    x, y = sp.symbols('x y')

    # 2. Definindo o campo vetorial F = (L, M)
    # Escolhemos um campo vetorial arbitrário para o teste
    L = x**2 - y**2
    M = 2*x*y