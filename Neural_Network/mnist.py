import sys, os
sys.path.append(os.pardir)
from dataset.mnist import load_mnist

(train_X, train_y), (test_X, test_y) = load_mnist(flatten=True, normalize=False)

print(train_X.shape)
print(train_y.shape)
print(test_X.shape)
print(test_y.shape)