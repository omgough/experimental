import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt

    return mo, np, plt


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Clifford map:**

    > $x_{n+1} = \sin (ay_n) +c\cos(ax_n)$


    > $y_{n+1} = \sin(bx_n) + d\cos(b y_n)$

    - Four constants $a, b, c, d$ shape the whole thing.
    - Classic version is $a = -1.4, b = 1.6, c = 1.0, d = 0.7$.
    - Given a starting point $(x_0,y_0)$, you apply the two lines above over and over, where the output of the last becomes the input of the next.
    - The sequence of points you pass through is the attractor.
    """)
    return


@app.cell
def _(np):
    def clifford(x, y, a, b, c ,d):
        x_next = np.sin(a*y) + c*np.cos(a*x)
        y_next = np.sin(b*x) + d*np.cos(b*y)
        return x_next, y_next    

    return (clifford,)


@app.cell
def _(a_slider, b_slider, c_slider, clifford, d_slider):
    x_1 = 1
    y_1 = 1

    x_values = []
    y_values = []

    # a = -1.4
    # b = 1.6
    # c = 1.0
    # d = 0.7

    a = a_slider.value
    b = b_slider.value
    c = c_slider.value
    d = d_slider.value

    x, y = x_1, y_1
    n_iterations = 1000000

    for i in range(n_iterations):
        x, y = clifford(x, y, a, b, c, d)
        x_values.append(x)
        y_values.append(y)
    return x_values, y_values


@app.cell
def _(plt, x_values, y_values):
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot()
    ax.scatter(x_values, y_values, s=0.1, alpha=0.2, color="navy", edgecolors="none")
    ax.set_aspect("equal")
    ax.axis("off")
    fig
    return


@app.cell
def _(mo):
    a_slider = mo.ui.slider(-3.0, 3.0, step=0.05, value=-1.4, label="a")
    b_slider = mo.ui.slider(-3.0, 3.0, step=0.05, value=1.6, label="b")
    c_slider = mo.ui.slider(-3.0, 3.0, step=0.05, value=1.0, label="c")
    d_slider = mo.ui.slider(-3.0, 3.0, step=0.05, value=0.7, label="d")

    mo.vstack([a_slider, b_slider, c_slider, d_slider])
    return a_slider, b_slider, c_slider, d_slider


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
