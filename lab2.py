def fact(n):
    rezultat = 1
    for i in range(2,n+1):
        rezultat = rezultat*i
    return rezultat

def aranjamente(n,k):
    rezultat = 1
    for i in range(n, n-k,-1):
        rezultat = rezultat * i
    return rezultat

def combinari(n,k):
    rezultat = aranjamente(n,k)//fact(k)
    return rezultat

def ex1a(nr_pozitii, nr_caractere):
    produs = 1
    for i in range (1,nr_pozitii+1):
        produs = produs*nr_caractere
    print(f"Nr. de parole cu {nr_caractere} caractere este {produs} \nAdica {nr_caractere}^{nr_pozitii}.\n")
    return produs

def ex1b(nr_parole):
    nr_secunde = nr_parole/1000000000
    print(f"Pentru a testa cele {nr_parole} parole ar fi necesare: \n{nr_secunde} secunde \n{nr_secunde/60} minute \n{nr_secunde/360} ore \n{nr_secunde/(360*24)} zile\n")
    return nr_secunde/(360*24*7)

def ex1c(nr_saptamani):
    print(f"Intr-o saptamana probabilitatea de a sparge parola este {1/nr_saptamani}.\n")

def ex1d(nr_pozitii, nr_caractere):
    produs = 1
    for i in range (1,nr_pozitii+1):
        produs = produs*nr_caractere
    nr_secunde = produs/1000000000
    ex1c(nr_secunde/(360*24*7))


def ex2(nr_calculatoare, nr_studenti):
    rezultat = combinari(nr_studenti, nr_calculatoare)
    print(f"Putem aseza {nr_studenti} studenti intr-un lab. cu {nr_calculatoare} calculatoare in {rezultat} moduri.\n")

def ex3(nr_calculatoare, nr_studenti):
    rezultat = aranjamente(nr_calculatoare, nr_studenti)
    print(f"Putem aseza {nr_studenti} studenti intr-un lab. cu {nr_calculatoare} calculatoare in {rezultat} moduri.\n")
    

def ex4a(nr_noi, nr_vechi, nr_cumparate, i):
    nr_posibilitati = combinari(nr_noi+nr_vechi, nr_cumparate)
    nr_favorabile = combinari(nr_vechi,i) * combinari(nr_noi, nr_cumparate-i)
    print(f"Probabilitatea ca un client sa cumpere fix {i} calculatoare reconditionate este {nr_favorabile/nr_posibilitati}")
    return nr_favorabile/nr_posibilitati

    
def ex4b(nr_noi, nr_vechi, nr_cumparate):
    lista = []
    for i in range(0,nr_cumparate+1):
        lista.append(ex4a(nr_noi,nr_vechi,nr_cumparate,i))
    maxim = max(lista)
    index = -1
    for i in range(0, nr_cumparate+1):
        if lista[i] == maxim :
            index = i
            break
    print(f"Cel mai probabil cumparatorul se va alege cu {index} calculatoare reconditionate")

def ex5a(nr_carti, nr_extrase):
    probabilitate = combinari(48,2)*combinari(4,3)/combinari(52,5)
    print(f"Probabilitatea sa extragem 3 asi este {probabilitate}.\n")
    return probabilitate


