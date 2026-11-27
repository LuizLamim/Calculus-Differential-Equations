def calcular_juros_compostos():
    print("=== Calculadora de Juros Compostos ===")

    # Entrada de dados
    capital_inicial = float(input("Valor inicial (R$): "))
    aporte_mensal = float(input("Aporte mensal (R$) [digite 0 se não houver]: "))
    taxa_juros = float(input("Taxa de juros (%): "))
    tipo_taxa = input("A taxa é 'mensal' ou 'anual'? ").strip().lower()
    tempo = int(input("Tempo (em meses): "))