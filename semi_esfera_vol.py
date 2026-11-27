import math

def calcular_volume_semiesfera(raio: float) -> float:
    """Calcula o volume de uma semiesfera dado o seu raio."""
    if raio < 0:
        raise ValueError("O raio não pode ser um valor negativo.")

    volume = (2 / 3) * math.pi * (raio**3)
    return volume

def main():