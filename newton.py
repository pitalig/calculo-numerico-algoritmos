#!/usr/bin/env python
# encoding: utf-8

def newton(f, derivF, x_0, n_max, prec):
    Iter = [("NumIter", "iter", "new iter", "f(new iter)", "controle")]
    i = 1
    x_k = x_0
    while f(x_k - prec) * f(x_k + prec) > 0 and i < n_max:
        temp = x_k - f(x_k) / derivF(x_k)
        linha = (i, x_k, temp, f(temp), f(x_k - prec) * f(x_k + prec))
        x_k = temp
        Iter.append(linha)
        i += 1
    temp = x_k - f(x_k) / derivF(x_k)
    linha = (i, x_k, temp, f(temp), f(x_k - prec) * f(x_k + prec))
    Iter.append(linha)

    ########################################################################################

    # # Exemplo 1
    #
    # f = function(x)
    # {
    #   return(3*x^3-2*x^2+3*x-2)
    # }
    #
    # derivF = function(x)
    # {
    #   return(9*x^2-4*x+3)
    # }
    #
    # prec = 10^-8
    # n_max = 1000
    # m = -1
    # M = 1
    # x_0 = M
    # x_1 = M+5
    # NewMet(f,derivF,M,n_max, prec)
    # SecMet(f,x_0,x_1,n_max, prec)
    #
    # ########################################################################################
    #
    #
    #
    # # Exemplo 2
    #
    # f = function(x)
    # {
    #   return(sin(x)+2*cos(x))
    # }
    #
    # derivF = function(x)
    # {
    #   return(cos(x)-2*sin(x))
    # }
    #
    # prec = 10^-13
    # n_max = 1000
    # m = 2
    # M = 3
    # x_0 = M
    # x_1 = M+0.1
    # NewMet(f,derivF,M,n_max, prec)
    # SecMet(f,x_0,x_1,n_max, prec)
