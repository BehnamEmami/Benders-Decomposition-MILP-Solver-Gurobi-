# -*- coding: utf-8 -*-
"""
Jun 12 23:45:51 2024

@author: Behnam
"""

from gurobipy import Model, GRB, quicksum
import numpy as np

class SimpleBenders:
    def __init__(self):
        # Problem size
        self.Nx = 2  # x and y
        self.Nz = 1  # z
        self.m = 2   # constraints involving x, z
        self.n = 1   # constraints on z

        # Coefficients
        self.c = np.array([-4, -3]).reshape((self.Nx, 1))
        self.f = np.array([-5]).reshape((self.Nz, 1))
        self.A = np.array([[-2, -3], [-2, -1]])
        self.B = np.array([[-1], [-3]])
        self.b = np.array([-12, -12]).reshape((self.m, 1))
        self.D = np.array([[-1]])
        self.d = np.array([-20]).reshape((self.n, 1))

        self.z_init = np.array([[4]])  # initial feasible z

        self.eps = 1e-3
        self.max_iter = 20
        self.UB = GRB.INFINITY
        self.LB = -GRB.INFINITY

        self.optimality_cuts = []
        self.feasibility_cuts = []
        self.upper_bounds_list = []
        self.lower_bounds_list = []

    def solve_subproblem(self, z_val):
        model = Model()
        model.setParam("OutputFlag", 0)
        p = model.addVars(self.m, lb=0.0, name="p")
        expr = quicksum(p[i] * (self.b[i, 0] - self.B[i, 0] * z_val[0, 0]) for i in range(self.m))
        model.setObjective(expr, GRB.MAXIMIZE)

        for j in range(self.Nx):
            model.addConstr(quicksum(p[i] * self.A[i, j] for i in range(self.m)) <= self.c[j, 0])

        model.optimize()
        if model.Status == GRB.OPTIMAL:
            duals = np.array([p[i].X for i in range(self.m)]).reshape((self.m, 1))
            return duals, model.ObjVal, True
        else:
            return None, None, False

    def solve_master_problem(self):
        model = Model()
        model.setParam("OutputFlag", 0)

        z = model.addVar(vtype=GRB.INTEGER, lb=0.0, name="z")
        n = model.addVar(lb=-GRB.INFINITY, name="n")

        model.setObjective(self.f[0, 0] * z + n, GRB.MINIMIZE)
        model.addConstr(self.D[0, 0] * z >= self.d[0, 0])  # Dz >= d

        for p in self.optimality_cuts:
            expr = quicksum(p[i, 0] * (self.b[i, 0] - self.B[i, 0] * z) for i in range(self.m))
            model.addConstr(n >= expr)

        for r in self.feasibility_cuts:
            expr = quicksum(r[i, 0] * (self.b[i, 0] - self.B[i, 0] * z) for i in range(self.m))
            model.addConstr(expr <= 0)

        model.optimize()
        return np.array([[z.X]]), model.ObjVal

    def run(self):
        z = self.z_init
        i = 0

        while abs((self.UB - self.LB)/self.UB) > self.eps and i < self.max_iter:
            duals, val, is_opt = self.solve_subproblem(z)

            if is_opt:
                self.optimality_cuts.append(duals)
                self.UB = min(self.UB, float(self.f.T @ z + val))
            else:
                # (Optional) implement feasibility cut if needed
                pass

            z, lb = self.solve_master_problem()
            self.LB = lb
            self.upper_bounds_list.append(float(self.UB))
            self.lower_bounds_list.append(float(self.LB))
            print(f"Iter {i}: LB={self.LB:.3f}, UB={self.UB:.3f}, z={z.flatten()[0]}")
            i += 1

        print("\nDone.")


