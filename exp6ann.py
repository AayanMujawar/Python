import numpy as np
import pandas as pd

df = pd.read_excel('student_dataset.xlsx')

X = df[['CGPA', '10th Score', '12th Score', 'IQ']].values
Y = df[['Placement']].values

X = (X - X.mean(axis=0)) / X.std(axis=0)

def initialize_parameters(input_size, output_size):
    np.random.seed(3)
    W = np.random.randn(output_size, input_size) * 0.1
    b = np.zeros((output_size, 1))
    return W, b

def sigmoid(Z):
    return 1 / (1 + np.exp(-Z))

def sigmoid_derivative(A):
    return A * (1 - A)

def compute_cost(AL, Y):
    m = Y.shape[0]
    cost = (1 / (2 * m)) * np.sum(np.square(AL - Y))
    return cost

def forward_pass(X, W, b):
    Z = np.dot(X, W.T) + b.T
    A = sigmoid(Z)
    return A, Z

def backpropagation(X, Y, A, Z, W):
    m = Y.shape[0]
    dZ = A - Y
    dW = (1 / m) * np.dot(dZ.T, X)
    db = (1 / m) * np.sum(dZ, axis=0, keepdims=True)
    return dW, db

def update_parameters(W, b, dW, db, learning_rate):
    W = W - learning_rate * dW
    b = b - learning_rate * db
    return W, b

def train(X, Y, epochs, learning_rate):
    input_size = X.shape[1]
    output_size = 1
    W, b = initialize_parameters(input_size, output_size)

    for epoch in range(epochs):
        A, Z = forward_pass(X, W, b)
        cost = compute_cost(A, Y)
        dW, db = backpropagation(X, Y, A, Z, W)
        W, b = update_parameters(W, b, dW, db, learning_rate)
        if epoch % 100 == 0:
            print(f"Epoch {epoch} - Cost: {cost}")

    return W, b

W, b = train(X, Y, epochs=1000, learning_rate=0.01)

A, _ = forward_pass(X, W, b)
predictions = A > 0.5
print("Final Predictions:")
print(predictions)
