"""
EXERCITII WORKSHOP (Sesiunea 7)
"""
import math


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
! Pentru toate exercițiile: Apelati functia de cel putin 2 ori cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.
"""


"""
1. Scrieti o functie care primeste ca parametru lungimea laturii
unui patrat si returneaza aria sa.
"""

triggered_function()

# def arie_patrat(l):
#     arie_patrat = l ** 2
#     return arie_patrat
#
# print(arie_patrat(3))



"""
2. Scrieti un subprogram care primeste ca parametru lungimea laturii unui patrat
si returneaza atat lungimea diagonalei, cat si perimetrul patratului.
"""

triggered_function()

# def calcule_patrat(l):
#     lungime_diagonala = l * 1.414        # l * 'radical din 2'
#     perimetru = 4 * l
#     return lungime_diagonala, perimetru
#
# print(calcule_patrat(2))



"""
3. Scrieti o functie care primeste ca parametri de intrare lungimile celor doua catete
ale unui triunghi dreptunghic si returneaza lungimea ipotenuzei.
"""

triggered_function()

# import math
#
# def calcul_triunghi(cateta1, cateta2):
#     lungime_ipotenuza = math.sqrt(cateta1 ** 2 + cateta2 ** 2)
#     return lungime_ipotenuza
#
# print(calcul_triunghi(3, 4))



"""
4. Scrieti o functie care primeste 3 parametri de tip real, cu semnificatia
de lungimi pentru 3 segmente. 
Functia va returna 1 daca cele trei segmente pot forma un triunghi si 0, in caz contrar.
"""

triggered_function()

# def verificare_triunghi(lungime_segment1, lungime_segment2, lungime_segment3):
#     if lungime_segment1 > 0 and lungime_segment2 > 0 and lungime_segment3 > 0:
#         if lungime_segment1 + lungime_segment2 > lungime_segment3 or lungime_segment2 + lungime_segment3 > lungime_segment1 or lungime_segment3 + lungime_segment1 > lungime_segment2:
#             return 1
#     else:
#         return 0
#
# print(verificare_triunghi(1, 2, 3))



"""
5. Functie care returneaza aria cercului.
"""

triggered_function()

# import math
#
# def aria_cercului(raza):
#     aria_cercului = math.pi * raza ** 2
#     return aria_cercului
#
# print(aria_cercului(2))



"""
6. Functie fara return, primeste un string si printeaza pe ecran:
Numarul de caractere lower case este x
Numarul de caractere upper case este y 
"""

triggered_function()

# # implementare FOR EACH
# def numaratoare_caractere(string):
#
#     count_lower = 0
#     count_upper = 0
#
#     for caracter in string:
#         if caracter.islower():
#             count_lower += 1
#         elif caracter.isupper():
#             count_upper += 1
#
#     print(f"Numarul de caractere lower case este {count_lower}")
#     print(f"Numarul de caractere upper case este {count_upper}")
#
# numaratoare_caractere('HeLlO WoRlD!')


# # implementare FOR
# def numaratoare_caractere(string):
#
#     count_lower = 0
#     count_upper = 0
#
#     for i in  range(len(string)):
#         if string[i].islower():
#             count_lower += 1
#         elif string[i].isupper():
#             count_upper += 1
#
#     print(f"Numarul de caractere lower case este {count_lower}")
#     print(f"Numarul de caractere upper case este {count_upper}")
#
# numaratoare_caractere('HeLlO WoRlD!')






"""
7. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive.
"""

triggered_function()

# FOR EACH
# def arata_numere_pozitive(lista):
#     lista_numere_pozitive = []
#     for numar in lista:
#         if numar > 0:
#             lista_numere_pozitive.append(numar)
#     return lista_numere_pozitive
#
# print(arata_numere_pozitive([500, -2, 35, 0, 2.34, 29, -10, 68, -3.14]))



# FOR
# def arata_numere_pozitive(lista):
#     lista_numere_pozitive = []
#     for i in range(len(lista)):
#         if lista[i] > 0:
#             lista_numere_pozitive.append(lista[i])
#     return lista_numere_pozitive
#
# print(arata_numere_pozitive([500, -2, 35, 0, 2.34, 29, -10, 68, -3.14]))
