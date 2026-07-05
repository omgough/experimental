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
    from fractions import Fraction

    return Fraction, mo, mpl, np, plt


@app.cell
def _(Fraction, np):
    def attractor(x, y, a, b):
        x_next = np.sin(x**2 - y**2 + a)
        y_next = np.cos(2*x*y + b)
        return x_next, y_next

    def pi_label(value):
        frac = Fraction(value / np.pi).limit_denominator(8)
        n, d = frac.numerator, frac.denominator
        if n == 0:
            return "0"
        sign = "-" if n < 0 else ""
        n = abs(n)
        num = r"\pi" if n == 1 else rf"{n}\pi"
        return rf"{sign}{num}" if d == 1 else rf"{sign}\frac{{{num}}}{{{d}}}"

    return attractor, pi_label


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
def _(a, b, mpl, pi_label, plt, x_values, y_values):
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
        rf"$a = {pi_label(a)}, \; b = {pi_label(b)}$"
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
def _(mo, np):
    a_slider = mo.ui.slider(-4*np.pi, 4*np.pi, step=np.pi/8, label="a")
    b_slider = mo.ui.slider(-4*np.pi, 4*np.pi, step=np.pi/8, label="b")
    mo.vstack([a_slider, b_slider])
    return a_slider, b_slider


@app.cell
def _(SITE_BG, fig):
    fig.savefig("attractor9", dpi=300, facecolor=SITE_BG, bbox_inches="tight")
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
