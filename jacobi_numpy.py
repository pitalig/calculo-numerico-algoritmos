from pprint import pprint

import numpy as np

import constr_matriz


def jacobi(m_h, v_h, n_max, tol):
    # Cria o chute inicial
    x = np.zeros(len(m_h[0]))

    # Cria o vetor d com os elementos da diagonal principal de m_h
    d = np.diag(m_h)
    # Cria o vetor r com os elementos de m_h e diagonal principal nula
    r = m_h - np.diagflat(d)

    # Executa a iteração
    for i in range(n_max):
        x_old = x.copy()
        x = (v_h - np.dot(r, x)) / d
        # Verifica a tolerância
        if np.allclose(x, x_old, tol):
            break
    return x


def v_jacobi(q, r, x, h, n, a_, b_, n_max, tol):
    # Matriz e vetor de termos independentes
    m_h = constr_matriz.constr_matriz(q, x, h, n)
    v_h = constr_matriz.constr_vetor(r, x, h, n, a_, b_)

    # Vetor solução
    return jacobi(m_h, v_h, n_max, tol)


if __name__ == "__main__":
    # TESTE 1
    m_h = np.array([[2.0, 1.0], [5.0, 7.0]])
    v_h = np.array([11.0, 13.0])
    guess = np.array([1.0, 1.0])

    sol = jacobi(m_h, v_h, 25, 0.0001)

    print('m_h:')
    pprint(m_h)

    print('v_h:')
    pprint(v_h)

    print('x:')
    pprint(sol)
