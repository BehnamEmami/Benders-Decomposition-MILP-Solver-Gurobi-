# -*- coding: utf-8 -*-
"""
Jun 12 23:45:51 2024

@author: Behnam
"""



import matplotlib.pyplot as plt
import numpy as np

def plot_bounds(lower_bounds, upper_bounds):
    iters = np.arange(1, len(lower_bounds) + 1)

    plt.figure(figsize=(8, 5))
    plt.plot(iters, upper_bounds, 'o-', label='Upper Bound')
    plt.plot(iters, lower_bounds, 's-', label='Lower Bound')
    plt.fill_between(iters, lower_bounds, upper_bounds, color='gray', alpha=0.2)
    
    plt.title("Benders Decomposition Convergence")
    plt.xlabel("Iteration")
    plt.ylabel("Objective Value")
    plt.xticks(iters)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("convergence.png")
    plt.show()
