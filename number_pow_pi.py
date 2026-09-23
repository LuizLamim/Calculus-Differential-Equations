import math

def calcular_potencia_pi():
    print("--- Calculadora de Número Elevado a Pi ---")

    try:
        # Pede para o usuário digitar um número
        numero = float(input("Digite um número: "))
        
        # Realiza a operação (número elevado a pi)
        resultado = numero ** math.pi
        
        # Mostra o resultado formatado
        print(f"\n{numero} elevado a pi (aprox. {math.pi:.4f}) é igual a:")
        print(f"-> {resultado}")

        except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")