import numpy as np
import matplotlib.pyplot as plt

'''''
    Exercitiul 1 a :

    Care este probabilitatea ca ambii copii sa fie fete,
stiind ca cel mare este fata? <=> Care este  probabilitatea 
ca al cel mic sa fie fata? 
    ~ 0.5

cazuri posibile :

1) COPIL MIC : fata    ---    COPIL MARE : fata   (favorabil)
2) COPIL MIC : baiat   ---    COPIL MARE : fata

=> probabilitate 1/2 = 0.5
 
'''''

def ex1a():

    cazuri_totale = 0
    cazuri_favorabile = 0

    # < 0.5 = baiat 
    # > 0.5 = fata

    for i in range(10000):

        copil_1 = np.random.random()
        copil_2 = np.random.random()

        # ne intereseaza doar daca al doilea copil e fata 

        if copil_2 > 0.5:
            cazuri_totale += 1
            
            if copil_1 > 0.5:
                cazuri_favorabile += 1
    
    print(f"Probabilitatea de la EX 1 a) = {cazuri_favorabile/cazuri_totale}")






'''''
    Exercitiul 1 b :

    Care este probabilitatea ca ambii copii sa fie fete,
stiind ca unul dintre ei este fata?
    ~ 0.(3)

cazuri posibile :

1) COPIL MIC : fata    ---    COPIL MARE : fata   (favorabil)
2) COPIL MIC : baiat   ---    COPIL MARE : fata   
3) COPIL MIC : fata    ---    COPIL MARE : baiat

=> probabilitate 1/3 = 0.(3)
 
'''''

def ex1b():

    cazuri_totale = 0
    cazuri_favorabile = 0

    # < 0.5 = baiat 
    # > 0.5 = fata

    for i in range(10000):

        copil_1 = np.random.random()
        copil_2 = np.random.random()

        # ne intereseaza doar daca macar unul dintre copii este fata

        if copil_2 > 0.5 or copil_1 > 0.5:
            cazuri_totale += 1
            
            if copil_1 > 0.5 and copil_2 > 0.5:
                cazuri_favorabile += 1
    
    print(f"Probabilitatea de la EX 1 b) = {cazuri_favorabile/cazuri_totale}")







'''''
    Exercitiul 2

    Pentru acest exercitiu voi simula de
10000 de ori cate n aruncari si voi numara
in cate dintre acestea va pica cap de k ori.
    Probabilitatea maxima va fi atunci cand 
k o sa fie jumatate din n.

'''''

def ex2(n, k):

    cazuri_totale = 10000
    cazuri_favorabile = 0

    # > 0.5 = cap
    # < 0.5 = pajura

    for i in range(cazuri_totale):

        aruncari = np.random.rand(n)

        # aici numar cati capi au fost

        nr_capi = sum(aruncari > 0.5)
        
        if nr_capi == k:
            cazuri_favorabile += 1
    
    print(f"Probabilitatea de la EX 2 = {cazuri_favorabile/cazuri_totale}")






'''''
    Exercitiul 3

    Se poate observa din diagrama ca
np.random.uniform() functioneaza corect.
Spre exemplu, eu am impartit intervalul (a,b)
in 100 se bucati, iar pe exemplul dat de mine
(10000, 0, 1), se observa ca majoritatea bucatilor
(din cele 100) au frecventa ~ 100, ceea ce face
functia corecta. (deoarece, am impartit intervalul in 
100 de bucati, si 100 * 100 = 10000)

'''''

def ex3(n, a, b):
    
    # aici am generat sirul de lungime n 
    # cu valori cuprinse intre a si b

    valori = np.random.uniform(a, b, n)

    # aici am impartit (a,b) in 100 de intervale
    # (am setat si transparenta strict din motive estetice)

    plt.hist(valori, bins=100, range=(a, b), alpha=0.5)

    plt.xlabel("Valori generate")
    plt.ylabel("Frecventa")
    plt.xlim(a, b)
    plt.grid()
    plt.show()


# apelurile de functii

ex1a()
ex1b()
ex2(10,5)
ex3(10000, 0, 1)

