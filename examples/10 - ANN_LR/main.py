# implementing an ANN from scratch and to get a better sense of variable shapes

import helpers
import numpy as np

if __name__ == '__main__':

    try:

        def ann(DATA, LABELS, HIDDEN_LAYER_SIZE, iterations):

            parameters = helpers.initialize_parameters(DATA, LABELS, HIDDEN_LAYER_SIZE)

            for i in range(0, iterations):

                A2, cache = helpers.forward_propagation(DATA, parameters)
                cost = helpers.compute_cost(A2, LABELS)
                grads = helpers.backward_propagation(parameters, cache, DATA, LABELS)
                parameters = helpers.update_parameters(parameters, grads)

            return parameters


        DATA = np.array([[0,0], [0,1], [1,1], [1,0]])
        LABELS = np.array([[0], [0], [1], [0]])

        result = ann(DATA, LABELS, 8, 100)
        print(result["b2"])

    except Exception as ex:

        print('Exception! ' + str(ex))