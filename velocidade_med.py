def calcular_velocidade_media(distancia, tempo):
    """Calcula a velocidade média dada a distância e o tempo."""
    if tempo <= 0:
        return "Erro: O tempo deve ser maior que zero."
    
    velocidade = distancia / tempo
    return velocidade

    try:
        distancia = float(input("Digite a distância percorrida (ex: km ou metros): "))
    tempo = float(input("Digite o tempo gasto (ex: horas ou segundos): "))
    
    resultado = calcular_velocidade_media(distancia, tempo)
    
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"\nA velocidade média é de {resultado:.2f}")

    except ValueError: