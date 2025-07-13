# -*- coding: utf-8 -*-
"""
Jun 12 23:45:51 2024

@author: Behnam
"""

from benders import SimpleBenders
from plotter import plot_bounds

def main():
    # Initialize and solve the Benders decomposition MILP
    benders_solver = SimpleBenders()
    benders_solver.run()

    # Plot the convergence (LB and UB over iterations)
    plot_bounds(benders_solver.lower_bounds_list, benders_solver.upper_bounds_list)

if __name__ == "__main__":
    main()