import numpy as np
from euler_explicite import euler_explicite

def schema(sigma, L, f, h, tau, K):

    n = int(round(L / h))
    x_int = np.linspace(h, L - h, n-1)

    U0 = f(x_int)

    mu = sigma * tau / h**2

    def F(t, U):
        U_new = np.empty_like(U)
        U_new[0] = U[0] + mu*(U[1] - 2*U[0] + 0)
        for j in range(1, n-2):
            U_new[j] = U[j] + mu*(U[j+1] - 2*U[j] + U[j-1])
        U_new[-1] = U[-1] + mu*(0 - 2*U[-1] + U[-2])
        return (U_new - U) / tau

    t0 = 0.0
    tf = K * tau
    t_vals, W = euler_explicite(F, t0, U0, tau, tf)

    return W