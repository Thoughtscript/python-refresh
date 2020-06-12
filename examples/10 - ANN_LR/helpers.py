import numpy as np
import math


def initialize_parameters(X, Y, H):

    params = {"W1": None, "b1": None, "W2": None, "b2": None}

    try:

        n_x = X.shape[0]
        n_y = Y.shape[0]

        np.random.seed(2)

        params["W1"] = np.random.randn(H, n_x) * 0.01
        params["b1"] = np.zeros((H, 1))
        params["W2"] = np.random.randn(n_y, H) * 0.01
        params["b2"] = np.zeros((n_y, 1))

    except Exception as ex:
        print('Exception initialize_parameters! ' + str(ex))

    return params


def sigmoid(x):
    return 1 / (1 + math.exp(-x))


def forward_propagation(X, params):
    cache = {"Z1": 0, "A1": 0, "Z2": 0, "A2": 0}

    try:

        cache["Z1"] = np.dot(params["W1"], X) + params["b1"]
        cache["A1"] = np.tanh(cache["Z1"])
        cache["Z2"] = np.dot(params["W2"], cache["A1"]) + params["b2"]
        cache["A2"] = sigmoid(cache["Z2"])

    except Exception as ex:
        print('Exception forward_propagation! ' + str(ex))

    return cache["A2"], cache


def compute_cost(A2, Y):
    cost = 0

    try:
        m = Y.shape[1]
        logprobs = np.multiply(Y, np.log(A2)) + np.multiply((1 - Y), np.log(1 - A2))
        cost = - 1 / m * np.sum(logprobs)
        cost = float(np.squeeze(cost))

    except Exception as ex:
        print('Exception compute_cost! ' + str(ex))

    return cost


def backward_propagation(params, cache, X, Y):
    grads = {"dW1": 0, "db1": 0, "dW2": 0, "db2": 0}
    try:
        m = X.shape[1]

        dZ2 = cache["A2"] - Y
        grads["dW2"] = 1 / m * np.dot(dZ2, cache["A1"].T)
        grads["db2"] = 1 / m * np.sum(dZ2, axis=1, keepdims=True)

        dZ1 = np.dot(params["W2"].T, dZ2) * (1 - np.power(cache["A1"], 2))
        grads["dW1"] = 1 / m * np.dot(dZ1, X.T)
        grads["db1"] = 1 / m * np.sum(dZ1, axis=1, keepdims=True)

    except Exception as ex:
        print('Exception backward_propagation! ' + str(ex))

    return grads


def update_parameters(params, grads, learning_rate=1.2):
    parameters = {"W1": 0, "b1": 0, "W2": 0, "b2": 0}
    try:

        parameters["W1"] = params["W1"] - learning_rate * grads["dW1"]
        parameters["b1"] = params["b1"] - learning_rate * grads["db1"]
        parameters["W2"] = params["W2"] - learning_rate * grads["dW2"]
        parameters["b2"] = params["b2"] - learning_rate * grads["db2"]

    except Exception as ex:
        print('Exception update_parameters! ' + str(ex))

    return parameters
