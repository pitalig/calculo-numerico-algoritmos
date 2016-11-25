#!/usr/bin/env
# -*- coding: utf-8 -*-
import constr_matriz


def gauss(a, y, n):
    # Escalonar
    for j in range(n):
        if a[j][j] == 0:
            k = j
            while True:
                if 0 == a[k][j]:
                    k += 1
                    if k == n:
                        print("Matriz inválida")
                        break
                else:
                    temp = a[k]
                    a[k] = a[j]
                    a[j] = temp
                    break
        for i in range(j + 1, n):
            m = - a[i][j] / a[j][j]
            for k in range(j, n):
                a[i][k] += m * a[j][k]
            y[i] += m * y[j]
    # print("Matriz escalonada:")
    # print(np.matrix(a))
    # print("Vetor auxiliar após escalonamento:")
    # print(np.matrix(y))
    # Resolver
    x = [None] * n
    for i in range(n-1, -1, -1):
        x[i] = y[i]
        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]
        x[i] = x[i] / a[i][i]
    return x


def v_gauss(q, r, x, h, n, a_, b_):
    # Matriz e vetor de termos independentes
    m_h = constr_matriz.constr_matriz(q, x, h, n)
    v_h = constr_matriz.constr_vetor(r, x, h, n, a_, b_)

    # Vetor solução
    return gauss(m_h, v_h, n - 1)

# ----------------teste----------------
if __name__ == "__main__":
    b = [[1, 2, 3], [4, 5, 8], [7, 8, 5]]
    c = [10, 11, 12]

    print(gauss(b, c, 3))
