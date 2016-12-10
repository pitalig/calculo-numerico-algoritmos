#!/usr/bin/env
# -*- coding: utf-8 -*-


# Calcula o vetor solução para uma malha de pontos, utilizando a solução conhecida.
# Entradas: Equação diferencial e malha de pontos
# Retorno: vetor solução
def v_sol(y, x):
    v = []
    for i in x:
        v.append(y(i))
    return v

