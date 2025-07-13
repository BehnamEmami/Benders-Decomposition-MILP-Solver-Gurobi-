# Benders-Decomposition-MILP-Solver-Gurobi-
This project implements a simple Benders decomposition algorithm to solve a mixed-integer linear programming (MILP) problem using the Gurobi optimization solver. The decomposition splits continuous and integer decision variables and solves a master-subproblem iteratively.

---

## 📌 Problem Formulation

The problem is formulated as:

```
minimize    -4x - 3y - 5z
subject to
            -2x - 3y - z  ≥ -12
            -2x -  y - 3z ≥ -12
            -z           ≥ -20
            x, y         ≥ 0
            z ∈ ℤ₊
```

This MILP is solved using Benders decomposition where `x` and `y` are continuous (first-stage), and `z` is an integer variable (second-stage or complicating variable).

---

## 📁 File Structure

```
benders/
├── benders.py       # Main Benders decomposition logic using Gurobi
├── main.py          # Entry point: runs the Benders solver and plots convergence
├── plotter.py       # Contains matplotlib code to plot convergence of bounds
├── convergence_plot.png  # Saved plot image after execution (optional)
```

---

## 🚀 Getting Started

### 1. **Install Dependencies**

You'll need:

- Python ≥ 3.7
- [Gurobi](https://www.gurobi.com/) (with a valid license)
- `matplotlib`
- `numpy`

```bash
pip install matplotlib numpy gurobipy
```

> 💡 Note: Gurobi requires a license. Free academic licenses are available on their [website](https://www.gurobi.com/academia/academic-program-and-licenses/).

---

### 2. **Run the Solver**

From the command line or a Python IDE (e.g., Spyder, VS Code):

```bash
python main.py
```

The solver will output each iteration's lower and upper bounds and generate a convergence plot.

---

## 📈 Example Output

```
Iter 0: LB=-36.000, UB=-20.000, z=0.0
Iter 1: LB=-28.000, UB=-24.000, z=2.0
Iter 2: LB=-24.000, UB=-24.000, z=0.0
```

A plot showing the convergence of the lower and upper bounds over iterations is also generated.

---

## 📊 Output Plot

The convergence plot will be saved as `convergence_plot.png` in the project directory.

---

## 🤝 Acknowledgements

- This implementation uses Gurobi's Python interface for high-performance optimization.
- Designed for educational and demonstration purposes to show how Benders decomposition works on small MILPs.

---

## 🧑‍💻 Author

Behnam Emami  
[b.demami91@gmail.com]

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).
