import numpy as np
#first straight

m = 7
b = 1
l = 0.000001 # learning rate

iteracoes = 1000

for i in range(iteracoes):
    Y_pred = m*X + b # valor atual da reta
    derivadam = np.sum(2*X*(Y_pred - y)) # derivada da funcao de custo em relacao a m
    derivadab = np.sum(2*(Y_pred - y)) # derivada em funcao de custo em relacao a b
    m = m + derivadam*L # atualiza m
    b = b + derivadab*L # atualiza b

print(f'valor m: {m}, valor b: {b}')
