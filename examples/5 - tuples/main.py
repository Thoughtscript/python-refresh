if __name__ == '__main__':

    try:

        # 3-tuple
        exampleTuple = (1,2,3)

        # Access tuples
        print(exampleTuple[2])

        # Tuples can't be changed - they are immutable
        ## With throw error if uncommented

        ### exampleTuple[1] = 44

        # Destructuring
        (x, y, z) = (9,10,11)
        print(x)
        print(y)
        print(z)
        print((x, y, z))

        # Comparison - element by element
        print(exampleTuple < (x, y, z))
        print(exampleTuple > (1000, "", "Hello"))

    except Exception as ex:

        print('Exception! ' + str(ex))