import numpy as np
import pandas as pd

# Reading dataset from an Excel file
df = pd.read_excel('student_dataset.xlsx')

# Selecting relevant features (CGPA, 10th Score, 12th Score, IQ) as input and Placement as output
X = df[['CGPA', '10th Score', '12th Score', 'IQ']].values.T
Y = df[['Placement']].values.T  # Target variable

# Initializing parameters
def initialize_parameters(layer_dims):
    np.random.seed(3)
    print("Layer Dimensions:", layer_dims)
    parameters = {}
    L = len(layer_dims)
    print("Total No. of layers in NN:", L)

    for i in range(1, L):
        parameters['W' + str(i)] = np.ones((layer_dims[i-1], layer_dims[i])) * 0.1
        parameters['b' + str(i)] = np.zeros((layer_dims[i], 1))

    return parameters

layer_dims = [4, 3, 1]  # 4 input features, 3 hidden neurons, 1 output neuron
parameters = initialize_parameters(layer_dims)
print(parameters)

# Forward propagation
def linear_forward(A_prev, W, b):
    Z = np.dot(W.T, A_prev) + b
    return Z

def relu(Z):
    return np.maximum(0, Z)

def L_layer_forward(X, parameters):
    A = X
    caches = []
    L = len(parameters) // 2
    
    for i in range(1, L):
        A_prev = A
        W = parameters['W' + str(i)]
        b = parameters['b' + str(i)]
        Z = linear_forward(A_prev, W, b)
        A = relu(Z)
        cache = (A_prev, W, b, Z)
        caches.append(cache)
    
    W_out = parameters['W' + str(L)]
    b_out = parameters['b' + str(L)]
    Z_out = linear_forward(A, W_out, b_out)
    AL = Z_out
    
    return AL, caches

# Example execution
y_hat, caches = L_layer_forward(X, parameters)
print("Final output:")
print(y_hat)
