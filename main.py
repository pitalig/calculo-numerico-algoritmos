#!/usr/bin/env
# -*- coding: utf-8 -*-
import os
import sys

import executar


# Opção para encerrar o programa
def finalizar():
    sys.exit()


# Opções do menu
menu = {
    '1': executar.imprime_matriz_vetor,
    '2': executar.solucoes_residuo,
    '3': executar.gauss_plot_erro,
    '4': executar.gauss_plot_erro_log,
    '5': executar.reducao_erro,
    '0': finalizar
}


# Menu
def menu_principal():
    os.system('cls' if os.name == 'nt' else 'clear')

    print('Insira o número da opção desejada')
    print('1 - Imprimir a matriz do sistema e o vetor de termos independentes')
    print('2 - Comparar o resíduo entre as soluções de Gauss e Jacobi')
    print('3 - Exibir o gráfico de erro para a solução de Gauss')
    print('4 - Exibir o gráfico do logaritmo do erro para a solução de Gauss')
    print('5 - Analisar o erro a cada iteração para solução de Jacobi')
    print('\n0 - Sair')
    escolha = input()

    exec_menu(escolha)
    return


# Executar menu
def exec_menu(escolha):
    os.system('cls' if os.name == 'nt' else 'clear')
    escolha = escolha.lower()
    if escolha == '':
        menu_principal()
    else:
        try:
            menu[escolha]()
            print('\n\nInsira 0 para encerrar o programa ou qualquer valor para executar novamente')
            if input() == '0':
                finalizar()
            else:
                menu_principal()
        except KeyError:
            print('Opção inválida, tente novamente.\n')
            menu_principal()
    return


if __name__ == "__main__":
    menu_principal()
