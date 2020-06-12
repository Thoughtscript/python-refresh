# numpy example

# import the whole library and use it
import numpy as np

if __name__ == '__main__':

    try:

        # ---------------------- #
        # matrix multiplication

        a = np.random.rand(12288, 150)
        b = np.random.rand(150, 45)
        c = np.dot(a, b)
        print(c)
        ## 12288 x 45
        print(c.shape)
        print("\n")

        # ---------------------- #
        # element-wise multiplication

        a = np.random.rand(4, 3)
        b = np.random.rand(4, 1)
        c = a * b
        print(c)
        ## 4 x 3
        print(c.shape)
        print("\n")

        # ---------------------- #
        # vector

        v = np.array([10,30,1])
        print(v)
        ## 1 x 3 matrix with shape (3,)
        print(v.shape)
        print("\n")

        # ---------------------- #
        # element-wise addition

        a = np.random.rand(4, 3)
        b = np.random.rand(4, 3)
        c = a + b
        print(c)
        ## 4 x 3
        print(c.shape)
        print("\n")

        # ---------------------- #
        # transposing

        a = np.random.rand(4, 1)
        b = np.random.rand(1, 5)

        ## 1 x 4
        print(a.T.shape)
        ## 5 x 1
        print(b.T.shape)
        print("\n")



    except Exception as ex:

        print('Exception! ' + str(ex))