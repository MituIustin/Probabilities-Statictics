import numpy as np
from random import randrange
import time
import matplotlib as plt
import matplotlib.pyplot as plt


zar_1 = [2,2,2,5,5,5]
zar_2 = [3,3,3,3,3,6]
zar_3 = [1,4,4,4,4,4]

cnt_1vs2 = 0
cnt_2vs3 = 0
cnt_3vs1 = 0

cnt_1vs2_np = 0
cnt_2vs3_np = 0
cnt_3vs1_np = 0


def simulare_1vs2():
    global zar_1
    global zar_2
    global cnt_1vs2
    for i in range (100000):
        if zar_1[randrange(6)] < zar_2[randrange(6)]:
            cnt_1vs2 += 1

def simulare_2vs3():
    global zar_2
    global zar_3
    global cnt_2vs3
    for i in range (100000):
        if zar_2[randrange(6)] < zar_3[randrange(6)]:
            cnt_2vs3 += 1

def simulare_3vs1():
    global zar_1
    global zar_3
    global cnt_3vs1
    for i in range (100000):
        if zar_3[randrange(6)] < zar_1[randrange(6)]:
            cnt_3vs1 += 1

start_time = time.perf_counter()

simulare_1vs2()
simulare_2vs3()
simulare_3vs1()

p1 = cnt_1vs2/100000
p2 = cnt_2vs3/100000
p3 = cnt_3vs1/100000

end_time = time.perf_counter()
t1 = end_time - start_time

print(f"Probabilitatea ca zarul 2 sa bata zarul 1 este {p1}")
print(f"Probabilitatea ca zarul 3 sa bata zarul 2 este {p2}")
print(f"Probabilitatea ca zarul 1 sa bata zarul 3 este {p3}")
print("Time: ", t1)


def simulare_1vs2_nparr():
    global zar_1
    global zar_2
    global cnt_1vs2_np

    arr1 = np.random.choice(zar_1, size=100000, replace=True)
    arr2 = np.random.choice(zar_2, size=100000, replace=True)

    cnt_1vs2_np = sum(arr1 < arr2)
    


def simulare_2vs3_nparr():
    global zar_2
    global zar_3
    global cnt_2vs3_np

    arr1 = np.random.choice(zar_2, size=100000, replace=True)
    arr2 = np.random.choice(zar_3, size=100000, replace=True)

    cnt_2vs3_np = sum(arr1 < arr2)
    
def simulare_3vs1_nparr():
    global zar_3
    global zar_1
    global cnt_3vs1_np

    arr1 = np.random.choice(zar_3, size=100000, replace=True)
    arr2 = np.random.choice(zar_1, size=100000, replace=True)

    cnt_3vs1_np = sum(arr1 < arr2)
    
    

start_time = time.perf_counter()

simulare_1vs2_nparr()
simulare_2vs3_nparr()
simulare_3vs1_nparr()

p1 = cnt_1vs2_np/100000
p2 = cnt_2vs3_np/100000
p3 = cnt_3vs1_np/100000

end_time = time.perf_counter()
t2 = end_time - start_time


print(f"Probabilitatea ca zarul 2 sa bata zarul 1 este {p1}")
print(f"Probabilitatea ca zarul 3 sa bata zarul 2 este {p2}")
print(f"Probabilitatea ca zarul 1 sa bata zarul 3 este {p3}")
print("Time: ", t2)


print("Timp 1 / Timp 2 = ", t1/t2 )


def simulare_1vs2vs3():
    global zar_1
    global zar_2
    global zar_3
    cnt_1 = 0
    cnt_2 = 0
    cnt_3 = 0
    win_probs_1 = []
    win_probs_2 = []
    win_probs_3 = []
    for i in range (100000):
        indx1 = zar_1[randrange(6)]
        indx2 = zar_2[randrange(6)]
        indx3 = zar_3[randrange(6)]
        if  indx1 > indx2 and indx1 > indx3:
            cnt_1 += 1
        if  indx2 > indx1 and indx2 > indx3:
            cnt_2 += 1
        if  indx3 > indx2 and indx3 > indx1:
            cnt_3 += 1

        win_probs_1.append(cnt_1 / (i + 1))
        win_probs_2.append(cnt_2 / (i + 1))
        win_probs_3.append(cnt_3 / (i + 1))

    print(f"Cu toate cele 3 zaruri, zarul 1 are sansa de castig: {cnt_1/100000}")
    print(f"Cu toate cele 3 zaruri, zarul 2 are sansa de castig: {cnt_2/100000}")
    print(f"Cu toate cele 3 zaruri, zarul 3 are sansa de castig: {cnt_3/100000}")

    plt.plot(range(1, 100001), win_probs_1, label='Zarul 1')
    plt.plot(range(1, 100001), win_probs_2, label='Zarul 2')
    plt.plot(range(1, 100001), win_probs_3, label='Zarul 3')
    plt.xlabel('Nr incercari')
    plt.ylabel('Prob de castig')
    plt.legend()
    plt.show()

simulare_1vs2vs3()

