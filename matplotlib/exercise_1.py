"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison
Jan 2018

"""
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    N = 256
    xs = np.linspace(-np.pi, np.pi, num=N)
    sins = np.sin(xs)
    coss = np.cos(xs)
    plt.plot(xs, sins)
    plt.plot(xs, coss)
    plt.show()

