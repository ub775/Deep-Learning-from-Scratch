import numpy as np
import matplotlib.pylab as plt

def relu(x):
    return np.maximum(0, x)

def main():
    x = np.arange(-1.0, 1.0, 0.1)
    y = relu(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

if __name__ == '__main__':
    main()