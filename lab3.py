import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

#ex 1a + 1b

n = 0
def aruncare (procent):
    global n
    nr = np.random.random()
    if nr < procent:
        n = n + 1
    
def simulare_ab():
    global n
    x = np.linspace(0,10000,10000)
    y = []

    for i in range(1,10001):
        aruncare(0.5)
        y.append(n/i)
    plt.plot(x,y)
    plt.show()

simulare_ab()

#ex 1c

def simulare_c():
    global n
    x = np.linspace(0,10000,10000)
    y = []

    for i in range(1,10001):
        aruncare(0.75)
        y.append(n/i)
    plt.plot(x,y,'o')
    plt.show()

#simulare_c()

