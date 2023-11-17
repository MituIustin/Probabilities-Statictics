import numpy as np


def ex1():

    cnt1 = 0
    cnt2 = 0
    
    for i in range(10000):
        n =  np.random.choice(np.arange(0,2), p=[0.3, 0.7])
        
        r1 = np.random.choice(np.arange(0,2), p=[0.4, 0.6])
        r2 = np.random.choice(np.arange(0,2), p=[0.2, 0.8])

        if r1 == 0 and r2 == 0 and n == 0:
            cnt1 = cnt1 + 1
            cnt2 = cnt2 + 1
        
        if r1 == 0 and r2 == 0 and n == 1:
            cnt1 = cnt1+ 1
        
        


    print(f"Probabilitate : {(cnt2/10000)/(cnt1/10000)}")
ex1()
