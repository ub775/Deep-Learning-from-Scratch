import numpy as np
import matplotlib.pylab as plt

def step(x):
    y = x > 0
    return y.astype(np.int32)

def main():
    x = np.arange(-5.0, 5.0, 0.1)
    y = step(x)
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)
    plt.show()

if __name__ == '__main__':
    main()