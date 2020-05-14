if __name__ == '__main__':

    try:

        hrs = input("Enter Hours: ")
        rate = input("Enter Rate: ")
        # must convert to float
        dollars = float(hrs) * float(rate)
        # must convert to string
        print("Total Pay: " + str(dollars))

    except Exception as ex:

        print('Exception!'.format(ex))