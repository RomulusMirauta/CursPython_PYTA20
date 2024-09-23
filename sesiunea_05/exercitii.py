"""
Rezolvari exercitii sesiunea 5
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
EX1: Se da numarul x = -5.
Foloseste un while pentru a afisa numerele negative pornind
de la -5.
La final, afiseaza un mesaj ca s-au afisat toate numerele
negative.
"""

triggered_function()

# x = -5
#
# while x < 0:
#     print(x)
#     x += 1
# print("S-au afisat toate numerele negative")



"""
EX2: Calcularea mediei
Ne dorim sa cerem utilizatorului sa introduca notele
luate la examene. 
Vom lua input-ul de la utilizator, pana
cand acesta introduce -1.
In functie de notele luate, trebuie sa calculam media aritmetica
si sa o afisam.
"""

triggered_function()

# note_utilizator = []
# nota_utilizator = 0
#
# while nota_utilizator != -1:
#     nota_utilizator = int(input("Introdu nota: "))
#     if nota_utilizator > 0 and nota_utilizator <= 10:
#         note_utilizator.append(nota_utilizator)
#
# print(note_utilizator)
#
# if len(note_utilizator) != 0:
#     media = sum(note_utilizator)/len(note_utilizator)
#     print("Media aritmetica este: ", media)
# else:
#     print("Nu avem note introduse.")



"""
EX3: Afiseaza toate numerele pare pana la 10.
"""

triggered_function()

# for numar in range(0, 10, 2):
#     print(numar)



"""
EX4: Se da lista:
legume = ['spanac', 'castraveti', 'conopida', 'ardei']
Afiseaza toate elementele din lista accesandu-le dupa index.
"""

triggered_function()

# legume = ['spanac', 'castraveti', 'conopida', 'ardei']
# lungime_lista = len(legume)
# for i in range(lungime_lista):
#     print(legume[i])




"""
EX5:
2. Se da lista:
produse = [
    {
        'nume produs': 'Rosii',
        'pret': 5
    },
    {
        'nume produs': 'Paine',
        'pret': 8
    },
    {
        'nume produs': 'Lapte',
        'pret': 6
    },
    {
        'nume produs': 'Cafea'
    }
]
Sa se afiseze toate produsele care au pretul mai mare de 5 lei.
"""

triggered_function()

# produse = [
#     {
#         'nume produs': 'Rosii',
#         'pret': 5
#     },
#     {
#         'nume produs': 'Paine',
#         'pret': 8
#     },
#     {
#         'nume produs': 'Lapte',
#         'pret': 6
#     },
#     {
#         'nume produs': 'Cafea'
#     }
# ]
#
# for produs in produse:
#     # print(produse)
#     if "pret" in produs.keys() and produs["pret"] > 5:
#         print(produs["nume produs"])
#         # break


"""
EX6: Sa se afiseze primul numar par din intervalul 1 - 10
(inclusiv capetele de interval).
"""

triggered_function()

# numere = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for i in range(1, 11): # if range(1, 10) => inclusiv 1, inclusiv 9
#     if (i % 2) == 0:
#         print(numere[0])
#         print(i)
#         print(numere[9])
#         break




"""
EX7:
Se da lista:
participanti = ['Maria', 'Ionela', 'Marius', 'Paul']
Folosind un ciclu repetitiv, cauta daca 'Marius' se afla in lista de participanti.
Dupa ce l-ai gasit intrerupe ciclul repetitiv.
"""

triggered_function()

participanti = ['Maria', 'Ionela', 'Marius', 'Paul']

# i = 0

# print(participanti[i])

# for participant in participanti:
#     if participanti[i] == 'Marius':
#         print('L-am gasit pe Marius!')
#         break
#     i += 1
#     # break     # NOT HERE !!!



# # BETTER IMPLEMENTATION
# for participant in participanti:
#     if participant == 'Marius':         #  participant is the loop variable that takes on each value in the list as the loop iterates
#         print('L-am gasit pe Marius!')
#         break





"""
EX8: 1. Se da lista:
numere = [1, 2, 3, 4, 5, 6, 7]
Afiseaza toate elementele din lista numere,
cu exceptia numerelor 3 si 5
"""

triggered_function()

# numere = [1, 2, 3, 4, 5, 6, 7]
#
# for numar in numere:
#     if numar == 3 or numar == 5:
#         continue    # skips over 3 and 5
#     print(numar)
#     # continue    # NOT HERE !!!









print("-" * 150 + "\n" * 2)
print("OUTPUT PENTRU [ EXEMPLE - CURS ] \n")


# # Exemplul 1 - Afisarea numerelor de la 0 la 3
# i = 0
#
# while i <= 3:
#     print(i)
#     i += 1



# Exemplul 2 - Afisarea numerelor pozitive
# x = 8
# while x > 0:
#     print(f"Numarul {x} este pozitiv")
#     x -= 1
# print("S-a iesit din while")
# print(f"Dupa while, x are valoarea {x}")



# # Exemplul 3 - validarea credentialelor de conectare
# username = input("Introduceti numele de utilizator: ")
# password = input("Introduceti parola: ")
#
# while len(username) < 6 and len(password) < 6:
#     print("Usernamel-ul si parola trebuie sa aiba min 6 caractere!")
#     username = input("Introduceti numele de utilizator: ")
#     password = input("Introduceti parola: ")
# print("Autentificare reusita")


# # Exemplul 4 - ghicirea unui numar introdus la tastatura
# import random
#
# secret_number = random.randint(1, 10)
#
# guessed = False
#
# while not guessed:
#     guess_number = int(input("Alege un numar de la 1 la 10: "))
#     if guess_number == secret_number:
#         print("Felicitari! Ai ghicit!")
#         guessed = True # conditia de iesire
#     elif guess_number < secret_number:
#         print("Numarul este prea mic. Incercati din nou.")
#     else:
#         print("Numarul este prea mare. Incercati din nou.")
# else:
#     print("ACESTA ESTE ELSE-UL BUCLEI WHILE => S-A IESIT DIN BUCLA")
# # OPTIONAL: La final, se poate pune un else. Blocul de cod din else se va executa mereu 1 data, la final, atata timp cat ciclul repetitiv nu este intrerupt intentionat



# # Exemplul 3 - Cautarea unui element intr-o lista
# numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
#
# search_value = int(input("Ce numar cautati? "))
#
# index = 0
# while index < len(numbers):
#     if numbers[index] == search_value:
#         print(f"Valoarea a fost gasita la indexul: {index}")
#         break
#     index += 1
# else:
#     print("Valoarea nu a fost gasita in lista!")




# 📌 FOR/FOR ELSE - executam codul de un anumit numar de ori

# 📌 FOR EACH - executam cod pentru fiecare element dintr-o structura de date


# for i in range(4):                                    # FOR
#     print(i)
# else:
#     print("Am terminat.")


# culori = ["rosu", "albastru", "galben", "mov"]
#
# for culoare in culori:                                  # FOR EACH
#     print(f"Culoarea mea preferata este {culoare}")



# for i in range(1, 50):
#     if i == 3:
#         break
#     print(i)

# for i in range(1, 50):
#     if i == 3:
#         print(i)
#     # print(i)

# for i in range(1, 50):
#     if i == 3:
#         continue     # skipping over '3'
#     print(i)



# for i in range(5):
#     if i == 3:
#         continue    # continue ~= skip => it skips over '3'
#     print(i)




# # 📌 FOR EACH
# # Iterating over a list of names
# names = ['Alice', 'Bob', 'Charlie']
#
# for name in names:  # Iterates directly over elements
#     print(name)
#
#
# # 📌 FOR CLASSIC
# # Iterating over a list of names
# names = ['Alice', 'Bob', 'Charlie']
#
# for i, name in enumerate(names):  # `i` gives the index, `name` gives the element
#     print(f"Index {i}: {name}")   # If you need to access the index while iterating (which would require a traditional for loop in other languages), you can use the enumerate() function.

#
# nota_utilizator = 0
# note_utilizator = []
#
# while nota_utilizator != -1:
#     nota_utilizator = int(input("Introdu nota: "))
#     if nota_utilizator > 0 and nota_utilizator <= 10:
#         note_utilizator.append(nota_utilizator)
# else:
#     print("Ati introdus -1")






# print()
# #iteram printr-un dictionar folosind metodele keys(), respectiv value()
# dic_pitici_s = {
#     "piticul 1": "Bucurosul",
#     "piticul 2": "Rusinosul",
#     "piticul 3": "Mutulica",
#     "piticul 4": "Morocanosul",
#     "piticul 5": "Hap-Ciu",
#     "piticul 6": "Inteleptul",
#     "piticul 7": "Somnorosul"
# }
# for keys in dic_pitici_s.keys():  #acesta versiune va itera prin cheile dic. si va afisa valoarea aferenta fiecarei chei
#     print(keys)
#     print(dic_pitici_s[keys])

# print("---" * 5)
#
# dic_pitici_i = {
#     1: "Bucurosul",
#     2: "Rusinosul",
#     3: "Mutulica",
#     4: "Morocanosul",
#     5: "Hap-Ciu",
#     6: "Inteleptul",
#     7: "Somnorosul"
# }
# # for value in dic_pitici_i.values(): #acesta versiune va itera prin valorile dic. si va afisa fiecare valoare
# #     print(value)
# #
# def range_dict(dic_pitici_i):
#     for i in range(len(dic_pitici_i)): #aceasta versiune ne va oferi valori incepand de la 0 pana la elementele din dictionar, i va fi folosit ca un index pt a accesa valorile
#         print(dic_pitici_i[i+1]) #adaugam +1 deoarece cheile dintr-un dictionar incep de la 1
#
# range_dict(dic_pitici_i)
#
# print("done")
#
# # => printeaza valorile by default (values not used)






# #Exercitiu: vrem sa calculam suma numerelor impare
# suma = 0  # initializam variabila suma
# for i in range(0, 11): #folosim bucla for pt a itera prin nr de la 0 la 10
#     if i % 2 == 0: #verificam daca nr este impar, adica daca restul(folosim operatorul % - modulo) impartirii la 2 este 0 atunci nr este par
#         print(f"Numar par: {i}")
#         continue #si trece la urmatoarea iteratie a buclei datorita acestei instructiuni
#     print(f"Numar impar: {i} - dupa if")
#     suma += i #daca i este impar atunci se adauga la suma
# print(f"Suma numerelor impare de la 0 la 10 este: {suma}") #aici printam suma nr pt intervalul dat folosind formatarea sirului de caractere











"""
Intrebari interviu:

1. Cand folosim while si cand folosim for?
2. Ce este obligatoriu sa avem in interiorului blocului de cod while?
3. Ce reprezinta functia range?
4. Cand alegem sa folosim break intr-o structura repetitiva?
5. Cand alegem sa folosim continue intr-o structura repetitiva?
6. Ce face else-ul dintr-un for/else si while/else?
7. Daca avem un while/else, in ce caz nu se va executa codul din else?
"""


"""
RASPUNSURI:

1. WHILE - A while loop is best used when the number of iterations is not known in advance, and you need to continue looping until a certain condition is met.
FOR - A for loop is best used when you know in advance how many times you want to iterate, or when you need to iterate over a sequence of elements (like a list, tuple, string or range).

2. Ce este obligatoriu sa avem in interiorului blocului de cod while? - incrementare/decrementare => care influenteaza conditia buclei (caz contrar => bucla infinita)

3. range - built-in function, generates a sequence of numbers; syntax: range(start, stop, step); by default: start = 0 (inclusiv, optional), stop = mandatory (exclusiv), step = 1 (optional)

4. break - cand avem nevoie sa oprim iteratia

5. continue - cand avem nevoie sa dam skip la o iteratie (iteratia curenta sau mai multe iteratii)

6. else-ul dintr-un for/else si while/else - este optional, iar blocul de cod din else se va executa mereu 1 data, la final

7. while/else, in ce caz nu se va executa codul din else? - codul din else va fi executat de fiecare data cand conditia nu va fi adevarata
exceptie: prezenta unui break inainte de else-ul while-ului
daca conditi va fi mereu adevarata (bucla infinita)
"""