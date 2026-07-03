import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    from scipy.integrate import solve_ivp

    return mo, np, plt, solve_ivp


@app.function
def lorenz(t, state, sigma=10.0, rho=28.0, beta=8.0/3.0):
    x, y, z = state
    dx = sigma * (y-x)
    dy = x * (rho-z)-y
    dz = x * y - beta * z
    return [dx, dy, dz]


@app.cell
def _(np):
    initial_state = [1.0, 1.0, 1.0]
    t_span = (0.0, 40.0)
    t_eval = np.linspace(t_span[0], t_span[1], 10000)
    return initial_state, t_eval, t_span


@app.cell
def _(initial_state, rho_slider, solve_ivp, t_eval, t_span):
    sol = solve_ivp(lorenz, 
                    t_span, 
                    initial_state, 
                    t_eval=t_eval,
                   args=(10.0, rho_slider.value, 8.0/3.0))
    return (sol,)


@app.cell
def _(sol):
    sol.y.shape
    return


@app.cell
def _(sol):
    sol.y[0][:5]
    return


@app.cell
def _(plt, sol):
    fig = plt.figure()
    ax = fig.add_subplot(projection="3d")
    ax.plot(sol.y[0], sol.y[1], sol.y[2], linewidth = 0.5)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z")
    fig
    return


@app.cell
def _(mo):
    rho_slider = mo.ui.slider(start = 0.0, 
                              stop = 50.0, 
                              step = 0.5, 
                              value = 28.0, 
                              label = "rho")

    rho_slider
    return (rho_slider,)


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
