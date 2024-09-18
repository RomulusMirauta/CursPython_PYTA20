"""
Sesiunea 6 - Exercitii cu Trainer
"""


# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------

def create_triggered_function():        # definim functia "create_triggered_function"
    call_count = 0                      # defineste variabila locala call_count si o initializeaza cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function" este apelata
        # print()                         # printam un rand liber
        # print()
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
1. GHICITOARE DE NUMAR
- numar_secret = Generati un numar random intre 1 si 30
- numar_ghicit = None
- Folosind un while:
   - Utilizatorul alege un numar
   - Programul îi spune (in functie de caz):
        - Nr secret e mai mare
        - Nr secret e mai mic
        - Felicitari! Ai ghicit!
"""

triggered_function()

import random

numar_secret = random.randint(1, 30)

numar_ghicit = int(input("Ghiciti numarul: "))

while numar_secret != numar_ghicit:
    if numar_secret > numar_ghicit:
        print("Nr secret e mai mare")
        numar_ghicit = int(input("Ghiciti numarul: "))
    else:
        print("Nr secret e mai mic")
        numar_ghicit = int(input("Ghiciti numarul: "))
else:
    print("Felicitari! Ai ghicit!")



"""
2. Alege un numar de la tastatura si genereaza in consola o piramida
de numere, ca in exemplele de mai jos: 

Exemplu: 7

1
22
333
4444
55555
666666
7777777

Exemplu: 3

1
22
333
"""

# triggered_function()

# # print("2"*2)      # incercare, test

# numar = int(input("Alegeti numarul: \n"))
#
# for n in range(1, numar+1):
#     print(str(n) * n)




# tema: de printat un soare din caractere, cu un mesaj in mijlocul soarelui "concediu placut" !!!!!!!!!!!!!!!!!!!!!!!!!!!!!


# numar = int(input("Alegeti numarul: \n"))

# for n in range(1, 8):
#     # print(' ' * n)
#     # print((' ' + str(n)) * n)
#     # print(' ' * n + str(n) * n)
#     # print(' ' * (7-n) + str(n) * n)     # reversed indentation
#     print(' ' * (7-2*n) + str(n) * n)   # shape
#     print(' ' * (20-n) + str(n) * n)      # big indentation



# inc
# for n in range(1, 20):
#     print(' ' * (7-2*n) + str(n) * n)   # shape



# soare simplu
# # n = 5   # min
# n = 7   # ok
# # n = 9   # max
#
# for i in range(n):
#     for j in range(n):
#         if (i == n // 2 or j == n // 2 or (i == j) or (i + j == n - 1)):
#             print(n, end=" ")
#         else:
#             print(" ", end=" ")
#     print()



# soare cu mesaj
# n = 30
# message = "   Concediu placut   "
# mid = n // 2
# for i in range(n):
#     for j in range(n):
#         if i == mid and j == mid - len(message) // 3:
#             print(message, end="")
#             j += len(message) - 1
#         elif (i == mid or j == mid or (i == j) or (i + j == n - 1)):
#             print(n, end=" ")
#         else:
#             print(" ", end=" ")
#     print()




"""
3. Se da lista:
tastatura_telefon = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
  [0]
]

Itereaza prin lista 2D si printeaza ‘Cifra curenta este x.’
(HINT: nested for - adică for in for)
"""

# triggered_function()

# tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
#
# for sublista in tastatura_telefon:         # i = sublista = cifra (din tastatura_telefon)
#     for element in sublista:
#         print(f"Cifra curenta este {element}")




"""
4. Se da lista:
numere = [23, -45, 79, -236, 200, -13]

Creeaza o lista care contine doar numerele negative.
"""

# triggered_function()

# numere = [23, -45, 79, -236, 200, -13]
#
# numere_negative = []
#
# for numar in numere:
#     if numar > 0:
#         continue    # skip
#     numere_negative.append(numar)
#
# print(numere)
# print(numere_negative)




"""
5. 
Se da dictionarul:
persoana = {
    'nume': 'Alex',
    'varsta': 25,
    'oras': 'Bucuresti'
}

a. Cere utilizatorului cheia si valoarea pe care doreste sa o
adauge in dictionar. Foloseste metoda update().
b. Printeaza, pe rand, toate cheile din dictionar.
c. Printeaza, pe rand, toate valorile din dictionar.
"""

# triggered_function()

# persoana = {
#     'nume': 'Alex',
#     'varsta': 25,
#     'oras': 'Bucuresti'
# }
#
# #a
# cheie_utilizator = input("Introdu cheia: \n")
# valoare_utilizator = input("Introdu valoarea pentru cheia aleasa: \n")
# persoana.update({cheie_utilizator: valoare_utilizator})
# # print(persoana)
#
# #b
# for cheie in persoana.keys():
#     print(cheie)
#
# #c
# for valoare in persoana.values():
#     print(valoare)




"""
6. Cere utilizatorului sa introduca de la tastatura un numar intreg pozitiv.
Scrie un program care verifica daca numarul este prim.
Afiseaza un mesaj sugestiv in consola in fiecare caz.
"""

# triggered_function()

# numar = int(input("Introdu un numar intreg pozitiv: \n"))
#
# if numar > 1:
#     for i in range(2, numar):
#         if numar % i == 0:
#             print("Numarul NU este prim")
#             break
#     else:
#         print("Numarul este prim")
# else:
#     print("Numarul introdus este negativ")
