import math

def calcular_raiz_da_soma():
    print("--- Calculadora de Raiz da Soma ---")
    
    try:
        # Solicita os dois números ao usuário
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        
        # Soma os números
        soma = num1 + num2
        
        # Calcula a raiz quadrada da soma
        resultado = math.sqrt(soma)
        
        # Exibe o resultado de forma clara
        print(f"\nA soma de {num1} + {num2} é: {soma}")
        print(f"A raiz quadrada de {soma} é: {resultado:.4f}")
        
    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")

# Executa a função
if __name__ == "__main__":
    calcular_raiz_da_soma()