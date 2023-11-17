import numpy as np
from random import randint

def ghiceste_usa(nr_usi):

    usi = np.random.rand(nr_usi)
    usi = (usi>=max(usi))

    raspuns_concurent = np.random.randint(0, nr_usi)
    
    if usi[raspuns_concurent] == False :
        return True
    return False

def ex1():
    cazuri_posibile = 10000
    cazuri_favorabile = 0
    nr_usi = 3
    for i in range(cazuri_posibile):
        if ghiceste_usa(nr_usi):
            cazuri_favorabile += 1
    
    print(f"Probabilitate = {cazuri_favorabile/cazuri_posibile}")


def ex2():

    cazuri_posibile = 0
    cazuri_favorabile = 0

    nr_usi = int(input("Nr. de usi = "))
    game = True
    
    while game:
        game = False
        cazuri_posibile += 1

        usi = np.random.rand(nr_usi)
        usi = (usi>=max(usi))
    

        raspuns = int(input("Ce usa alegi? \n"))
        raspuns = raspuns - 1

        print("O alegere foarte buna, uite ce era in spatele altor usi:")

        nr_usi_deschise = nr_usi - 2

        for i in range(nr_usi):
            if i == raspuns:
                print(f"Usa aleasa = ???")
            else:
                if nr_usi_deschise > 0 :
                    if usi[i] == False:
                        print(f"Usa {i+1} = Capra")
                    else:
                        print(f"Usa {i+1} = ???")
                        nr_usi_deschise += 1
                    nr_usi_deschise -= 1
                else:
                    print(f"Usa {i+1} = ???")

        schimbare = int(input("Iti schimbi alegerea ? \n 1) Da \n 2) Nu \n "))

        if schimbare == 1:
            if usi[raspuns-1] == True:
                print("Ai pierdut! \n")
            else:
                print("Ai castigat! \n")
                cazuri_favorabile += 1
        else:
            if usi[raspuns-1] == True:
                print("Ai castigat! \n")
                cazuri_favorabile += 1
            else:
                print("Ai pierdut! \n")

        raspuns = int(input("Joci iar? \n 1) Da \n 2) Nu \n"))
        if raspuns == 1:
            game = True
    
    
    print(f"Probabilitatea de castig = {cazuri_favorabile/cazuri_posibile}")

    

ex1()
ex2()
