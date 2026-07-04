import marimo

__generated_with = "0.23.13"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    from matplotlib.colors import LogNorm, LinearSegmentedColormap

    return mo, mpl, np, plt


@app.cell
def _(np):
    def attractor(x, y, a, b):
        x_next = np.sin(x**2 - y**2 + a)
        y_next = np.cos(2*x*y + b)
        return x_next, y_next

    return (attractor,)


@app.cell
def _(a_slider, attractor, b_slider):
    x_1 = 1
    y_1 = 1
    a = a_slider.value
    b = b_slider.value

    x_values = []
    y_values = []

    x, y = x_1, y_1
    n_iterations = 1000000

    for i in range(n_iterations):
        x, y = attractor(x, y, a, b)
        x_values.append(x)
        y_values.append(y)
    return a, b, x_values, y_values


@app.cell
def _(a, b, mpl, plt, x_values, y_values):
    mpl.rcParams["mathtext.fontset"] = "stix"   # Cambria-like serif math
    SITE_BG = "#fcfbf7"
    fig = plt.figure(figsize=(8, 8))
    fig.patch.set_facecolor(SITE_BG)
    ax = fig.add_subplot()
    ax.set_facecolor(SITE_BG)
    ax.scatter(x_values, y_values, s=0.1, alpha=0.2, color="#2f57bf", edgecolors="none")
    ax.set_aspect("equal")
    ax.axis("off")

    # equations + live parameter values, top-left, baked into the image
    label = (
        r"$x_{n+1} = \sin(x_n^2 - y_n^2 + a)$" "\n"
        r"$y_{n+1} = \cos(2 x_n y_n + b)$" "\n"
        rf"$a = {a:.2f}, \; b = {b:.2f}$"
    )
    fig.text(
        0.03, 0.97, label,
        ha="left", va="top",
        fontsize=12, color="black",
        linespacing=1.6,
    )

    fig
    return SITE_BG, fig


@app.cell
def _(mo):
    a_slider = mo.ui.slider(-10.0, 10.0, step=0.1, label="a")
    b_slider = mo.ui.slider(-10.0, 10.0, step=0.1, label="b")
    mo.vstack([a_slider, b_slider])
    return a_slider, b_slider


@app.cell
def _(SITE_BG, fig):
    fig.savefig("attractor6", dpi=300, facecolor=SITE_BG, bbox_inches="tight")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
