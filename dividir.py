def dividir(a, b):
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: Não é possível dividir por zero!"

# Exemplo de uso:
num1 = float(input("Digite o primeiro número: "))