"""
Rezolvari exercitii sesiunea 4
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
EX1: 
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""

triggered_function()

# lista = ['apa', 5, True]
#
# # Da, lista este o structura de date ordonata, pentru ca elementele sunt pastrate in ordinea in care au fost adaugate
# # => fiecare element din lista are un index => putem accesa un element specific folosind acel index
#
# print(lista[1])
#
# print(len(lista))



"""
EX2:
a. Defineste o lista numita filme_preferate, cu cel putin 3 elemente.
b. Inverseaza lista folosind slicing. (ca la string)
c. Folosind if, verifica daca lista este goala sau nu,
si afiseaza un mesaj corespunzator pentru fiecare situatie.
"""

triggered_function()

# filme_preferate = ["Titanic", "Avatar", "Cenusareasa"]
# print(filme_preferate)
#
# lista_filme_preferate_inversate = filme_preferate[::-1]
# print(lista_filme_preferate_inversate)
#
# if len(filme_preferate) == 0:
#     print("Lista este goala")
# else:
#     print("Lista are elemente")


"""
EX3: Se da structura de date cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8].
a. Verifica tipul structurii de date dat.
b. Accesand metodele de pe lista, sorteaza lista cifre.
c. Verifica daca 9 este in lista cifre. Afiseaza un mesaj corespunzator.
"""

triggered_function()

# cifre = [0, 6, 3, 4, 1, 2, 5, 7, 8]
#
# # print(type(cifre))
#
# # b.
# print(cifre)

# temp = 0

# cifre_ord = []

# print("\n INCEPE ORDONAREA ! \n")

# i = 0

# IT WORKS !!!

# for cifra in cifre:
#     cifre_ord.insert(i, max(cifre) - i)
#     print(cifre_ord)
#     i += 1
#
# print(cifre_ord[::-1])



# CHEATING

# cifre_ord = sorted(cifre)
# print(cifre_ord)





# TRY 5
# for cifra in range(1, 20):
#     if cifre[i] == max(cifre):
#         print("Found MAX !!!")
#         cifre_ord.append(cifre[i])
#         temp = cifre[i]
#         cifre[i] = cifre[i + 1]
#         print(cifre)
#         # if temp > cifre[i + 2]:
#     # else:
#         # temp = cifre[i]
#         # print(cifre)
#     i += 1
#
# print(cifre_ord)


# TRY 4
# i = 0
#
# # cifre = str(cifre)
#
# for cifra in cifre:
#     # cifre_ord.append(cifre[max(cifre)-i])
#     # cifre_ord.insert(i, cifre[max(cifre)-i])        # [8, 7, 5, 2, 1, 4, 3, 6, 0]     WRONG !
#     cifre_ord.insert(i, max(cifre) - i)               # [8, 7, 6, 5, 4, 3, 2, 1, 0]
#     # cifre_ord.insert(i, int(cifre[max(cifre)-i]))
#     print(cifre_ord)
#     i += 1
#
# # print(cifre_ord)
#
#
# # cifre_ord.insert(i, cifre[max(cifre)-i])        # cifre_ord.insert(0, cifre[max(cifre)-0]) <=> cifre_ord.insert(0, cifre[max(cifre)]) <=> cifre_ord.insert(0, cifre[8])


# TRY 3
# temp = 0
#
# cifre_ord = []
#
# i = 0
#
# for cifra in range(1, 20):
#     if cifre[i] > cifre[i + 1]:
#         cifre_ord.append(cifre[i])
#         temp = cifre[i]
#         cifre[i] = cifre[i + 1]
#         print(cifre)
#         # if temp > cifre[i + 2]:
#     # else:
#         # temp = cifre[i]
#         # print(cifre)
#     i += 1
#
# # print(cifre_ord)


# TRY 2
# temp = 0
#
# cifre_ord = []
#
# for cifra in cifre:
#     if cifre[0] > cifre[1]:
#         cifre.append(cifre[0])
#     else:
#         temp = cifre[0]


# TRY 1
# temp = 0
#
# cifre_ord = []
#
# i = 0
#
# for cifra in cifre:
#     # i += 1
#     if cifre[i] == i:
#         cifre_ord.append(cifre[i])
#     else:
#         temp = cifre[i]
#     i += 1
#
# print(cifre_ord)


# c.
# if 9 in cifre:
#     print("9 se afla in lista cifre")
# else:
#     print("9 NU se afla in lista cifre")



"""
EX4: Defineste o lista si exploreaza metodele ajutatoare ale listelor. 
"""

triggered_function()

fruits = ['apple', 'banana', 'cherry', 'date']
print(fruits)
print(len(fruits))

fruits[1] = 'pineapple'
print(fruits)

fruits.append('apple')
print(fruits)

print(len(fruits))

print(fruits[2])

fruits.insert(0, 'kiwi')
print(fruits)

fruits.pop()
print(fruits)

element_sters = fruits.pop(0)
print(element_sters)
print(fruits)

fruits.remove('apple')
print(fruits)

fruits.remove('date')
print(fruits)



"""
EX5: Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""

triggered_function()

# my_set = {1, 2, 3, 4}
# print(my_set)
#
# my_set.add(5)
# print(my_set)
#
# my_set.add(6)
# print(my_set)
#
# my_set.add(1)
# print(my_set)   # Set-urile pastreaza doar elementele UNICE
#
# my_set.remove(3)
# print(my_set)
#
# my_set.pop()
# print(my_set)



"""
EX6:
Se da urmatoarea structura de date:
locatie = (44.34, 12.456)
a. Verifica tipul structurii de date
b. Este aceasta structura de date ordonata?
c. Este aceasta structura de date mutabila?
d. Determina lungimea structurii de date.
e. Salveaza a doua valoare intr-o variabila.
Verifica daca aceasta este mai mare de 13, si afiseaza
un mesaj corespunzator.
"""

triggered_function()

# locatie = (44.34, 12.456)
# print(type(locatie))
#
# # este ordonata
#
# # nu este mutabila
#
# print(f"Lungimea structurii de date din variabila locatie este de: {len(locatie)} elemente ")
#
# var_2 = locatie[1]
#
# if var_2 > 13:
#     print("Variabila este mai mare decat 13")
# else:
#     print("Variabila este mai mica decat 13")





"""
EX7: 
a. Defineste un dictionar, numit student1, cu urmatoarele chei:
nume, prenume, varsta, an_studiu, facultate, medie. 
Valorile le alegi tu.
b. Afiseaza lungimea dictionarului.
c. Printeaza prenumele studentului.
d. Adauga o noua pereche cheie-valoare, cu tara in care studiaza studentul.
e. Verifica daca dictionarul contine cheia oras.
"""

triggered_function()

student1 = {
    'nume': 'Popescu',
    'prenume': 'Andrei',
    'varsta': 29,
    'an_studiu': 3,
    'facultate': 'Inginerie',
    'medie': 9.90
}

print(len(student1))

print(student1['prenume'])

print(student1)
student1['tara'] = 'Romania'
print(student1)

if 'oras' in student1.keys():
    print("Dictionarul contine cheia oras")
else:
    print("Dictionarul NU contine cheia oras")



"""
EX8:
a. Citeste de la tastatura urmatoarele date legate de o noua reteta: nume, ingrediente,
timp prepapare.
b. Salveaza datele citite intr-un dictionar.
c. Actualizeaza numele retetei, scriind-ul cu litere mari.
"""

triggered_function()

# nume = input("Scrie numele retetei: ")
# ingrediente = input("Scrie ingredientele: ")
# timp_preparare = input("Scrie timpul de preparare: ")
#
# reteta = {
#     'nume': nume,
#     'ingrediente': ingrediente,
#     'timp_preparare': timp_preparare
# }
#
# print(reteta)
#
# # reteta["nume"] = nume.upper()
# # <=>
# reteta['nume'] = reteta["nume"].upper() # Cristina
# print(reteta)


# diferente ??





"""
EX9:
a. Se da un dictionar cu contacte din agenda telefonica:
contacte = {'Maria': '0722898956', 'Aurel': '0755342298'}
b. Aurel si-a schimbat numarul de telefon. Actualizeaza-l.
c. Ai obtinut numarul de telefon a lui Mihai. Adauga-l in contacte.
d. Maria a plecat in strainatate si nu mai are numar de telefon. Sterge-l.
e. Verifica daca ai numarul Mihaelei si afiseaza un mesaj corespunzator.
"""

# 7 si 9 pentru luni


triggered_function()

contacte = {
    'Maria': '0722898956',
    'Aurel': '0755342298'
}

print(contacte)
contacte.update({'Aurel': '0755555555'})
print(contacte)

contacte['Mihai'] = '0757888555'
print(contacte)

del contacte['Maria']
print(contacte)

if 'Mihaela' in contacte.keys():
    print("Ai numarul Mihaelei.")
else:
    print("NU ai numarul Mihaelei.")

