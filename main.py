#!/usr/bin/env
# -*- coding: utf-8 -*-
import time

import matplotlib.pyplot as plt
import numpy as np

import construtor
import gauss
import jacobi_numpy
import minimos
import outros
import solve
from dados import *

start_time = time.time()

# Soluciona a matriz utilizando a solução real conhecida
print('\n\n---------- REAL ----------')
print(solve.v_sol(y, x))

# Soluciona a matriz pelo método de Gauss
print('\n\n---------- GAUSS ----------')
v1 = gauss.v_sol_mh(q, r, x, h, n, a_, b_)
# print(v1)
# Calcula o resíduo para solução de Gauss
# print('RESÍDUO')
res_gauss = outros.residuo(construtor.matriz(q, x, h, n), construtor.vetor(r, x, h, n, a_, b_), v1)
# print(res_gauss)
print('RESÍDUO MAX')
print(max(res_gauss))

# Soluciona a matriz pelo método de Jacobi
print('\n\n---------- JACOBI ----------')
v2 = jacobi_numpy.v_sol_mh(q, r, x, h, n, a_, b_, 10, 0)
# print(v2)
# Calcula o resíduo para solução de Jacobi
# print('RESÍDUO')
res_jacobi = outros.residuo(construtor.matriz(q, x, h, n), construtor.vetor(r, x, h, n, a_, b_), v2)
# print(res_jacobi)
print('RESÍDUO MAX')
print(max(res_jacobi))

# Compara os resíduos de Gauss e Jacobi
print('\n\n---------- COMPARAÇÃO RESÍDUOS ----------')
dif_res = abs(np.array(res_jacobi) - np.array(res_gauss)).tolist()
# print(dif_res)
print('DIFERENÇA MAX')
print(max(dif_res))

print('\n\n---------- COMPARAÇÃO RESÍDUOS ----------')
# Calcula o erro_gauss do método de Gauss e plota o gráfico
erro_gauss = gauss.erro_n(y, q, r, a, b, a_, b_, 40)
# print(erro_gauss)
plt.semilogy(range(5, 41, 5), erro_gauss, 'ko')

# Calcula e imprime o polinomio interpolador pelo método de mínimos quadrados
mmq = minimos.polin(range(5, 41, 5), erro_gauss)
print(mmq[1])

# Plota o gráfico do polinomio interpolador
x_mmq = list(np.arange(5, 40, 0.1))
y_mmq = [mmq[0](xi) for xi in x_mmq]
plt.semilogy(x_mmq, y_mmq)
plt.show()

print("\n\n---------- %s SEGUNDOS ----------" % (time.time() - start_time))
