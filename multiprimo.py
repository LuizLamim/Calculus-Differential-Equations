def is_prime(n):
    """Verifica se um número é primo."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def multiply_first_n_primes(n):
    """Encontra os primeiros 'n' números primos e os multiplica."""
    primes = []
    num = 2
    product = 1
    
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
            product *= num
        num += 1
        
    return primes, product