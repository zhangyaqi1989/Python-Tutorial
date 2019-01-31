import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Hello World")
    m = 5
    n = 7
    xs = [0, m, m, 0, 0]
    ys = [0, 0, n, n, 0]
    ax = plt.axes()
    ax.axis("equal")
    plt.xlim([-1, m + 1])
    plt.ylim([-1, n + 1])
    for i in range(4):
        x0, x1 = xs[i], xs[i+1]
        y0, y1 = ys[i], ys[i+1]
        ax.plot([x0, x1], [y0, y1], 'b-')
    plt.show()
