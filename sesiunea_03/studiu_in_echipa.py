"""
EXERCITII WORKSHOP (Sesiunea 3)
"""


# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------

def create_triggered_function():        # definim functia "create_triggered_function"
    call_count = 0                      # defineste variabila locala call_count si o initializeaza cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function" este apelata
        print()                         # printam un rand liber
        print()
        print("-" * 150)
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
1.
a. Citeste un string de la tastatura (ex: alabala portocala).
b. Salveaza primul caracter intr-o variabila - indiferent care este el, incearca cu 2 string-uri diferite.
c. Capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter => alAbAlA portocAla.
"""

triggered_function()

# alAbAlA portocAla

# random_string = input('Introduceti un string: ')
# var1 = random_string[0]
# var2 = var1.capitalize()
# random_string_1 = random_string.replace(var1, var2)
# print(random_string_1)
#
# primul_caracter = random_string[0]
# ultimul_caracter = random_string[-1]
# prinul_caracter = primul_caracter.lower()
# ultimul_caracter = ultimul_caracter.lower()
# caractere_mijloc = random_string_1[1:-1]
# print(caractere_mijloc)
#
# text_modificat = primul_caracter + caractere_mijloc + ultimul_caracter
# print(f"Raspuns final: {text_modificat}")







# de implementat o alta solutie folosind cicluri repetitive - for






"""
2.
a. Citeste un username de la tastatura.
b. Citeste o parola.
c. Afiseaza: 'Parola pentru user-ul x este ***** și are x caractere'.
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect.

Exemple:
- parola 'abc' => ***
- parola 'abcd' => ****
"""

triggered_function()

# username = input("Introduceti nume utilizator: ")
# password = input("Introduceti parola: ")
#
# print(f"Parola pentru user-ul {username} este {'*' * len(password)} și are {len(password)} caractere.")







"""
3. 
x, y, z - laturile unui triunghi.
Afișeaza daca triunghiul este isoscel, echilateral sau oarecare.
"""

triggered_function()

# x = input("Introduceti dimensiunea laturei 1: ")
# y = input("Introduceti dimensiunea laturei 2: ")
# z = input("Introduceti dimensiunea laturei 3: ")
#
# if (x == y != z or x == z != y or y == z != x):
#     print("Triughiul este isoscel.")
# elif (x == y == z):
#     print("Triunghiul este echilateral.")
# else:
#     print("Triunghiul este oarecare.")      # (x != y != z)






"""
4.
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x are exact 6 cifre.
"""

triggered_function()

# x = int(input("Introduceti un numar intreg: "))
#
# if len(str(x)) == 6:
#     print("Numarul intreg introdus are 6 cifre.")
# else:
#     print("Numarul intreg introdus NU are 6 cifre.")








"""
5. 
a. Citeste trei numere intregi, x, y, z, de la tastatura.
b. Afiseaza care este cel mai mare dintre ele.
"""

triggered_function()

# x = int(input("Introduceti primul numar intreg: "))
# y = int(input("Introduceti al doilea numar intreg: "))
# z = int(input("Introduceti al treilea numar intreg: "))


# # implementation1 with errors, error if 1,2,3 => max 1 ???
# if (x > y > z):
    # print(f"Cel mai mare numar introdus este: {x}")
# elif (y > x > z):
#     print(f"Cel mai mare numar introdus este: {y}")
# elif (z > x > y):
#     print(f"Cel mai mare numar introdus este: {z}")
# else:
#     print("Toate numere sunt egale.")


# # implementation2 with errors, as above
# if (x > y and y > z):
#     print(f"Cel mai mare numar introdus este: {x}")
# elif (y > x and x > z):
#     print(f"Cel mai mare numar introdus este: {y}")
# elif (z > x and x > y):
#     print(f"Cel mai mare numar introdus este: {z}")
# # else:
# #     print("Toate numere sunt egale.")



# # implementations with data structures: list

# list = [x, y, z]

# list.sort()
# print(f"Cel mai mare numar introdus este: {list[-1]}") # issues/limitations in this implementation (e.g.: 1000, 350, 2 => max = 350 ???)

# print(f"Cel mai mare numar introdus este: {max(list)}") # same issues as above

# 1 ERROR FOUND: Did not force input as integer






"""
6. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock':
Declara un string nou care sa fie format din primele 5 caractere + ultimele 5.
"""

triggered_function()

# string = 'Coral is either the stupidest animal or the smartest rock'
#
# string_nou = string[:5] + string[-5:]
#
# # print(string[:5])
# # print(string[-5:])
# # print(string_nou)


"""
7. Avand string-ul '0123456789':
- Afiseaza doar numerele pare. 
- Afiseaza doar numerele impare.

HINT: Foloseste slicing, controleaza din pas
"""

triggered_function()

string = '0123456789'

print(f"Numerele pare sunt: {string[0::2]}")
print(f"Numerele impare sunt: {string[1::2]}")






"""
EXERCITII RECOMANDATE - STUDIU INDIVIDUAL                                        .

1. Revizualizeaza sesiunile din aceasta saptamana si ia notite in caz ca ti-a scapat ceva.

2. Vizualizeaza din cursul ‘Primii pasi in Programare’ sectiunile:
- Variabile si Tipuri de date
- Operatori si Flow Control.
"""
