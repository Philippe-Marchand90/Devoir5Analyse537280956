import numpy as np
import euler_explicite as euler_explicite

def schema(sigma, L, f, h, tau, K):

    n = int(round(L/H))
    x_int = np.linspace(h, L-h, n-1)

    U0 = f(x_int)

    mu = sigma*tau / h**2

    def F(t, U):
        UN = np.empty_like(U)
        UN[0] = U[0] + mu*(U[1] - 2*U[0] + 0)
        
