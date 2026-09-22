import torch
import torch.nn as nn
import torch.optim as optim

# Definindo o modelo
model = nn.Linear(1, 1)

# Definindo a função de perda e o otimizador
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Dados de exemplo fictícios
X = torch.tensor([[1.0], [2.0], [3.0]], dtype=torch.float32)
y = torch.tensor([[2.0], [4.0], [6.0]], dtype=torch.float32)