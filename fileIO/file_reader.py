"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    filename = "A3_Square.gcode"
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    lines = [line.strip()[line.index('G'):] for line in lines]
    tokens = [line.split() for line in lines]
    print(tokens)
    """
    f = open(filename, 'r')
    lines = f.readlines()
    lines = [line.strip()[line.index('G'):] for line in lines]
    tokens = [line.split() for line in lines]
    print(tokens)
    f.close()
