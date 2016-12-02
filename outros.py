#!/usr/bin/env
# -*- coding: utf-8 -*-
import numpy as np


# Calcula o resíduo entre um solução real e uma solução aproxixmada.
# Entradas: matriz, vetor de termos independentes, vetor solução real
# Retorno: vetor resíduo
def residuo(m, v, v_sol):
    return (np.matrix(v) - np.dot(np.matrix(v_sol), np.matrix(m))).tolist()
