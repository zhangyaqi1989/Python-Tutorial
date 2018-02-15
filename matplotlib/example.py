import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Hello World")
    m = 5
    n = 7
    xs = [0, m, m, 0, 0]
    ys = [0, 0, n, n, 0]
    plt.axis('equal')
    for i in range(4):
        plt.xlim([0, m + 1])
        plt.ylim([0, n + 1])
        x0, x1 = xs[i], xs[i+1]
        y0, y1 = ys[i], ys[i+1]
        plt.plot([x0, x1], [y0, y1])
        plt.pause(0.5)
        plt.draw()
    plt.show()

