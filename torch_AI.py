import torch
import torch.nn as nn
import torch.optim as optim

# Definindo o modelo
model = nn.Linear(1, 1)

# Definindo a função de perda e o otimizador
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)