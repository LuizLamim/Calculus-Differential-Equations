def calcular_aceleracao():
    print("=== Calculadora de Taxa de Variação de Velocidade (Aceleração) ===\n")
    
    # Seleção de unidade de medida
    print("Escolha a unidade de velocidade:")
    print("1 - Metros por segundo (m/s)")
    print("2 - Quilômetros por hora (km/h)")
    opcao = input("Opção (1 ou 2): ").strip()
    
    try:
        # Entrada dos dados
        v_inicial = float(input("\nInforme a velocidade inicial: "))
        v_final = float(input("Informe a velocidade final: "))
        tempo = float(input("Informe o tempo gasto (em segundos): "))
        
        # Validação do tempo
        if tempo <= 0:
            print("\nErro: O tempo precisa ser maior que zero!")
            return

        # Converter km/h para m/s se necessário (1 m/s = 3.6 km/h)
        if opcao == "2":
            v_inicial_ms = v_inicial / 3.6
            v_final_ms = v_final / 3.6
        else:
            v_inicial_ms = v_inicial
            v_final_ms = v_final

        # Cálculo da variação de velocidade e aceleração
        delta_v = v_final_ms - v_inicial_ms
        aceleracao = delta_v / tempo

        # Exibição dos resultados
        print("\n" + "="*40)
        print("RESULTADOS:")
        print(f"Variação de velocidade (Δv): {delta_v:.2f} m/s")
        print(f"Aceleração média: {aceleracao:.2f} m/s²")
        print("="*40)

        # Interpretação do resultado
        if aceleracao > 0:
            print("O movimento é ACELERADO (a velocidade aumentou).")
        elif aceleracao < 0:
            print("O movimento é RETARDADO / DESACELERADO (a velocidade diminuiu).")
        else:
            print("A velocidade é CONSTANTE (aceleração nula).")

    except ValueError:
        print("\nErro: Por favor, insira apenas valores numéricos válidos.")

# Executa o programa
if __name__ == "__main__":
    calcular_aceleracao()