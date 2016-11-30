from pprint import pprint

import numpy as np

import construtor


# Calcula o vetor solução pelo método de Jacobi.
# Entradas: matriz, vetor de termos independentes, número máximo de iterações, tolerância
# Retorno: vetor solução
def v_sol(m, v, n_max, tol):
    # Cria o chute inicial
    x = np.zeros(len(m[0]))

    # Cria o vetor d com os elementos da diagonal principal de m
    d = np.diag(m)
    # Cria o vetor r com os elementos de m e diagonal principal nula
    r = m - np.diagflat(d)

    # Executa a iteração
    for i in range(n_max):
        x_old = x.copy()
        x = (v - np.dot(r, x)) / d
        # Verifica a tolerância
        if np.allclose(x, x_old, tol):
            break
    # Retorna o vetor solução
    return x


# Calcula o vetor solução, para a matriz de uma equação, pelo método de Jacobi.
# Entradas: q(x), r(x), malha de pontos, passo, número de pontos, y(a), y(b), número máximo de iterações, tolerância
# Retorno: vetor solução
def v_sol_mh(q, r, x, h, n, a_, b_, n_max, tol):
    # Calcula a matriz e o vetor de termos independentes
    m_h = construtor.matriz(q, x, h, n)
    v_h = construtor.vetor(r, x, h, n, a_, b_)

    # Calcula e retorna o vetor solução
    return v_sol(m_h, v_h, n_max, tol)


if __name__ == "__main__":
    # TESTE 1
    m = np.array([[2.0, 1.0], [5.0, 7.0]])
    v = np.array([11.0, 13.0])
    guess = np.array([1.0, 1.0])

    sol = v_sol(m, v, 25, 0.0001)

    print('m:')
    pprint(m)

    print('v:')
    pprint(v)

    print('x:')
    pprint(sol)
