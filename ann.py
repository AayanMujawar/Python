import numpy as np
import matplotlib.pyplot as plt





# Sigmoid activation function and its derivative for backpropagation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)





# Generate a simple dataset (study hours vs exam scores)
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)  # Study hours
y = np.array([35, 50, 60, 70, 75, 80, 85, 90, 95, 100]).reshape(-1, 1)  # Exam scores

# Normalize y to be between 0 and 1
y = y / 100





# Initialize parameters
input_layer_size = 1   # Input layer size (study hours)
hidden_layer_size = 3  # Hidden layer size
output_layer_size = 1  # Output layer size (exam score)
learning_rate = 0.01
epochs = 10000





# Initialize weights and biases
np.random.seed(42)  # For reproducibility
w1 = np.random.randn(input_layer_size, hidden_layer_size) * 0.1  # Weights from input to hidden layer
b1 = np.zeros((1, hidden_layer_size))  # Bias for hidden layer
w2 = np.random.randn(hidden_layer_size, output_layer_size) * 0.1  # Weights from hidden to output layer
b2 = np.zeros((1, output_layer_size))  # Bias for output layer





# Training loop (backpropagation)
losses = []
for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X, w1) + b1
    a1 = sigmoid(z1)  # Hidden layer activation
    z2 = np.dot(a1, w2) + b2
    a2 = sigmoid(z2)  # Output layer activation
    
    # Loss calculation (Mean Squared Error)
    loss = np.mean((a2 - y) ** 2)
    losses.append(loss)






    # Backpropagation
    # Output layer error and gradients
    error_output = a2 - y
    d_w2 = np.dot(a1.T, error_output * sigmoid_derivative(a2))  # Gradient for w2
    d_b2 = np.sum(error_output * sigmoid_derivative(a2), axis=0, keepdims=True)  # Gradient for b2

    # Hidden layer error and gradients
    error_hidden = np.dot(error_output * sigmoid_derivative(a2), w2.T)
    d_w1 = np.dot(X.T, error_hidden * sigmoid_derivative(a1))  # Gradient for w1
    d_b1 = np.sum(error_hidden * sigmoid_derivative(a1), axis=0, keepdims=True)  # Gradient for b1






    # Update weights and biases using gradient descent
    w2 -= learning_rate * d_w2
    b2 -= learning_rate * d_b2
    w1 -= learning_rate * d_w1
    b1 -= learning_rate * d_b1

    # Print loss at intervals
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")







# Predictions after training
predictions = []
for i in range(len(X)):
    z1 = np.dot(X[i].reshape(1, 1), w1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, w2) + b2
    a2 = sigmoid(z2)
    predicted = a2[0][0] * 100  # Denormalize the output
    predictions.append(predicted)





# Plotting the loss over epochs
plt.plot(losses)
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.title('Loss during Training')
plt.grid(True)
plt.show()






# Final predictions
print("\nPredictions after training:")
for i in range(len(X)):
    print(f"Study hours: {X[i][0]}, Predicted Score: {predictions[i]:.2f}")
