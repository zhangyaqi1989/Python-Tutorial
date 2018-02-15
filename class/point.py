"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""
import random

class Point2D:
    num = 0 # static variable 
    def __init__(self, x, y): # constructor
        self.x = x
        self.y = y
        Point2D.num += 1

    def __str__(self): # special method toString()
        """
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""
import numpy as np
import matplotlib.pyplot as plt


if __name__ == "__main__":
    print("Hello World")

        return "({0}, {1})".format(self.x, self.y)

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return "({0}, {1}, {2})".format(self.x, self.y, self.z)


if __name__ == "__main__":
    p = Point2D(1, 2)
    print(p)
    print(Point2D.num)
    lst = []
    for _ in range(10):
        p = Point2D(random.randint(0, 10), random.randint(0, 10))
        lst.append(p)

    print(Point2D.num)
    for item in lst:
        print(item)
    p3d = Point3D(1, 2, 3)
    print(p3d)
    print(Point3D.num)
