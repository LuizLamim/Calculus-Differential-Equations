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