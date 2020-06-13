# implementing an ANN from scratch and to get a better sense of variable shapes

import helpers
import numpy as np

if __name__ == '__main__':

    try:

        def train_ann(DATA, LABELS, HIDDEN_LAYER_SIZE, iterations, TEST):

            for x in range(DATA.shape[1]):
                print("Data entry " + str(DATA[0][x]) + "&" + str(DATA[1][x]) + " with label " + str(LABELS[0][x]))

            result = None
            found = None
            parameters = helpers.initialize_parameters(DATA, LABELS, HIDDEN_LAYER_SIZE)

            for i in range(0, iterations):

                A2, cache = helpers.forward_propagation(DATA, parameters)
                predict = helpers.predict(A2)
                print("Predict: " + str(predict))
                if (predict == TEST).all():
                    found = i
                    result = predict
                    break

                cost = helpers.compute_cost(A2, LABELS)
                print("Cost: " + str(cost))

                grads = helpers.backward_propagation(parameters, cache, DATA, LABELS)
                parameters = helpers.update_parameters(parameters, grads)

            print("ANN arrived at conclusion: " + str(result) + " after " + str(found) + " iterations ")
            return parameters


        DATA = np.array([[0,0], [0,1], [1,1], [1,0]])
        LABELS = np.array([[0, 0, 1, 0]])
        TEST = np.array([[False, False, True, False]])

        # transpose DATA so shape (2,4)
        result = train_ann(DATA.T, LABELS, 4, 100, TEST)
        # print(result)

        # --------------------------------------------------------------- #
        # Now, let's save off the training data above (results) and ...
        # pass in a fresh set of data

        def predict_ann(DATA, parameters):
            A2, cache = helpers.forward_propagation(DATA, parameters)
            predict = helpers.predict(A2)
            return predict

        DATA = np.array([[1, 1], [0, 0], [1, 0], [0, 1]])
        testResult1 = predict_ann(DATA.T, result)
        print("Test set 1: " + str(testResult1) + " from " + str(DATA))

        DATA = np.array([[0, 1], [1, 1], [1, 1], [0, 1]])
        testResult2 = predict_ann(DATA.T, result)
        print("Test set 2: " + str(testResult2) + " from " + str(DATA))

        DATA = np.array([[1, 1], [1, 1], [1, 1], [1, 1]])
        testResult3 = predict_ann(DATA.T, result)
        print("Test set 3: " + str(testResult3) + " from " + str(DATA))

        DATA = np.array([[0, 1], [0, 1], [0, 1], [0, 1]])
        testResult4 = predict_ann(DATA.T, result)
        print("Test set 4: " + str(testResult4) + " from " + str(DATA))

    except Exception as ex:

        print('Exception! ' + str(ex))