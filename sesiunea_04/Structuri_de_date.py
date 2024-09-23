"""
Obiective Sesiunea_4 - Structuri_de_Date
Sa stim ce sunt structurile de date
Sa intelegem cum lucram cu ele
Sa putem sa accesam elemente dintr-o structura de date
Sa intelegem cum sa adaugam sau sa stergem elemente dintr-o structura de date

"""
print("---LISTE---definirea lor se face prin intermediul=>> []")
print()
#liste - sunt structuri de date care pot salva mai multe elemente intr-o locatie
#listele sunt ordonate si sunt mutabile (putem adauga, sterge, modifica elementele din lista)

l1 = []
l2 = []
lista_elemente = ["Ana", "Anton", 2, 45.6, True]
print(type(lista_elemente))
print(lista_elemente)
lista_elemente.pop() #functia pop() sterge din lista by defauld ultimul element
print(lista_elemente)
lista_elemente.pop(0) #stergem din lista cu functia pop() elementul de pe indexul dat
print(lista_elemente)
lista_elemente.remove(2) #stergem din lista cu functia remove() elementul dat
print(lista_elemente)
lista_elemente.append("Radu") #functia append() adauga in lista elementul dat - va fi pus ultimul element in lista
print(lista_elemente)
lista_elemente.insert(1, "Matei")#functia insert() adauga elementul in lista conform indexul dat
lista_elemente.insert(2, 46)
print(lista_elemente)
lungime_lista = len(lista_elemente)
print(f'Lungimea liste este de {lungime_lista} elemente')
lista_elemente.pop(1) #stergem din lista cu functia pop() elementul de pe indexul dat
print(lista_elemente)
print("---" * 15 + "\n")

print("---SETURI---definirea lor se face prin intermediul=>> {} ")
# Seturile - sunt structuri de date care pot salva mai multe elemente in aceeasi locatie
# Seturile nu sunt ordonate,
set_elemente = {"Ana", "Anton", 2, 45.6, True}
print(set_elemente)
set_elemente.add("Matei") #functia add() adauga un element in set, elementul nu este adaugat la sfarsitul
print(set_elemente)
set_elemente.pop()#functia pop() sterge din set un element random
print(set_elemente)
set_elemente.remove(2) #functia remove() sterge din set elementul dat
print("------")
print(set_elemente)
set_elemente_1 = {"Tudor", "Ana", True}
set_elemente_1.update(set_elemente)
print(set_elemente_1)
print(set_elemente)
set_elemente.update(set_elemente_1) #functia update() face update la set cu setul dat
print(set_elemente)
print("---" * 15 + "\n")

print("---TUPLURI---definirea lor se face prin intermediul=>> ()")
#Tupluri - sunt structuri de date care pot salva mai multe elemente in aceeasi locatie
#Tuplurile - sunt ordonate si sunt imutabile (putem accesa elementele, dar nu putem sterge, adauga sau modifica elementele)
tuplu_elemente = ("Ana", "Anton", 2, 45.6, True)
print(tuplu_elemente[1])
tuplu_elemente.index("Ana") #functia index() - va returna indexul la care se află elementul "Ana" în tuplu.
print(tuplu_elemente.index(2)) #ne ve printa indexul elementului 2 din tuplu
print(tuplu_elemente)

print("---" * 15 + "\n")

print("---DICTIONARE---")
#Dictionarele - structuri de date care pot salva mai multe elemente DE TIP CHEIE:VALOARE in aceeasi locatie
#Dictionarele sunt ordonate si imutabile(putem adauga, sterge, modifica elementele din dic)
#accesam elementele dintr-un dictionar prin intermediul cheilor. Cheile unui dictionar trebuie sa fie unice, dar valorile se pot repeta

dictionar_elemente = {
    "nume": "Ana",
    "prenume": "Anton",
    "durata_angajare": 2,
    "varsta": 45.6,
    "inca_angajata": True}

print(dictionar_elemente)
dictionar_elemente.update({"nume": "Maria"})
print(dictionar_elemente)
dictionar_elemente["nume"] = "Andra"
print(dictionar_elemente)

#alte functii
dictionar_elemente.pop("varsta") #functia pop() sterge din dictional perechea cheie:valoare, tinand cont de cheia data
print(dictionar_elemente)
dictionar_elemente.get("nume")
print(dictionar_elemente.get("nume")) #functia get() ne ofera informatia valorii pt cheia data
dictionar_elemente.keys() # functia keys() ne ofera intr-o lista cheile dictionarului pe care apelam functia
print(dictionar_elemente.keys())
dictionar_elemente.values() # functia values() ne ofera intr-o lista valorile dictionarului pe care apelam functia
print(dictionar_elemente.values())

dictionar_valori = {
    "numere_intregi": [1, 2, 3],
    "caractere": ["a", "b", "c"],
    "numere_zecimale": [22.4, 33.5, 34.5]
}
a = dictionar_valori.get("numere_intregi")[0]
print(a)
print(dictionar_valori.get("numere_intregi")[0])
print(dictionar_valori.get("caractere")[1])
print(dictionar_valori.get("numere_zecimale")[2])



# -------------------------------------------------------------------------------------

"""
Se dau doua variabile, x = 10, z = 2.
Efectueaza toate operatiile pe cele 2 variabile,
folosind operatorii aritmetici.
"""

