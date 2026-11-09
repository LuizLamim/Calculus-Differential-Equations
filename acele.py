def calcular_aceleracao_media(v_inicial, v_final, t_inicial, t_final):
    delta_v = v_final - v_inicial
    delta_t = t_final - t_inicial
    
    if delta_t == 0:
        raise ValueError("O intervalo de tempo (delta t) não pode ser zero.")
        
    return delta_v / delta_t

if __name__ == "__main__":
    print("--- Calculadora de Aceleração Média ---")
    try:
        vi = float(input("Digite a velocidade inicial (m/s): "))
        vf = float(input("Digite a velocidade final (m/s): "))
        ti = float(input("Digite o tempo inicial (s): "))
        tf = float(input("Digite o tempo final (s): "))
        
        aceleracao = calcular_aceleracao_media(vi, vf, ti, tf)
        print(f"\nAceleração média calculada: {aceleracao:.2f} m/s²")
        
    except ValueError as e:
        print(f"\nErro nos dados inseridos: {e}")