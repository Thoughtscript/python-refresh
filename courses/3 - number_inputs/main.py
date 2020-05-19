if __name__ == '__main__':

    try:

        # enter 7,2,bob,10,4,done
        # should see Invalid input, ..., Maximum is 10, Minimum is 2

        largest = None
        smallest = None

        while True:
            num = input("Enter a number: ")
            try:

                if num == "done": break

                # check if NaN
                num = int(num)

                # forgot what instance of equivalent is! Yikes!
                # also forgot the logical operators :( - it's not '||' or '&&'!
                if smallest is None and largest is None:
                    smallest = num
                    largest = num
                    continue
                if num < smallest:
                    smallest = num
                    continue
                if num > largest:
                    largest = num
                    continue

            except:
                print("Invalid input")

        print("Maximum is", largest)
        print("Minimum is", smallest)

    except Exception as ex:

        print('Exception!'.format(ex))
