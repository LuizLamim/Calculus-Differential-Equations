import numpy as np
from sklearn.neural_network import MLPClassifier

# 1. PREPARAÇÃO DOS DADOS
def gerar_dados_treino(quantidade):
    """
    Gera cores RGB aleatórias e define a resposta correta (0 para Preto, 1 para Branco)
    com base na fórmula de luminância perceptiva humana.
    """
    # Gera 'quantidade' de cores RGB (valores de 0 a 255)
    X = np.random.randint(0, 256, size=(quantidade, 3))
    y = []

    for r, g, b in X:
        # Fórmula de luminância (como o olho humano percebe o brilho)
        luminancia = (0.299 * r + 0.587 * g + 0.114 * b) / 255.0
        
        if luminancia > 0.5:
            y.append(0) # Fundo claro -> Texto Preto
        else:
            y.append(1) # Fundo escuro -> Texto Branco
            
    return X, np.array(y)

print("Gerando dados e treinando a Rede Neural...")

# Geramos 2000 exemplos para a rede estudar
X_treino, y_treino = gerar_dados_treino(2000)

# Normalizamos os dados de RGB (0-255) para valores entre 0 e 1 (facilita para a rede neural)
X_treino = X_treino / 255.0

# 2. CRIAÇÃO E TREINAMENTO DA REDE NEURAL
# Criamos uma rede com 2 camadas ocultas (uma com 8 neurônios e outra com 4 neurônios)
rede_neural = MLPClassifier(hidden_layer_sizes=(8, 4), max_iter=2000, random_state=42)

# O comando 'fit' é onde o aprendizado realmente acontece
rede_neural.fit(X_treino, y_treino)

print("Treinamento concluído!\n")