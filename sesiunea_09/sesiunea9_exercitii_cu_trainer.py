"""
Sesiunea 9 - Exercitii cu Trainer
"""


# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------

def create_triggered_function():        # definim functia "create_triggered_function"
    call_count = 0                      # defineste variabila locala call_count si o initializeaza cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function" este apelata
        print("-" * 150 + "\n" * 2)
        print(f"Output pentru exercitiul cu numarul [ {call_count} ]")
                                        # ⬆️ printeaza text + valoare stocata in variabila "call_count" - loop iteration, printeaza o data per apelare functie
        print()
    return triggered_function           # acerst return este folosit pentru functia "create_triggered_function"

# Create the triggered function         # TBD
triggered_function = create_triggered_function()

# Example usage:
# triggered_function()                  # apelarea functiei

# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------


"""
IMPORTANT! Pentru toate exercitiile: apelati functia de cel putin 2 ori
cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.                        
"""

"""
1. Functie care returneaza aria dreptunghiului.
"""

triggered_function()

# latime = int(input("Care este latimea dreptunghiului? \n"))
# lungime = int(input("Care este lungime dreptunghiului? \n"))
#
# def aria_dreptunghiului(latime, lungime):
#     return latime * lungime
#
# print(f"Aria dreptunghiului este {aria_dreptunghiului(latime, lungime)}")



"""
2. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""

triggered_function()



# # implementation 1
# litera = input("Introduceti o litera: ")
# cuvant = input("Introduceti un cuvant: ")
#
# def verificare_caracter(litera, cuvant):
#     if litera in cuvant:
#         return True
#     else:
#         return False
#
# print(verificare_caracter(litera, cuvant))



# # implementation 2
# litera = input("Introduceti o litera: ")
# cuvant = input("Introduceti un cuvant: ")
#
# def verificare_caracter(litera, cuvant):
#     if cuvant.find(litera) == -1:       # returneaza -1 daca nu gaseste caracterul, iar daca gaseste caracterul returneaza indexul
#         return False
#     else:
#         return True
#
# print(verificare_caracter(litera, cuvant))



# # implementation 3
# litera = input("Introduceti o litera: ").lower()
# cuvant = input("Introduceti un cuvant: ").lower()
#
# def verificare_caracter(litera, cuvant):
#     for caracter in cuvant:
#         if caracter == litera:
#             return True
#     else:
#         return False
#
# print(verificare_caracter(litera, cuvant))



"""
3. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA:
Primul numar x este mai mare decat al doilea numar y
Al doilea numar y este mai mare decat primul numar x
Numerele sunt egale. 
"""

triggered_function()

# def compara_numere(x, y):
#     if x > y:
#         print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
#     elif y > x:
#         print(f"Al doilea numar {y} este mai mare decat primul numar {x}")
#     else:
#         print(f"Numerele sunt egale.")
#
# compara_numere(1, 2)
# compara_numere(23, 15)
# compara_numere(5, 5)



"""
4. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""

triggered_function()






"""
5. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""

# triggered_function()






"""
6. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

# triggered_function()






"""
7. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1 :2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

# triggered_function()






"""
8. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
"""

# triggered_function()






"""
9. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""

# triggered_function()






"""
10. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""

# triggered_function()








"""
11. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""

# triggered_function()






"""
12. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""

# triggered_function()





"""
13. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun
daca nu vrei sa ne zici cand e ziua ta :)
"""

# triggered_function()

# # Cracium
# from datetime import datetime
# def zile_pana_la_Craciun():
#     astazi = datetime.now()
#     data_Craciun = datetime(astazi.year, 12, 25)
#     if astazi > data_Craciun:
#         data_Craciun = datetime(astazi.year + 1, 12, 25)
#     zile_pana_la_Craciun = data_Craciun - astazi
#     print(f"Mai sunt {zile_pana_la_Craciun} zile pana la Craciun")
#
# zile_pana_la_Craciun()



# # TEMA - implementare pentru ziua noastra de nastere
# from datetime import datetime
# def zile_ramase_pana_la_ziua_mea_de_nastere():
#     astazi = datetime.now()
#     zi_nastere = datetime(astazi.year, 12, 7)
#     if astazi > zi_nastere:
#         zi_nastere = datetime(astazi.year + 1, 12, 7)
#     zile_pana_la_sarbatorire = zi_nastere - astazi
#     print(f"Mai sunt {zile_pana_la_sarbatorire} zile pana la ziua mea de nastere")
#
# zile_ramase_pana_la_ziua_mea_de_nastere()





# implementare formular de contact
# package: __init__.py




# TEMA: formular de inregistrare
# de folosit implementarea self.email = None
# metoda validare: password = confirm password


