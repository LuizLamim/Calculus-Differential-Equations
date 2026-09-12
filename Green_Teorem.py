import sympy as sp

def demonstrar_teorema_green():
    # 1. Definindo as variáveis simbólicas
    x, y = sp.symbols('x y')

    # 2. Definindo o campo vetorial F = (L, M)
    # Escolhemos um campo vetorial arbitrário para o teste
    L = x**2 - y**2
    M = 2*x*y

    print("--- DEMONSTRAÇÃO DO TEOREMA DE GREEN ---")
    print(f"Campo vetorial: L(x,y) = {L}, M(x,y) = {M}")
    print("Região D: Quadrado de (0,0) a (1,1)\n")
    
    # ==========================================
    # LADO DIREITO: Integral Dupla
    # ==========================================
    # Derivadas parciais
    dM_dx = sp.diff(M, x)
    dL_dy = sp.diff(L, y)
    
    # Integrando da integral dupla
    integrando_duplo = dM_dx - dL_dy
    
    # Calculando a integral dupla (x de 0 a 1, y de 0 a 1)
    integral_dupla = sp.integrate(sp.integrate(integrando_duplo, (x, 0, 1)), (y, 0, 1))
    
    print("1. Calculando a Integral Dupla ∬ (∂M/∂x - ∂L/∂y) dA:")
    print(f"   ∂M/∂x = {dM_dx}")
    print(f"   ∂L/∂y = {dL_dy}")
    print(f"   Integrando = {integrando_duplo}")
    print(f"   Resultado da Integral Dupla = {integral_dupla}\n")
    
    # ==========================================
    # LADO ESQUERDO: Integral de Linha (4 segmentos)
    # ==========================================
    # O quadrado tem 4 lados (C1, C2, C3, C4) percorridos no sentido anti-horário.