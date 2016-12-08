import matplotlib.pyplot as plt

import gauss

x = [1, 2, 3]
teste = [0.1, 0.2, 0.3]


def f_1(x):
    return 1 / x


def f_2(x):
    return 1 / x ** 2


def f_3(x):
    return 1 / x ** 3


m = len(x)
n = 3

aux = [[0] * 3] * 3

for i in range(n):
    aux[i][0] = f_1(x[i])
    aux[i][1] = f_2(x[i])
    aux[i][2] = f_3(x[i])

m = [[0.0] * 3] * 3
w = [0.0] * 3

for i in range(n):
    for j in range(n):
        for k in range(n):
            m[i][j] += aux[k][i] * aux[k][j]
    for k in range(n):
        w[i] += aux[k][i] * teste[k]

p = gauss.v_sol(m, w, 3)


def erro(x):
    return p[1] / x + p[2] / x ** 2 + p[3] / x ** 3


plt.plot(erro(x))
