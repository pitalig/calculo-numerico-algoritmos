#!/usr/bin/env
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np

import construtor
import gauss
import jacobi_numpy
import minimos
import outros
import solve
# Importa os dados do problema do arquivo desejado
from dados_test import *

# Soluciona a matriz pelo método de Gauss
v1 = gauss.v_sol_mh(q, r, x, h, n, a_, b_)
print('Solução Gauss')
print(v1)

# Soluciona a matriz pelo método de Jacobi
v2 = jacobi_numpy.v_sol_mh(q, r, x, h, n, a_, b_, 1000000, 0.0001)
print('Solução Jacobi')
print(v2)

# Soluciona a matriz utilizando a solução real conhecida
print('Solução real')
print(solve.v_sol(y, x))

# Calcula o resíduo para solução de Jacobi
print('Resíduo')
print(outros.residuo(construtor.matriz(q, x, h, n), construtor.vetor(r, x, h, n, a_, b_), v2))

# Calcula o erro do método de Gauss e plota o gráfico
erro = gauss.erro_n(y, q, r, a, b, a_, b_, 40)
print(erro)
plt.semilogy(range(5, 41, 5), erro, 'ko')

# Calcula e imprime o polinomio interpolador pelo método de mínimos quadrados
mmq = np.poly1d(minimos.polin_numpy(list(range(5, 41, 5)), erro, 7))
print(mmq)

# Plota o gráfico do polinomio interpolador
x_mmq = list(np.arange(5, 40, 0.1))
y_mmq = [abs(mmq(xi)) for xi in x_mmq]
plt.semilogy(x_mmq, y_mmq)
plt.show()
