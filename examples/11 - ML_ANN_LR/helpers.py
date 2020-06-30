import numpy as np

# Helper operations.

def sigmoid(Z):
    A = 1 / (1 + np.exp(-Z))
    cache = Z
    return A, cache

def relu(Z):
    A = np.maximum(0,Z)
    cache = Z
    return A, cache

def relu_backward(dA, cache):
    Z = cache
    dZ = np.array(dA, copy=True)
    dZ[Z <= 0] = 0
    return dZ

def sigmoid_backward(dA, cache):
    Z = cache
    s = 1 / (1 + np.exp(-Z))
    dZ = dA * s * (1 - s)
    return dZ

# Parameter initialization and/or updating

def initialize_parameters(LAYERS):
    np.random.seed(1)
    params = {}
    L = len(LAYERS)
    try:
        for l in range(1, L):
            params['W' + str(l)] = np.random.randn(LAYERS[l], LAYERS[l - 1]) / np.sqrt(LAYERS[l - 1])
            params['b' + str(l)] = np.zeros((LAYERS[l], 1))

    except Exception as ex:
        print('Exception initialize_parameters! ' + str(ex))

    return params

# higher is both required to find the model
# and to find it more quickly - LR 2 finds in 5 iterations (compared with 31 in single layer)
# if it's 4,5 it's not granular enough and will fail to generate a solution
def update_parameters(params, grads, learning_rate = 3):
    L = len(params) // 2
    try:
        for l in range(L):
            params["W" + str(l + 1)] = params["W" + str(l + 1)] - learning_rate * grads["dW" + str(l + 1)]
            params["b" + str(l + 1)] = params["b" + str(l + 1)] - learning_rate * grads["db" + str(l + 1)]

    except Exception as ex:
        print('Exception update_parameters! ' + str(ex))

    return params

# Many-layered ANN forward

def linear_forward(A, W, b):
    Z = W.dot(A) + b
    cache = (A, W, b)
    return Z, cache

def linear_activation_forward(A_prev, W, b, activation):
    A = A_prev
    cache = ()
    try:
        if activation == "sigmoid":
            Z, linear_cache = linear_forward(A_prev, W, b)
            A, activation_cache = sigmoid(Z)

        elif activation == "relu":
            Z, linear_cache = linear_forward(A_prev, W, b)
            A, activation_cache = relu(Z)

        cache = (linear_cache, activation_cache)

    except Exception as ex:
        print('Exception linear_activation_forward! ' + str(ex))

    return A, cache

def L_model_forward(X, parameters):

    A = X
    AL = A
    caches = []
    L = len(parameters) // 2
    try:
        for l in range(1, L):
            A_prev = A
            A, cache = linear_activation_forward(A_prev, parameters['W' + str(l)], parameters['b' + str(l)], activation="relu")
            caches.append(cache)

        AL, cache = linear_activation_forward(A, parameters['W' + str(L)], parameters['b' + str(L)], activation="sigmoid")
        caches.append(cache)

    except Exception as ex:
        print('Exception L_model_forward! ' + str(ex))

    return AL, caches

# Many-layered ANN backward

def linear_backward(dZ, cache):
    dA_prev = 0
    dW = 0
    db = 0
    try:
        A_prev, W, b = cache
        m = A_prev.shape[1]

        dW = 1. / m * np.dot(dZ, A_prev.T)
        db = 1. / m * np.sum(dZ, axis=1, keepdims=True)
        dA_prev = np.dot(W.T, dZ)

    except Exception as ex:
        print('Exception linear_backward! ' + str(ex))

    return dA_prev, dW, db

def linear_activation_backward(dA, cache, activation):
    linear_cache, activation_cache = cache
    dA_prev = 0
    dW = 0
    db = 0
    try:
        if activation == "relu":
            dZ = relu_backward(dA, activation_cache)
            dA_prev, dW, db = linear_backward(dZ, linear_cache)

        elif activation == "sigmoid":
            dZ = sigmoid_backward(dA, activation_cache)
            dA_prev, dW, db = linear_backward(dZ, linear_cache)

    except Exception as ex:
        print('Exception linear_activation_backward! ' + str(ex))

    return dA_prev, dW, db

def L_model_backward(AL, Y, caches):
    grads = {}
    L = len(caches)
    m = AL.shape[1]
    Y = Y.reshape(AL.shape)

    try:
        dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))
        current_cache = caches[L - 1]
        grads["dA" + str(L-1)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL, current_cache, "sigmoid")

        for l in reversed(range(L - 1)):
            current_cache = caches[l]
            dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads["dA" + str(l + 1)], current_cache, "relu")
            grads["dA" + str(l)] = dA_prev_temp
            grads["dW" + str(l + 1)] = -dW_temp
            grads["db" + str(l + 1)] = -db_temp

    except Exception as ex:
        print('Exception L_model_backward! ' + str(ex))

    return grads

# Prediction

def predict(AL):
    predictions = AL > .5
    return predictions

def predict_ann(X, parameters):
    AL, cache = L_model_forward(X, parameters)
    predictions = predict(AL)
    return predictions

# Layers

def layers(X, Y, parameters):
    AL, caches = L_model_forward(X, parameters)
    grads = L_model_backward(AL, Y, caches)
    parameters = update_parameters(parameters, grads)

    predictions = predict(AL)
    print(AL)
    print("Predict: " + str(predictions))

    return predictions, AL, parameters
