if __name__ == '__main__':

    try:

        hrs = input("Enter Hours:")
        rate = input("Enter Rate:")

        fortyOrLess = float(hrs)
        moreThanForty = float(0)

        if (fortyOrLess > 40.0):
            moreThanForty = fortyOrLess - 40.0
            fortyOrLess = 40.0

        dollars = fortyOrLess * float(rate) + moreThanForty * 1.5 * float(rate)
        print(dollars)

    except Exception as ex:

        print('Exception!'.format(ex))
