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
from dados_test import *

v1 = gauss.v_sol_mh(q, r, x, h, n, a_, b_)

v2 = jacobi_numpy.v_sol_mh(q, r, x, h, n, a_, b_, 1000000, 0.0001)
print('Solução Gauss')
print(v1)
print('Solução Jacobi')
print(v2)
print('Solução real')
print(solve.v_sol(y, x))
print('Resíduo')
print(outros.residuo(construtor.matriz(q, x, h, n), construtor.vetor(r, x, h, n, a_, b_), v2))
erro = gauss.erro_n(y, q, r, a, b, a_, b_)
mmq = list(reversed(minimos.polin(list(range(5, 41, 5)), erro)))
print(mmq)
mmq = np.poly1d(mmq.copy())
x_mmq = list(range(5, 40, 5))
y_mmq = [mmq(xi) for xi in x_mmq]
plt.semilogy(x_mmq, y_mmq)
plt.ylabel('Erro')
plt.xlabel('n')
plt.title('Erro')
plt.show()
