import numpy as np
import math

latura_triunghi = np.sqrt(3) 
# am dedus asta dupa ce am dus o inaltime si am aplicat un cos de 30 de grade

nr_varianta_1 = 0
nr_varianta_2 = 0
nr_varianta_3 = 0

def varianta_1 () :

    global nr_varianta_1
    global latura_triunghi

    for i in range(0,10000):

        # aici generez 2 unghiuri aleatoare intre 0 si 2pi

        theta1 = 2 * np.pi * np.random.random()
        theta2 = 2 * np.pi * np.random.random()
        
        # calculam coordonatele lui x si y pt fiecare punct

        x1 = np.cos(theta1)
        y1 = np.sin(theta1)
        x2 = np.cos(theta2)
        y2 = np.sin(theta2)
        
        lungime_coarda = np.sqrt((x2 - x1)*(x2-x1) + (y2 - y1)*(y2-y1))
        if lungime_coarda > latura_triunghi:
            nr_varianta_1 += 1

def varianta_2():

    global nr_varianta_2
    global latura_triunghi

    for i in range(0, 10000):
        # unghi
        theta_pct = 2 * np.pi * np.random.random()

        # raza
        r = np.random.random()

        # x si y ale punctului ales random
        x = r * np.cos(theta_pct)
        y = r * np.sin(theta_pct)

        # unghiul pt punctele A (x1,y1) si B (x2,y2)
        theta = np.arctan2(y, x)

        x1 = r * np.cos(theta + np.pi/2)
        y1 = r * np.sin(theta + np.pi/2)

        x2 = r * np.cos(theta - np.pi/2)
        y2 = r * np.sin(theta - np.pi/2)

        lungime_coarda = np.sqrt((x2 - x1)*(x2-x1) + (y2 - y1)*(y2-y1))
        if lungime_coarda > latura_triunghi:
            nr_varianta_2 += 1




def varianta_3():

    global nr_varianta_3
    global latura_triunghi

    for i in range(0, 10000):

        # practic aici generez distanta de la centrul cercului la punctul respectiv
        punct = np.random.random()

        # calculam lungimea coardei ( din pitagora )
        lungime_coarda = 2 * np.sqrt(1 - punct*punct) 

        if lungime_coarda > latura_triunghi:
            nr_varianta_3 += 1
        
        '''''
        OBS.
            Aici probabilitatea mi se pare normal
        sa dea aprox 0.5. Practic in aceasta situatie nu 
        mi se pare neaparat ca varianta de a alege o coarda este
        "aleatorie". Practic in aceasta situatie nici macar nu conteaza
        unghiul, conteaza doar distanta de la centrul cercului la
        punctul ales aleator, deoarece, daca vrei ca aceasta sa fie mijlocul 
        coardei, automat latura dintre (x1,y1) si (x2,y2) o sa fie paralela
        cu diametrul cercului. Din moment ce distanta de la centrul cercului 
        la latura triunghiului este de 0.5 , practic algoritmul calculeaza ce 
        probabilitate exista sa aleg o lungime mai mare de 0.5 din
        intervalul [0,1), care e evident 50%.
        '''''

varianta_1()
varianta_2()
varianta_3()

probabilitate_varianta_1 = nr_varianta_1 / 10000
probabilitate_varianta_2 = nr_varianta_2 / 10000
probabilitate_varianta_3 = nr_varianta_3 / 10000

print(f"Probabilitatea pentru varianta 1: {probabilitate_varianta_1} ")
print(f"Probabilitatea pentru varianta 2: {probabilitate_varianta_2} ")
print(f"Probabilitatea pentru varianta 3: {probabilitate_varianta_3} ")

