"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""
import sys

if __name__ == "__main__":
    # sys.argv is a string list
    for i, arg in enumerate(sys.argv):
        print("argv[{0}] = {1}".format(i, arg))

    # cover string to int/float
    s_int = '100'
    print(int(s_int))
    s_float = '3.14'
    print(float(s_float))
