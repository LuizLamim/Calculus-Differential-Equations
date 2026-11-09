def calcular_velocidade_media(distancia, tempo):
    """Calcula a velocidade média dada a distância e o tempo."""
    if tempo <= 0:
        return "Erro: O tempo deve ser maior que zero."
    
    velocidade = distancia / tempo
    return velocidade