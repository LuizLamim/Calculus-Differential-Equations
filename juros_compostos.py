def calcular_juros_compostos():
    print("=== Calculadora de Juros Compostos ===")
    
    # Entrada de dados
    capital_inicial = float(input("Valor inicial (R$): "))
    aporte_mensal = float(input("Aporte mensal (R$) [digite 0 se não houver]: "))
    taxa_juros = float(input("Taxa de juros (%): "))
    tipo_taxa = input("A taxa é 'mensal' ou 'anual'? ").strip().lower()
    tempo = int(input("Tempo (em meses): "))

    # Converte a taxa anual para mensal equivalente, se necessário
    if tipo_taxa == "anual":
        taxa_mensal = (1 + (taxa_juros / 100)) ** (1 / 12) - 1
    else:
        taxa_mensal = taxa_juros / 100

    montante = capital_inicial
    total_investido = capital_inicial

    print("\n--- Evolução Mês a Mês ---")
    for mes in range(1, tempo + 1):
        # Aplica os juros sobre o saldo atual e soma o aporte do mês
        montante = montante * (1 + taxa_mensal) + aporte_mensal
        total_investido += aporte_mensal
        print(f"Mês {mes:02d}: R$ {montante:,.2f}")

    total_juros = montante - total_investido

    # Exibição dos resultados finais
    print("\n=== Resumo Final ===")
    print(f"Total investido: R$ {total_investido:,.2f}")
    print(f"Total em juros:  R$ {total_juros:,.2f}")
    print(f"Montante final:  R$ {montante:,.2f}")

if __name__ == "__main__":
    calcular_juros_compostos()