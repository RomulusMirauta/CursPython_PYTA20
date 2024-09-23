"""
Sesiunea 3 - Exercitii cu Trainer
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
1. Citeste de la tastatura:
- lungimea unui dreptunghi
- latimea unui dreptungi

Calculeaza aria si afiseaz-o in consola astfel:
    'Aria dreptunghiului este x.'
"""

triggered_function()

# lungime = int(input('Introduceti de la tastatura lungimea dreptunghiului: '))
# latime = int(input('Introduceti de la tastatura latimea dreptunghiului: '))
#
# print('Aria dreptunghiului este: ', lungime * latime)



"""
2. Avand string-ul:
'Coral is either the stupidest animal or the smartest rock':
- Afiseaza de cate ori apare cuvantul 'the'.
"""

triggered_function()

# string = 'Coral is either the stupidest animal or the smartest rock'
# print(f"Cuvantul 'the' apare de ", string.count('the'), " ori")




"""
lucru pe grupe
de comentat fiecare linie de cod

grupa 1
exercitii: 3
15min
apoi, 7
"""










"""
3. Folosind string-ul de la exercitiul 2:
- Afiseaza in consola daca acest string contine doar numere.
"""

triggered_function()

# str = 'Coral is either the stupidest animal or the smartest rock'     # declaram si initializam variabila "str"
# print("Variabila 'str' contine doar numere? Raspuns: ", string.isdigit())         # printam un text + ne folosim de functia de .isdigit() pentru a afla daca in str avem doar numere,
                                                                      # iar rezultatul apelarii functiei este False; afisam rezultatul
# cu ajutorul functiei print afisam un mesaj in consola, in care spunem utilizatorului daca string-ul nostru are doar numere, iar output-ul va fi False






"""
4. Citeste de la tastatura un string de dimensiune impara.
Afiseaza caracterul din mijloc.
"""

triggered_function()



# if lungime % 2 == 1
# <=>
# if lungime % 2 != 0





"""
5. Folosind o singura linie de cod, citeste un string de la tastatura (ex: 'alabala portocala')
si salveaza fiecare cuvant intr-o variabila.
- Afiseaza in consola ambele variabile pentru verificare.
"""

triggered_function()

# x, y = input("Introduceti doua cuvinte de la tastatura: ").split()
#
# print(f"primul cuvant este: {x}")
# print(f"al doilea cuvant este: {y}")






"""
6. 
a. Citeste o litera de la tastatura.
b. Verifica si afiseaza daca este vocală sau nu.
"""

triggered_function()

# a , e , i , o, u
# litera = input('Scrie o litera: ')
# in variabila litera salvam datele de la tastatura cu ajutorul functiei input
# cu ajutorul structurii if else verificam daca litera este vocala sau consoana si cu ajutorul functiei lower transformam stringul sa contina doar caractere mici
# if litera.lower() == 'a':
#     print('Litera este o vocala.')
# elif litera.upper() == 'E':
#     print('Litera este o vocala.')
# elif litera.lower() == 'i':
#     print('Litera este o vocala.')
# elif litera.lower() == 'o':
#     print('Litera este o vocala.')
# elif litera.lower() == 'u':
#     print('Litera este o vocala.')
# else:
#     print('Litera este o consoana.')










"""
7. Transforma si printeaza notele din sistem romanesc in:
 - Peste 9 => A
 - Peste 8 => B
 - Peste 7 => C
 - Peste 6 => D
 - Peste 4 => E
 - 4 sau sub => F
"""

triggered_function()

# nota = int(input("Introdu nota: "))    # declaram si initializam variabila "nota" cu date introduse de la tastatura, fortand tipul de int
# if nota > 9:                           # folosim un flow control (if), conditie (nota > 9)
#     print('Nota A este din sistemul romanesc este egala cu 10')                         #
# elif nota > 8:
#     print('B')
# elif nota > 7:
#     print('C')
# elif nota > 6:
#     print('D')
# elif nota > 4:
#     print('E')
# elif nota <= 4:
#     print('F')
# else:
#     print("Nota introdusa este incorecta!")






"""
8. 
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x are minim 4 cifre.

(Exemplu: 7895 are 4 cifre, 10 nu are minim 4 cifre)
"""

triggered_function()

# x = int(input("Introdu valoare lui x: "))
#
# if len(str(x)) >= 4:
#     print("x are minim 4 cifre")
# else:
#     print("x NU are minim 4 cifre")




"""
9.
a. Citeste un numar intreg, x, de la tastatura.
b. Verifica daca x este numar par sau impar.
"""

triggered_function()

# x = int(input("Introdu valoare lui x: "))
#
# if x == 0:
#     print("x este numar neutru")    # 0 nu este nici par, nici impar
# elif x % 2 == 0:
#     print("x este numar par")
# else:
#     print("x este numar impar")



"""
10. 
a. Citeste trei numere intregi, x, y, z, de la tastatura,
care sa reprezinte unghiurile unui triunghi.
b. Verifica si afiseaza daca triunghiul este valid sau nu.
"""

triggered_function()

# x = int(input("Introdu valoare lui x: "))
# y = int(input("Introdu valoare lui y: "))
# z = int(input("Introdu valoare lui z: "))
#
# if x + y + z == 180 and 0 < x < 180 and 0 < y < 180 and 0 < z < 180:
#     print("Triunghiul este valid")
# else:
#     print("Triunghiul NU este valid")


"""
11. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock':
a. Citește de la tastatura un numar intreg, x.
b. Afiseaza string-ul fara ultimele x caractere.

Exemplu: dacă ai ales 7 => 'Coral is either the stupidest animal or the smarte'
"""

triggered_function()

# string = 'Coral is either the stupidest animal or the smartest rock'
#
# x = int(input("Introdu valoare lui x: "))
#
# print(string[:(len(string)-x):1])



"""
12. Avand string-ul: 'Coral is either the stupidest animal or the smartest rock': 
a. Salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
(hint: este o metoda ajutatoare care te ajuta sa faci asta)

b. Folosind variabila de la punctul a + slicing, afiseaza tot string-ul pana la acest cuvant
"""

triggered_function()

# string = 'Coral is either the stupidest animal or the smartest rock'
#
# index_rock = string.find('rock')
# print(index_rock)
#
# print(string[:(index_rock):])


"""
13. Joc ghicit zarul
Cauta pe internet si vezi cum se genereaza un numar random.

Ne imaginam ca dai cu zarul si salvam acest numar in dice_roll.
Ia numarul ghicit de la utilizator.
Verifică si afiseaza daca utilizatorul a ghicit.
Vei avea 3 optiuni:
    - Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y.
    - Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y.
    - Ai ghicit. Felicitari! Ai ales x si zarul a fost y.
"""

triggered_function()

# import random
#
# dice_roll = random.randint(1, 6)
# numar_utilizator = int(input("Ghiceste un numar de la 1 la 6: "))
# if numar_utilizator < dice_roll:
#     print(f"Ai pierdut. Ai ales un numar mai mic. Ai ales {numar_utilizator} dar a fost {dice_roll}.")
# elif numar_utilizator > dice_roll:
#     print(f"Ai pierdut. Ai ales un numar mai mare. Ai ales {numar_utilizator} dar a fost {dice_roll}.")
# else:
#     print(f"Ai ghicit. Felicitari! Ai ales {numar_utilizator} si zarul a fost {dice_roll}.")



"""
14.  
a. Citeste de la tastatura un string.
b. Verifica daca primul si ultimul caracter sunt la fel, si afiseaza un mesaj sugestiv pentru fiecare caz.

ATENTIE: se doreste ca programul sa fie case insensitive - 'apA' e acceptat
"""

triggered_function()

# text = input("Introduceti un string: ")
# print(text)
# text = text.lower()
# print(text)
# if text[0] == text[-1]:
#     print("Primul si ultimul caracter sunt la fel.")
# else:
#     print("Primul si ultimul caracter NU sunt la fel.")

# TEST TEXT:
# acum avem un string a
# AcUm AvEm Un StRiNg a



"""
15.
BONUS: Nested ifs
Link: https://docs.google.com/presentation/d/1nWzcLprYoN4M3DIobhnFJpI85q_y4B7t/edit#slide=id.p45 - "Ex 14"

Citește de la tastatura varsta utilizatorului.
Spune-i utilizatorului dacă are drept de vot în România. Ia de la utilizator orice alte date necesare.
Condiții drept de vot:
- utilizatorul are drept de vot dacă este mai mare de 18 ani.
- utilizatorul are drept de vot dacă locuiește în RO.
"""

triggered_function()

# varsta = int(input("Introduceti varsta: "))
# cetatenie = input("Esti cetatean roman? ")
# cetatenie = cetatenie.capitalize()
# if varsta >= 18 and cetatenie == "Da":
#     print("Ai drept de vot!")
# else:
#     if varsta < 18:
#         print("Nu ai drept de vot, deoarece nu esti major!")
#     elif cetatenie != "Da":
#         print("Nu ai drept de vot, deoarece nu esti cetatean roman!")



"""
16.
TEMA: de incercat ex 13 din PPT

Exercitiul 13:  - tema 

Citește de la tastatura nr de ore lucrate de un angajat într-o saptamana.
Tinand cont ca numărul de ore standard de munca dintr-o saptamana este 40,
si se considera overtime ce e peste 40 de ore, afișează bonusul pe care angajatul îl primește
și un mesaj sugestiv, tinand cont de următoarele criterii:
bonusul este de 50 de lei dacă angajatul a lucrat între 40 și 50 de ore.
bonusul este de 100 de lei dacă angajatul a lucrat mai mult de 50 de ore.
dacă s-a lucrat nr de ore standard, angajatul nu e eligibil pentru bonus.
"""

triggered_function()

# # implementare 1
# ore_muncite = int(input("Introduceti nr zile lucrate: "))
# if ore_muncite < 40:
#     print(f'Ai lucrat {ore_muncite} ore, mai putine ore decat nr standard')
# elif 40 < ore muncite <= 50:
#     print(f"Ai lucrat {ore_muncite} ore si primesti 50 ron bonus")
# elif ore_muncite > 50:
#     print(f"Ai mumcit {ore_muncite} ore si primesti 100 ron bonus")
# else:
#     print('Ai muncit nr standard de ore')



# # implementare 2
# ore_muncite = int(input("Introduceti nr zile lucrate: ")) # variabila pentru date introduse
# ore_standard = 40
# if ore_standard < ore_muncite:
#     if ore_muncite <= 50:
#         bonus_angajat = 50
#         print(f"Ai muncit {ore_muncite} ore si primesti un bonus de {bonus_angajat} lei")
#     else:
#         bonus_angajat = 100
#         print(f"Ai muncit {ore_muncite} ore si primesti un bonus de {bonus_angajat} lei")
# else:
#     bonus_angajat = 0
#     print(f"Ai muncit {ore_muncite} ore si primesti un bonus de {bonus_angajat} lei")
