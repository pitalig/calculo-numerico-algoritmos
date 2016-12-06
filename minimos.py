#!/usr/bin/env
# -*- coding: utf-8 -*-
import gauss


def polin(x, y):
    xk1 = x
    xk2 = [xi**2 for xi in x]
    xk3 = [xi**3 for xi in x]
    xk4 = sum(xi**4 for xi in x)
    xk5 = sum(xi**5 for xi in x)
    xk6 = sum(xi**6 for xi in x)
    fxk1 = sum(y)
    fxk2 = sum([a*b for a, b in zip(xk1, y)])
    fxk3 = sum([a*b for a, b in zip(xk2, y)])
    fxk4 = sum([a*b for a, b in zip(xk3, y)])
    xk1 = sum(xk1.copy())
    xk2 = sum(xk2.copy())
    xk3 = sum(xk3.copy())
    m = [[len(x), xk1, xk2, xk3], [xk1, xk2, xk3, xk4], [xk2, xk3, xk4, xk5], [xk3, xk4, xk5, xk6]]
    v = [fxk1, fxk2, fxk3, fxk4]
    return gauss.v_sol(m, v, 4)


if __name__ == "__main__":
    x = [1, 2, 3]
    y = [10, 11, 12]

    print(polin(x, y))
