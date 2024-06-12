import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist
import pickle
import numpy as np
from functions.sigmoid import sigmoid
from functions.softmax import softmax

def get_test():
    (train_X, train_y), (test_X, test_y) = load_mnist(normalize=True, flatten=True, one_hot_label=False)
    
    return test_X, test_y

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)

    return y

x, t = get_test()
network = init_network()

batch_size = 100
accuracy_cnt = 0
for i in range(0, len(x), batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p = np.argmax(y_batch, axis=1)
    accuracy_cnt += np.sum(p == t[i:i+batch_size])

print(f"Accuracy: {float(accuracy_cnt) / len(x)}")
