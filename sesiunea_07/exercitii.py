"""
Rezolvari exercitii Functii - sesiunea 7
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
EX1: Defineste o functie care printeaza, pe rand,
primele 10 numere (1, 10).
"""

triggered_function()

# def print_primele_10_numere():
#     for numar in range(1, 11):
#         print(numar)
#
# print_primele_10_numere()



"""
EX2: Scrie o functie care parcurge o lista de numere data si
afiseaza mesajul 'Este par' pentru numerele pare si
'Este impar' pentru numere impare.
Daca in lista se gaseste un element care nu e numar intreg,
afiseaza un mesaj utilizatorului si apoi sari peste
elementul respectiv.
(Foloseste functia built-in isinstance()
pentru verificare daca elementul curent e int sau nu)
"""

triggered_function()

# # implementation 1
# def verifica_lista_numere(lista):
#     for i in range(len(lista)):
#         if isinstance(lista[i], int):
#             if lista[i] % 2 == 0:
#                 print(f"Numarul este par {lista[i]}")
#             else:
#                 print(f"Numarul este impar {lista[i]}")
#         else:
#             print(f"Elementul: {lista[i]} nu este un numar intreg")
# #             continue
#
# lista_numere = [-2,5, 4, 3, 5, 9, "3,5", "ala bala"]
#
# verifica_lista_numere(lista_numere)



# # implementation 2
# def verifica_lista_numere(lista):
#     for i in range(len(lista)):
#         if not isinstance(lista[i], int):
#             print(f"elementul: {lista[i]} nu este un numar intreg")
#             continue
#         if lista[i] % 2 == 0:
#             print(f"numarul este par {lista[i]}")
#         else:
#             print(f"numarul este impar {lista[i]}")
#
# lista_numere = [-2,5, 4, 3, 5, 9, "3,5", "ala bala"]
#
# verifica_lista_numere(lista_numere)



"""
EX3: Scrie o functie care calculeaza patratul unui numar.
Afiseaza rezultatul.
"""

triggered_function()

# def patratul_unui_numar(numar):
#     patrat = numar ** 2     # <=> numar * numar
#     print(f"Patratul numarului {numar} este: {patrat}")
#
# patratul_unui_numar(5)



"""
EX4: Scrie o functie care calculeaza impartirea dintre doua numere.
Afiseaza rezultatul.
"""

triggered_function()

# def impartire_doua_numere(x, y):
#     impartire = x / y   # '/' = true division (floating-point result) AND '//' = floor division (integer result, rounding down)
#     # print(f"Rezultatul impartirii dintre numerele [{x}] si [{y}] este: [{impartire}]")
#     print(f"[{x}] impartit la [{y}] este: [{impartire}]")
#
# impartire_doua_numere(10, 2)



"""
EX5: Scrie o functie care calculeaza inmultirea dintre doua numere.
Afiseaza rezultatul.
"""

triggered_function()

# def inmultire_doua_numere(x, y):
#     inmultire = x * y
#     print(f"[{x}] inmultit cu [{y}] este: [{inmultire}]")
#
# inmultire_doua_numere(10, 2)



"""
EX6: Rescrie functia de la exercitiul 3, 
astfel incat sa returneze rezultatul.
"""

triggered_function()

# def patratul_unui_numar2(numar):
#     patrat = numar ** 2     # <=> numar * numar
#     return numar ** 2
#
# # print(patratul_unui_numar2(5))
# print(f"Patratul este {patratul_unui_numar2(5)}")



"""
EX7: Rescrie functia de la exercitiul 4, 
astfel incat sa returneze rezultatul.
"""

triggered_function()

# def impartire_doua_numere(x, y):
#     impartire = x / y
#     return impartire
#     # return print(impartire)    # IT WORKS ! - NOT TO BE USED
#
# print(impartire_doua_numere(10, 2))
# # impartire_doua_numere(10, 2)



"""
EX8: Scrie o functie care ia ca parametru un numar intreg
si returneaza True daca numarul e par
si False daca numarul e impar.
"""

triggered_function()


# def numar_intreg(numar: int):
# # if isinstance(numar, int):
#     if numar % 2 == 0:
#         return True
#     else:
#         return False
#
# print(numar_intreg(13))






# tema: 7, 5, 4 - DONE
