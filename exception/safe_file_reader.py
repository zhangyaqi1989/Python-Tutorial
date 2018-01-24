"""
written by Yaqi Zhang (zhang623@wisc.edu)
University of Wisconsin-Madison

"""

if __name__ == "__main__":
    try:
        f = open('test.txt', 'r')
        print(1/0)
    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e)
    else:
        print(f.read())
        f.close()
    finally:
        print("Executing Finally")
