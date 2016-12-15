#!/usr/bin/env
# -*- coding: utf-8 -*-
# Módulo executar: responsável pela execução principal do programa
# Utiliza todos os outros módulos desenvolvidos e expoe de forma agradável os resultados

# Importa as bibliotecas extras utilizadas
import pprint
import time

import matplotlib.pyplot as plt
import numpy as np

import bisseccao
import construtor
import gauss
import jacobi
import lagrange
import minimos
import newton
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


# Imprime as soluções real, de Gauss e de Jacobi.
# Imprime o resíduo* das soluções de Gauss e de Jacobi
# Imprime a diferença entre os resíduos calculados
# *Resíduo: para A*x = b -> resíduo = |(A * vetor_solução) - b|
def solucoes_residuo():
    n = outros.set_n(a, b)
    prin = int(input('Exibir resultados detalhados? (0 - não / 1 - sim) '))

    print('\n---------- SOLUÇÕES ----------')
    # Soluciona a matriz utilizando a solução real conhecida
    if prin == 1:
        print('\n-------------------- REAL --------------------')
        print(solve.v_sol(y, n['x']))

    # Soluciona a matriz pelo método de Gauss
    print('\n-------------------- GAUSS --------------------')

    start_time = time.time()

    v1 = gauss.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_)
    if prin == 1:
        print(v1)
    # Calcula o resíduo para solução de Gauss
    res_gauss = outros.residuo(construtor.matriz(q, n['x'], n['h'], n['n']),
                               construtor.vetor(r, n['x'], n['h'], n['n'], a_, b_),
                               v1)
    if prin == 1:
        print('\nRESÍDUO')
        print(res_gauss)
    print('\nRESÍDUO MAX')
    print(max(res_gauss))
    print("\n---------- {:.06f} S ----------".format(abs(start_time - time.time())))

    # Soluciona a matriz pelo método de Jacobi
    print('\n-------------------- JACOBI --------------------')
    n_max = int(input('\nInsira o número máximo de iterações desejado '))
    tol = float(input('Insira a tolerância desejada '))
    start_time = time.time()
    v2 = jacobi.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_, n_max, tol)
    if prin == 1:
        print(v2)
    # Calcula o resíduo para solução de Jacobi
    res_jacobi = outros.residuo(construtor.matriz(q, n['x'], n['h'], n['n']),
                                construtor.vetor(r, n['x'], n['h'], n['n'], a_, b_),
                                v2)
    if prin == 1:
        print('\nRESÍDUO')
        print(res_jacobi)
    print('\nRESÍDUO MAX')
    print(max(res_jacobi))
    print("\n---------- {:.06f} S ----------".format(abs(start_time - time.time())))

    # Compara os resíduos de Gauss e Jacobi
    print('\n-------------------- DIFERENÇA ENTRE RESÍDUOS --------------------')
    dif_res = abs(np.array(res_jacobi) - np.array(res_gauss)).tolist()
    if prin == 1:
        print(dif_res)
    print('\nDIFERENÇA MAX')
    print(max(dif_res))


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


# Determina o valor de n necessário para atingir determinado erro
def determina_n():
    # Calcula o erro_gauss do método de Gauss
    erro_gauss = gauss.erro_n(y, q, r, a, b, a_, b_, 41, 5)
    n_erro_gauss = range(5, 41, 5)

    # Calcula e imprime o polinomio interpolador pelo método de mínimos quadrados
    mmq = minimos.polin(n_erro_gauss, erro_gauss)
    print('CONSTANTES POLINÔMIO OBTIDO POR MÍNIMOS QUADRADOS')
    print(mmq[1])

    # Le o erro desejado
    erro_desejado = float(input('Insira o erro desejado '))

    def mmq_erro(x):
        return mmq[0](x) - erro_desejado

    def mmq_erro_deriv(x):
        return - (mmq[1][0] * (x ** 2) + 2 * mmq[1][1] * x + 3 * mmq[1][2]) / x ** 4

    # Resolução por Bissecção
    start_time = time.time()
    n_erro = bisseccao.bissec(mmq_erro, 1, 500, 0.1, 0)
    total_time = abs(start_time - time.time())
    print('--------------- Utlizando Bissecção ---------------')
    print('Para garantir um erro inferior a {:.0e} é necessário n={:.0f}'.format(erro_desejado, n_erro[0]))
    print('Número de iterações: {}'.format(n_erro[1]))
    print('Tempo consumido: {:.6f} segundos'.format(total_time))

    # Resolução por Newton
    start_time = time.time()
    n_erro = newton.newton(mmq_erro, mmq_erro_deriv, 10, 1000, 0.1)
    total_time = abs(start_time - time.time())
    print('--------------- Utlizando Newton ---------------')
    print('Para garantir um erro inferior a {:.0e} é necessário n={:.0f}'.format(erro_desejado, n_erro[0]))
    print('Número de iterações: {}'.format(n_erro[1]))
    print('Tempo consumido: {:.6f} segundos'.format(total_time))


# Imprime a taxa de redução do erro entre a solução de Jacobi e Gauss para cada iteração.
def reducao_erro():
    # Define o valor de N e calcula a solução de Gauss para o N determinado
    n = outros.set_n(a, b)
    v_gauss = np.array(gauss.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_))
    # Cria dois vetores vazios, para armazenar os valores do erro e a taxa
    erro = []
    taxa = []
    # Calcula a solução de Jacobi para n_max=1
    # Calcula o erro (módulo da diferença entre o vetor solução de Gauss e Jacobi)
    # v2 recebe apenas o valor máximo do erro.
    v2 = max(abs((np.array(jacobi.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_, 1, 0, False)) - v_gauss)).tolist())
    for i in range(2, 50):
        v1 = v2
        # Calcula a solução de Jacobi para n_max=i
        # Calcula o erro (módulo da diferença entre o vetor solução de Gauss e Jacobi)
        # v2 recebe apenas o valor máximo do erro.
        v2 = max(abs((np.array(jacobi.v_sol_mh(q, r, n['x'], n['h'], n['n'], a_, b_, i, 0, False)) - v_gauss)).tolist())
        # Adiciona o erro máximo ao vetor erro.
        erro.append(v2)
        # Adiciona a taxa (1 - ((erro n_max=i-1)/(erro n_max=i)) ao vetor taxa
        taxa.append(1 - (v2 / v1))
    print('\n\nERRO A CADA ITERAÇÃO')
    print(erro)
    print('\n\nTAXA DE REDUÇÃO A CADA ITERAÇÃO')
    print(taxa)
    print('\n\nTAXA DE REDUÇÃO MÉDIA')
    print(sum(taxa) / len(taxa))


# Plota o gráfico da solução de lagrange e da solução real
def interpolador_lagrange():
    # Define o grau do polinomio e o intervalo a ser plotado no gráfico
    grau = 1 + int(input('Insira o grau do polinômio interpolador: '))
    intervalo = float(input('Insira o tamanho da área a ser analisada: '))
    # Define o intervalo de x
    x_ = np.linspace(0, intervalo, grau).tolist()
    # Calcula a solução real para o intervalo
    y_ = solve.v_sol(y, x_)
    # Calcula a solução do polinomio no intervalo
    polinomio = lagrange.pol_interpola(x_, y_)
    x_plot = np.arange(0, intervalo, 0.1)
    y_plot = solve.v_sol(y, x_plot)
    y_plot2 = [polinomio(x_i) for x_i in x_plot]
    # Plota os resultados
    plt.plot(x_, y_, 'ko', label='Pontos de referência')
    plt.plot(x_plot, y_plot, label='Solução real')
    plt.plot(x_plot, y_plot2, label='Solução Lagrange')
    plt.title('Interpolador de Lagrange')
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.legend(loc=2)
    plt.show()


# Teste
if __name__ == "__main__":
    solucoes_residuo()
