def calcular_aceleracao_media(v_inicial, v_final, t_inicial, t_final):
    delta_v = v_final - v_inicial
    delta_t = t_final - t_inicial

    if delta_t == 0:
        raise ValueError("O intervalo de tempo (delta t) não pode ser zero.")
        
    return delta_v / delta_t

if __name__ == "__main__":

    try:

    except ValueError as e:
        print(f"\nErro nos dados inseridos: {e}")