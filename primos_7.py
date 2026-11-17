def eh_primo(numero):
    if numero < 2:
        return False
    # Verifica divisores apenas até a raiz quadrada do número
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True


primos = []
candidato = 2

# Continua procurando até encontrar 7 números primos
while len(primos) < 7:
    if eh_primo(candidato):
        primos.append(candidato)
    candidato += 1

print("Os 7 primeiros números primos são:", primos)