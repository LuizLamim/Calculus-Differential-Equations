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
    
    # C1: y = 0, dy = 0, x varia de 0 a 1
    int_c1 = sp.integrate(L.subs(y, 0), (x, 0, 1))
    
    # C2: x = 1, dx = 0, y varia de 0 a 1
    int_c2 = sp.integrate(M.subs(x, 1), (y, 0, 1))
    
    # C3: y = 1, dy = 0, x varia de 1 a 0 (sentido inverso)
    int_c3 = sp.integrate(L.subs(y, 1), (x, 1, 0))
    
    # C4: x = 0, dx = 0, y varia de 1 a 0 (sentido inverso)
    int_c4 = sp.integrate(M.subs(x, 0), (y, 1, 0))
    
    integral_linha = int_c1 + int_c2 + int_c3 + int_c4
    
    print("2. Calculando a Integral de Linha ∮ (L dx + M dy):")
    print(f"   Segmento C1 (y=0, x de 0 a 1): {int_c1}")
    print(f"   Segmento C2 (x=1, y de 0 a 1): {int_c2}")
    print(f"   Segmento C3 (y=1, x de 1 a 0): {int_c3}")
    print(f"   Segmento C4 (x=0, y de 1 a 0): {int_c4}")
    print(f"   Resultado da Integral de Linha = {integral_linha}\n")
    
    # ==========================================
    # VERIFICAÇÃO FINAL
    # ==========================================
    if integral_dupla == integral_linha:
        print("CONCLUSÃO: Os resultados são idênticos!")
        print(f"Ambos os lados resultaram em {integral_dupla}. O Teorema de Green foi demonstrado com sucesso.")
    else:
        print("ERRO: Os resultados diferem.")

# Executa o programa
if __name__ == "__main__":
    demonstrar_teorema_green()