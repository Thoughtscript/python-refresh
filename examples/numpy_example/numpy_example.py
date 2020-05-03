# numpy example

# import the whole library and use it
# import numpy

from numpy import core

if __name__ == '__main__':

    try:

        # numpy array object
        arr = core.array([[1, 2, 3],[4, 2, 5]])
        print(arr)
        print(arr[0])

    except Exception as ex:

        print('Exception!'.format(ex))