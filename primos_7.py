def eh_primo(numero):
    if numero < 2:
        return False
    # Verifica divisores apenas até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True