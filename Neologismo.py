import random

def gerar_neologismo():
    # Listas de sons consonantais e vogais
    consoantes_inicio = ['b', 'c', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'z', 'bl', 'cl', 'fl', 'gl', 'pl', 'pr', 'tr', 'vr', 'ch', 'nh', 'lh']
    vogais = ['a', 'e', 'i', 'o', 'u', 'ae', 'ai', 'au', 'ea', 'ei', 'ia', 'io', 'ou']
    consoantes_meio = ['b', 'c', 'd', 'f', 'g', 'j', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'x', 'z', 'nt', 'nd', 'mp', 'st', 'xt', 'lt']
    terminacoes = ['ar', 'er', 'ir', 'izar', 'ificar', 'ada', 'ido', 'ância', 'ência', 'ópolis', 'verso', 'ium', 'al', 'el', 'il', 'ura']

    # Monta a estrutura da palavra de forma aleatória
    inicio = random.choice(consoantes_inicio)
    vogal1 = random.choice(vogais)
    
    # Decide se a palavra terá um som intermediário ou vai direto para o final
    if random.random() > 0.4:
        meio = random.choice(consoantes_meio)
        vogal2 = random.choice(vogais)
        fim = random.choice(terminacoes)
        palavra = f"{inicio}{vogal1}{meio}{vogal2}{fim}"
    else:
        fim = random.choice(terminacoes)
        palavra = f"{inicio}{vogal1}{fim}"
        
    return palavra.capitalize()

def gerar_lote():
    print("✨ Gerando 5 novos neologismos...")
    print("-" * 30)
    # Garante que não venham palavras repetidas no mesmo lote
    palavras = set()
    while len(palavras) < 5:
        palavras.add(gerar_neologismo())
        
    for i, p in enumerate(palavras, 1):
        print(f"{i}. {p}")
    print("-" * 30)

if __name__ == "__main__":
    while True:
        gerar_lote()
        resposta = input("\nPressiona Enter para gerar mais 5 ou digite 'sair' para encerrar: ").strip().lower()
        if resposta == 'sair':
            print("Até logo!")
            break