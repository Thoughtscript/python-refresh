# dict examples

if __name__ == '__main__':

    try:

        exampleDictionary = {
            "field": "example",
            "attribute": "another",
            "numerical": 2
        }

        print(exampleDictionary)

        # access value of dict by key
        numericalOne = exampleDictionary.get("numerical")
        print(numericalOne)

        numericalTwo = exampleDictionary["numerical"]
        print(numericalTwo)

        # set value of dict
        exampleDictionary["numerical"] = 4
        print(exampleDictionary["numerical"])

        # iterating through the dict
        ## keys
        for x in exampleDictionary:
            print(x)

        ## values
        for x in exampleDictionary:
            print(exampleDictionary[x])

        for x in exampleDictionary.values():
            print(x)

        ## keys and values by destructuring
        for x, y in exampleDictionary.items():
            print(x, y)

    except Exception as ex:

        print('Exception! ' + str(ex))