import numpy as np
import matplotlib.pyplot as plt
from schema import schema


def fonc():

    sigma = 1.0
    L = 1.0
    h = 1/10
    f = lambda x: np.sin(np.pi * x)
    for tau in [0.001, 0.01]:
        K = int(1.0 / tau)
        W = schema(sigma, L, f, h, tau, K)

        n = int(round(L / h))
        x = np.linspace(0, L, n+1)

        t_indices = [
            0,
            int(0.05 / tau),
            int(0.1  / tau),
            int(1.0  / tau)
        ]

        plt.figure()

        for idx in t_indices:
            t = idx * tau
            u = np.zeros(n+1)
            u[1:-1] = W[:, idx]
            plt.plot(x, u, label=f"approx et t={t:g}")

        for idx in t_indices:
            t = idx * tau
            u_ex = np.exp(-np.pi**2 * t) * np.sin(np.pi * x)
            plt.plot(x, u_ex, label=f"exa et t={t:g}")

        plt.xlabel("x")
        plt.ylabel("u")
        plt.title(f"Température pour tau={tau}")
        if tau <= 0.005:
            plt.ylim(0, 1)
        plt.legend()

    plt.show()

if __name__ == "__fonc__":
    fonc()