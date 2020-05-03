# dependency injection example with other examples

## note that depending on env setup, some dependencies will appear as errors (this is true of Django as well)
import dependency

if __name__ == '__main__':

    try:

        # variable assignment destructuring via tuple
        x,y = (15,2)

        # dict of tuples
        dictTuple = [
            ("a", 1, "c"),
            ("d", 2, "e"),
            ("f", 3, "g")
        ]

        ## iterate through dict
        for x, y, z in dictTuple:
            print(f"x: {x}, y: {y}, z: {z}")

        for x in dictTuple:
            print(f"x: {x[0]}, y: {x[1]}, z: {x[2]}")

        # do something n times
        for x in range(10):
            print(x)

        # lambda example
        l = lambda a, b: a * b
        print(l(5, 6))

        # function
        def exampleFunction(x):
            str = "Hello " + x

            ## basic string operations
            print(str)
            print(str[0:3])
            print(len(str))

            ## splite array
            sp = str.split(" ")
            print(sp)

            ## regex "in"
            isIn = "Hello" in str
            print(isIn)


        exampleFunction("World!")

        # dependency injection example
        robo = dependency.RoboCat("cat one", "Egyptian", "chrome")
        print(robo.meow("10101010011"))

    except Exception as ex:

        print('Exception!'.format(ex))