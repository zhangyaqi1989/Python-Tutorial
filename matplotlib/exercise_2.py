"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison
Jan 2018

"""
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # change font
    # plt.rcParams['font.size'] = 18

    # create a new figure of size 8x6 inches, 80 dots per inch
    plt.figure(figsize=(8, 6), dpi=80)

    # create a new subplot from a grid of 1x1
    plt.subplot(111)

    N = 256
    xs = np.linspace(-np.pi, np.pi, num=N)

    sins, coss = np.sin(xs), np.cos(xs)

    plt.plot(xs, sins, color="blue", linewidth=2.0, linestyle="-", label="sin")
    plt.plot(xs, coss, color="red", linewidth=2.0, linestyle="--", label="cos")
    plt.xlim(-4.0, 4.0)
    plt.ylim(-1.1, 1.1)
    plt.xticks(np.linspace(-4, 4, 9))
    plt.yticks(np.linspace(-1, 1, 5))
    plt.xlabel('x')
    plt.ylabel('sin/cos')
    plt.grid(True)
    plt.title('sin vs cos')
    plt.legend(loc="upper left")
    plt.savefig("exercise_2.png", dpi=80)

    plt.show()

