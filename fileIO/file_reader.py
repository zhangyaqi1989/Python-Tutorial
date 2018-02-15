"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    filename = "A3_Square.gcode"
    ''' 1. traditional method '''
    f = open(filename, 'r') # open file
    lines = f.readlines()   # read lines into a list
    lines = [line.strip()[line.index('G'):] for line in lines] # remove NXXX from line
    tokens_lst = [line.split() for line in lines] # split line into tokens
    for tokens in tokens_lst:
        print(tokens)
    f.close()

    ''' 2. use with '''
    with open(filename, 'r') as f: # handle close() automatically
        lines = f.readlines()
    lines = [line.strip()[line.index('G'):] for line in lines] # remove NXXX from line
    tokens_lst = [line.split() for line in lines] # split line into tokens
    for tokens in tokens_lst:
        print(tokens)
