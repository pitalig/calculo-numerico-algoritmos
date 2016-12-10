#!/usr/bin/env
# -*- coding: utf-8 -*-
import pprint
import time

import matplotlib.pyplot as plt
import numpy as np

import construtor
import gauss
import jacobi
import minimos
import outros
import solve
from dados import *


# Imprime a matriz e o vetor de termos independentes
def imprime_matriz_vetor():
    n = outros.set_n(a, b)
    print('\n\n---------- MATRIZ ----------')
    pprint.pprint(construtor.matriz(q, n['x'], n['h'], n['n']))

    print('\n\n---------- VETOR DE TERMOS INDEPENDENTES ----------')
    pprint.pprint(construtor.vetor(r, n['x'], n['h'], n['n'], a_, b_))


# Imprime as soluções reais, de Gauss e de Jacobi.
# Imprime o resíduo* das soluções de Gauss e de Jacobi
# Imprime a diferença entre os resíduos calculados
# *Resíduo: para A*x = v -> resíduo = |(A * vetor_solução) - v|
def solucoes_residuo():
    n = outros.set_n(a, b)

    # Inicia o tempo
    start_time = time.time()

    print('\n\n---------- SOLUÇÕES ----------')
    # Soluciona a matriz utilizando a solução real conhecida
    print('\n\n---------- REAL ----------')
    print(solve.v_sol(y, n['x']))

    # Soluciona a matriz pelo método de Gauss
    print('\n\n---------- GAUSS ----------')
    v1 = gauss.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_)
    print(v1)
    # Calcula o resíduo para solução de Gauss
    print('\nRESÍDUO')
    res_gauss = outros.residuo(construtor.matriz(q, n['x'], n['h'], n['n']),
                               construtor.vetor(r, n['x'], n['h'], n['n'], a_, b_),
                               v1)
    print(res_gauss)
    print('\nRESÍDUO MAX')
    print(max(res_gauss))

    # Soluciona a matriz pelo método de Jacobi
    print('\n\n---------- JACOBI ----------')
    n_max = int(input('\nInsira o número máximo de iterações desejado '))
    tol = float(input('\nInsira a tolerância desejada '))
    v2 = jacobi.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_, n_max, tol)
    print(v2)
    # Calcula o resíduo para solução de Jacobi
    print('\nRESÍDUO')
    res_jacobi = outros.residuo(construtor.matriz(q, n['x'], n['h'], n['n']),
                                construtor.vetor(r, n['x'], n['h'], n['n'], a_, b_),
                                v2)
    print(res_jacobi)
    print('\nRESÍDUO MAX')
    print(max(res_jacobi))

    # Compara os resíduos de Gauss e Jacobi
    print('\n\n---------- DIFERENÇA ENTRE RESÍDUOS ----------')
    dif_res = abs(np.array(res_jacobi) - np.array(res_gauss)).tolist()
    print(dif_res)
    print('\nDIFERENÇA MAX')
    print(max(dif_res))

    # Para o contador de tempo e imprime o resultado
    print("\n\n---------- %s SEGUNDOS ----------" % (time.time() - start_time))


# Calcula a solução de Gauss e plota um gráfico do erro
def gauss_plot_erro():
    n_max = 1 + int(input('\nInsira o número máximo de N desejado '))
    passo = int(input('\nInsira o passo desejado '))
    print('\n\n---------- ERRO GAUSS ----------')
    # Calcula o erro_gauss do método de Gauss e plota o gráfico
    erro_gauss = gauss.erro_n(y, q, r, a, b, a_, b_, n_max, passo)
    n_erro_gauss = range(5, n_max, passo)
    plt.semilogy(n_erro_gauss, erro_gauss, 'ko', label='Erro máximo')

    # Calcula e imprime o polinomio interpolador pelo método de mínimos quadrados
    mmq = minimos.polin(n_erro_gauss, erro_gauss)
    print('CONSTANTES MÍNIMOS QUADRADOS')
    print(mmq[1])

    # Plota o gráfico do polinomio interpolador
    x_mmq = list(np.arange(n_erro_gauss[0], n_erro_gauss[-1], 0.1))
    y_mmq = [mmq[0](xi) for xi in x_mmq]
    nome = '{:.5e}/n + {:.5f}/n² + {:.5f}/n³'.format(mmq[1][0], mmq[1][1], mmq[1][2])
    plt.semilogy(x_mmq, y_mmq, label=nome)
    plt.title('Valores máximos de erro - método de Gauss')
    plt.xlabel('n')
    plt.ylabel('Erro')
    plt.legend()
    plt.show()


# Calcula a solução de Gauss e plota um gráfico do logarítmo erro
def gauss_plot_erro_log():
    n_max = 1 + int(input('\nInsira o número máximo de N desejado '))
    passo = int(input('\nInsira o passo desejado '))
    print('\n\n---------- ERRO GAUSS LOG ----------')
    # Calcula o erro_gauss do método de Gauss
    erro_gauss = gauss.erro_n(y, q, r, a, b, a_, b_, n_max, passo)
    n_erro_gauss = range(5, n_max, passo)

    # Calcula o logaritmo do erro e de n e plota o gráfico
    erro_log = [math.log10(xi) for xi in erro_gauss]
    n_log = [math.log10(xi) for xi in n_erro_gauss]
    plt.plot(n_log, erro_log, 'ko', label='Erro máximo')

    # Calcula e imprime o polinomio interpolador pelo método de mínimos quadrados para o log
    mmq_log = minimos.polin_numpy(n_log, erro_log, 1)
    print('CONSTANTES MÍNIMOS QUADRADOS')
    print(mmq_log[1])

    # Plota o gráfico do polinomio interpolador
    x_mmq_log = list(np.arange(n_log[0], n_log[-1], 0.1))
    y_mmq_log = [mmq_log[0](xi) for xi in x_mmq_log]
    nome = '{:.5f}n + {:.5f}'.format(mmq_log[1][0], mmq_log[1][1])
    plt.plot(x_mmq_log, y_mmq_log, label=nome)
    plt.title('Logaritmo dos valores máximos de erro - método de Gauss')
    plt.xlabel('log10(n)')
    plt.ylabel('log10(Erro)')
    plt.legend()
    plt.show()


# Imprime a taxa de redução do erro entre a solução de Jacobi e Gauss para cada iteração.
def reducao_erro():
    n = outros.set_n(a, b)
    v_gauss = np.array(gauss.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_))
    erro = []
    taxa = []
    v2 = max(abs((np.array(jacobi.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_, 1, 0, False)) - v_gauss)).tolist())
    for i in range(2, 50):
        v1 = v2
        v2 = max(abs((np.array(jacobi.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_, i, 0, False)) - v_gauss)).tolist())
        erro.append(v2)
        taxa.append(1 - (v2 / v1))
    print('\n\nERRO A CADA ITERAÇÃO')
    print(erro)
    print('\n\nTAXA DE REDUÇÃO A CADA ITERAÇÃO')
    print(taxa)
    print('\n\nTAXA DE REDUÇÃO MÉDIA')
    print(sum(taxa) / len(taxa))


if __name__ == "__main__":
    reducao_erro()
