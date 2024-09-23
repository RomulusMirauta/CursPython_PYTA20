"""
Obiective sesiune:
Sa intelegem ce sunt structurile repetitive
Sa intelegem diferenta intre for si while
Sa intelegem diferenta intre for si foreach

"""


#Structuri repetitive = modalitati prin care putem sa executam o serie de statementuri (instructiuni)
#de mai multe ori pana cand o anumita conditie nu mai este indeplinita


#while - structura repetitiva care instruieste sistemul sa execute un set de instructiuni atata timp cat o conditie este adevarata

# exemplu: Vreau sa ii printez pe cei 7 pitici din Alba ca Zapada pe ecran
i = 1
while i <= 7:
    print(f"Piticul din Alba ca Zapada curent este: {i}")
    i += 1


print()
print("---For---structura repetitiva ")
#For - structura repetitiva care instruieste sistemul sa execute un set de instructiuni atata timp cat un contor se afla intr-un range

#exemplu : Vreau sa ii printez pe cei 7 pitici din Alba ca Zapada pe ecran -> cu start si pas default

for i in range(1, 8):
    print(f"Piticul curent este {i}")

print()
print("---For Each---structura repetitiva ")
#For Each - o modalitate prin care putem sa iteram printr-o structura de date prin parcurgerea elementelor

pitici = ["Bucurosul", "Rusinosul", "Mutulica", "Morocanosul", "Hap-Ciu", "Inteleptul", "Somnorosul"]
for pitic in pitici:
    print(f"Piticul curent este {pitic}.")


print()
print("---diferenta dintre for si for each--- ")
#diferenta dintre For si For Each  => La for variabila de iteratie stocheaza indexul elementelor din lista, in schimb ce la foreach aceasta stocheaza elementul in sine.
# For => util atunci cand vrem sa modificam o valoare in lista = ne va returna indexul elemetului din lista
pitici = ["Bucurosul", "Rusinosul", "Mutulica", "Morocanosul", "Hap-Ciu", "Inteleptul", "Somnorosul"]
#lungime_lista = len(pitici) # salvam lungimea listei in variabila lungime_lista. Voi afla lungimea listei cu ajutorul functiei len()
for i in range(0, len(pitici)):
    print(f"Piticul curent este {pitici[i]}.") #ne va afisa elementul din lista
    print(f"Piticul curent are indexul {i} in lista noastra.") #ne va afisa indexul elementului din lista

# For each => util atunci cand vrem sa scoatem un element din lista
pitici = ["Bucurosul", "Rusinosul", "Mutulica", "Morocanosul", "Hap-Ciu", "Inteleptul", "Somnorosul"]
for pitic in pitici:
    print(f"Piticul curent este {pitic}.") #ne va afisa elementul din lista


print()
print("---diferenta dintre for si while--- ")
#diferenta dintre For si While  => for il folosim cand stim cate iteratii avem, iar while il folosim cand avem un infinit de repetari
masini = ["Dacia", "Audi", "Trabant", "Toyota", "Ford", "BMW", "Opel", "Fiat", "Skoda"]
#For
for i in range(len(masini)):
    print(f"FOR: Masina curenta are indexul {i} (sau este pe pozitia {i}) in lista nostra de masini.") # aici afisam indexul elementului din lista
#For Each
for masina in masini:
    print(f"FOR EACH: Masina curenta este {masina}.") #aici afisam elementul din lista
#WHILE
i = 1
while i <= len(masini): #aici iteram prin lista folosind numerele incepand de la 1 pana la lungimea listei
    print(f"WHILE: Masina curenta este elementul cu nr {i} din lista noastra de masini") #aici printam nr elementului din lista
    i += 1 #variabila i este incrementata cu 1 pana la sfarsitul listei

i = 0
while i < len(masini): # aici iteram prin lista si afisam masina folosind indexul i
    print(f"WHILE: Masina curenta este {masini[i]} si este elementul cu nr. {i+1} .") #aici printam elementul din lista si  nr elementului din lista
    i += 1 #variabila i este incrementata cu 1 pana la sfarsitul listei



print()
#iteram printr-un dictionar folosind metodele keys(), respectiv value()
dic_pitici_s = {
    "piticul 1": "Bucurosul",
    "piticul 2": "Rusinosul",
    "piticul 3": "Mutulica",
    "piticul 4": "Morocanosul",
    "piticul 5": "Hap-Ciu",
    "piticul 6": "Inteleptul",
    "piticul 7": "Somnorosul"
}
for keys in dic_pitici_s.keys():  #acesta versiune va itera prin cheile dic. si va afisa valoarea aferenta fiecarei chei
    print(keys)
    print(dic_pitici_s[keys])

print("---" * 5)

dic_pitici_i = {
    1: "Bucurosul",
    2: "Rusinosul",
    3: "Mutulica",
    4: "Morocanosul",
    5: "Hap-Ciu",
    6: "Inteleptul",
    7: "Somnorosul"
}
for value in dic_pitici_i.values(): #acesta versiune va itera prin valorile dic. si va afisa fiecare valoare
    print(value)

def renge_dict(dic_pitici_i):
    for i in range(len(dic_pitici_i)): #aceasta versiune ne va oferi valori incepand de la 0 pana la elementele din dictionar, i va fi folosit ca un index pt a accesa valorile
        print(dic_pitici_i[i+1]) #adaugam +1 deoarece cheile dintr-un dictionar incep de la 1

renge_dict(dic_pitici_i)

print("done")

print("---controlul iteratiilor--- ")
#break = statement care instruieste sistemul sa sara peste restul de iteratii ramase si sa iasa din bucla repetitiva

date_plata_facturi = [1, 10, 15, 20, 25, 30] #lista cu datele de plata a facturii
data_plata_factura = 10 #variabila in care am salvat data platii facturii
lungime_lista = len(date_plata_facturi)
print(lungime_lista)
for i in range(lungime_lista): #folosim bucla for pt a itera prin fiecare element din lista
    #print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare. Cumpara chibrituri")
    if date_plata_facturi[i] == data_plata_factura: #verificam data curenta daca este egala cu data platii
        print(f"Factura a fost platita in ziua de  {date_plata_facturi[i]}, nu mai mananci la lumanare")
        break #daca condifia este adevarata atunci bucla se va opri datorita acestei instructiuni
    print(f"Data de astazi este: {date_plata_facturi[i]}, in continuare mananci la lumanare. Cumpara chibrituri")

print("---" * 25)
#continue = statement care instruieste sistemul sa sara peste iteratia curenta, nu peste celelalte iteratii

#Exercitiu: vrem sa calculam suma numerelor impare
suma = 0  # initializam variabila suma
for i in range(0, 11): #folosim bucla for pt a itera prin nr de la 0 la 10
    if i % 2 == 0: #verifcam daca nr este impar, adica daca restul(folosim operatorul % - modulo) impartirii la 2 este 0 atunci nr este par
        print(i)
        continue #si trece la urmatoarea iteratie a buclei datorita acestei instructiuni
    print(f"valoare {i} dupa if")
    suma += i #daca i este impar atunci se adauga la suma
print(f"Suma numerelor impare de la 0 la 10 este: {suma}") #aici printam suma nr pt intervalul dat folosind formatarea sirului de caractere




