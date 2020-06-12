# numpy example

# import the whole library and use it
import numpy as np
import time

if __name__ == '__main__':

    try:

        # ---------------------- #
        # init a, b, and c

        a = np.random.rand(100000)
        b = np.random.rand(100000)
        c = 0

        # ---------------------- #
        # for loop

        begin = time.time()

        for i in range(100000):
            c += a[i] * b[i]

        end = time.time()
        print(c)
        print(str(1000*(end - begin)) + " ms")
        print("\n")

        # ---------------------- #
        # dot matrix multiplication
        ## much faster

        begin = time.time()
        c = np.dot(a, b)
        end = time.time()

        print(c)
        print(str(1000*(end - begin)) + " ms")
        print("\n")

        # ---------------------- #
        # Second example - transposing through vectors

        a = np.random.rand(2, 5)
        print(a)
        print(a.shape)
        print("\n")

        b = np.random.rand(5, 1)
        print(b)
        print(b.shape)
        print("\n")

        begin = time.time()
        c = a * b.T
        end = time.time()

        print(c)
        ## shape 2 x 5 - the shapes match above and allow for very fast computation
        print(c.shape)
        print(str(1000 * (end - begin)) + " ms")
        print("\n")

    except Exception as ex:

        print('Exception! ' + str(ex))