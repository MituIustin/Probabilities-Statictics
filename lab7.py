import numpy as np
import matplotlib.pyplot as plt


def f(p):
    array_of_numbers = np.random.rand(10000)
    array_of_numbers = array_of_numbers > p

    bins = [-0.5, 0.5, 1.5]
    counts = np.histogram(array_of_numbers, bins=bins)

    plt.hist(array_of_numbers, bins = bins, ec = 'black', density = True)

    plt.xticks([0,1])
    plt.show()

def binomiala(p, n):

    bins = [i for i in range(n + 2)]

    arr = []
    
    for i in range(10000):
        v = np.random.rand(n)
        successes = sum(v > p)
        arr.append(successes)
        
    plt.hist(arr, bins=bins, ec='black', density=True)
    plt.show()


# f(0.75)

binomiala(0.5, 100)
