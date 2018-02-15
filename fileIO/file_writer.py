"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""

import random

if __name__ == "__main__":
    filename = "temp.txt"
    # create random ints in [0, 10]
    nums = [random.randint(0, 10) for _ in range(100)] 
    with open(filename, 'w') as f:
        for num in nums:
            f.write(str(num) + '\n')

