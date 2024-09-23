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
1. Lista de cumparaturi:

Se citeste de la tastatura o lista de cumparaturi. 
Utilizatorul introduce lista de cumparaturi ca un string,
cu alimentele separate prin virgula,
ATENTIE: fara spatii
Exemplu:rosii,castraveti,branza,oua

a. Sa se transforme string-ul citit de la tastatura intr-o lista. (vezi metode ajutatoare string).
b. Sorteaza lista de cumparaturi si printeaza lista sortata.
c. Adauga un aliment nou in lista de cumparaturi.
d. Sterge un aliment din lista de cumparaturi.
e. Modifica elementul de la pozitia 0 din lista.
f. Daca lista contine 'rosii' in ea, afiseaza mesajul "Aliment sanatos".
Daca nu, afiseaza mesajul "Iti recomandam rosiile de asemenea".
"""

triggered_function()

# cumparaturi = input("Introduceti lista de cumparaturi: \n").lower().split(",")
#
# print(cumparaturi)
#
# # cumparaturi = list(cumparaturi)
# # print(cumparaturi)
# # print(cumparaturi[0])           # IS THIS OK ???
#
# cumparaturi.sort()
# print(cumparaturi)
#
# produs_adaugat = input("Adauga un produs in lista: \n")
# cumparaturi.append(produs_adaugat.lower())
# # cumparaturi.append(("rosii"))
# print(cumparaturi)
#
# produs_sters = input("Sterge un produs din lista: \n")
# cumparaturi.remove(produs_sters.lower())
# # cumparaturi.remove("apa")
# print(cumparaturi)
#
# produs_modificat = input("Modifica primul produs din lista: \n")
# cumparaturi[0] = produs_modificat.lower()
# # cumparaturi[0] = "otet"
# print(cumparaturi)
#
# if 'rosii' in cumparaturi:
#     print("Aliment sanatos")
# else:
#     print("Iti recomandam rosiile de asemenea")
#
#
# # apa,castraveti,branza,oua
# # APA,CASTRAVEVTI,BRANZA,OUA





"""
2. Se da lista fructe = ['capsuni', 'mere', 'lamai'].
Converteste lista la string si afiseaza string-ul.
A se vedea metoda join().
"""

triggered_function()

# list_fructe = ['capsuni', 'mere', 'lamai']
#
# string_fructe = ", ".join(list_fructe)
# print("Lista este convertita la sirul de caractere", string_fructe)



"""
3. Se da lista numere = [1, 2, 3, 4, 56, 22, 5].
Afiseaza elementul cu valoarea maxima din string. (google- functia max()) # greseala string --> lista
"""

triggered_function()

# lista_numere = [1, 2, 3, 4, 56, 22, 5]
#
# print(max(lista_numere))



"""
4. Se da lista preturi = [12.3, 34.5, 22].
Calculeaza suma elementelor din lista preturi. (google - functia sum())
"""

triggered_function()

# lista_preturi = [12.3, 34.5, 22]
#
# print(sum(lista_preturi))


"""
5. Se da dictionarul:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
a. Afiseaza valoarea cheii city.
b. Kelly a fost promovata. Salariul ei este acum de 10000 lei. Fa modificarea si in dictionar.
c. Sterge varsta din dictionar.
d. Adauga o noua pereche cheie-valoare in dictionar, cu cheia employment_date. Valoarea o alegi tu.
e. Verifica daca exista cheia 'country' in dictionar. Daca nu exista, adauga-o.
"""

triggered_function()

# sample_dict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# print(sample_dict["city"])
#
# # sample_dict["salary"] = 10000
# sample_dict.update({"salary": 10000})
# # print(sample_dict["salary"])
#
# # sample_dict.pop("age")
# del sample_dict["age"]
# # print(sample_dict["age"])
#
# sample_dict["employment_date"] = "18.05.2021"
# # print(sample_dict["employment_date"])
# # print(sample_dict)
#
# if 'country' in sample_dict.keys():
#     print("Cheia 'country' exista in dictionar")
# else:
#     sample_dict["country"] = "Germany"
#
# # print(sample_dict)




"""
6. Concatenarea a doua dictionare

Se dau doua dictioanare:
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

Sa se concateneze cele doua dictionare folosind metoda update().
Observatie: Metoda update() o putem folosi pentru a adauga unul sau mai multe
perechi cheie:valoare in dictionar.
"""

triggered_function()

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'c': 3, 'd': 4}
#
# dict_concatenate = {}
#
# dict_concatenate.update(dict1)
# dict_concatenate.update(dict2)
#
# print(dict1)
# print(dict2)
# print(dict_concatenate)




"""
7. Se da urmatoarea lista cu dictionare:
lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
a. Adauga perechea {'c':'3'} in primul dictionar din lista.
b. Adauga un nou dictionar ca element in lista. Adauga-l la final.
c. Aduaga un nou dictionar ca element in lista, la indexul 1.
d. Verifica daca in al doilea dictionar din lista se gaseste cheia 'c'.
"""

triggered_function()

# lista = [{'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}]
#
# lista[0]['c'] = 3   # ~add
# lista[0]['c'] = 5   # ~update
# print(lista)
#
# lista.append({'e': 2, 'g': 5})
# print(lista)
#
# lista.insert(1, {'b': 6, 'd': 4})
# print(lista)
#
# if 'c' in lista[1].keys():
#     print("\n Cheia 'c' este in al doilea dictionar")
# else:
#     print("\n Cheia 'c' nu a fost gasita")
