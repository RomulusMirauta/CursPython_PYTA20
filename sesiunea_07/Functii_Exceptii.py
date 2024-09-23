'''
Obiective sesiune: Functii si Exceptii
Sa stim ce sunt functiile si exceptiile
Sa intelegem ce sunt parametrii si care e diferenta intre parametri si argumente
Sa putem sa folosim instructiunea return
Sa folosim functii cu numar indefinit de argumente
'''


#functiile - reprez. bloc de cod reutilizabile care sunt definite cu scopul de a limita numarul de linii de cod pe care le scriem si a face programul sa fie mai modular si respectiv mai usor de citit si de gestionat.
#Utilizarea functiilor se face prin apelarea lor.Apelarea reprezinta scrierea numelui functiei urmata de doua paranteze rotunde.

#Exemplu: sa creem o functie care sa returneze suma a 2 numere
# varianta 1
def suma(a, b): #definim functia cu 2 parametri
    return a + b #functia returneaza rezultatul operatiei de ardunare a celor 2 parametri

suma(2, 4) #apelam functia suma() si dam valori celor 2 parametri - argumente
print(suma(5, 3)) #apelam functia suma() in cadrul functiei print() pentru a afisa rezultatul functiei apelate

r = suma(b=3, a=4) #in variabila r salvam rezultatul functiei apelate, iar valorile pt parametri functiei le dam dand exact numele parametrilor
print(f"Suma nr este {r}") #afisam rezultatul variabilei folosindu-ne de functia print()


# varianta 2
def suma(a, b): #definim functia cu 2 parametri
    rez = a + b #salvam rezultatul operatiei de ardunare a celor 2 parametri intr-o variabila r
    return rez #returneaza valoare informatiei din variabila r


print(suma(2, 3)) #apelam functia suma() in cadrul functiei print() pentru a afisa rezultatul functiei apelate

c = 2

rezultat = c + r
print(rezultat)
def suma(a, b): #definim functia suma() care va avea 2 parametri
    print(f"Suma nr: {a + b}") #functia afiseaza rezultatul operatiei de adunare a celor 2 parametri folosindu-ne de functia print()


def diferenta(c, d): #definim functia diferenta() care va avea 2 parametri
    return c - d #functia retuneaza rezultatul operatiei de scadere a celor 2 param
dif = diferenta(30, 20) #salvam in variabila dif rezultatul apelarii functiei diferenta() care are ca si atribute 30, respectiv 20
print(f"diferenta este {dif}") #afisam un mesaj iar in cadrul string-ului scris in functia print() accesam datele din variabila def

dif = dif - c #aici avem o suprascriere, salvam in variabila dif rezultatul diferentei dintre variabila dif  si variabila c.
print(f"diferenta este {dif}")#afisam un mesaj iar in cadrul string-ului scris in functia print() accesam datele din variabila def


suma(2, 3) #apelam functia suma() care va afisa in consola rezultatul

#parametri - reprez adrese de memorie temporare care se populeaza atunci cand functia este apelata.
#parametri expliciti -> vor primi obligatoriu valoare la apelare
#parametri impliciti -> in cazul in care nu vor primi valoare la apelare se va folosi in mod implicit valoarea specificata la definirea functiei


print("---functii cu nr indefinit de parametri => *args")
#functii cu nr indefinit de parametri, vom folosi => *args(param. simpli)
#args  = prescurtarea de la arguments. Putem da si alt nume, dar de regula asta este folosit ca si conventie

#Exemplu de functie cu *args
def suma_numere(*args): #definim functia suma_numere() care va avea un nr indefinit de parametri deoarece folosim *args
    suma = 0 #initializam varianbila suma caruia ii dam valoarea 0
    for numar in args: #ne folosim de structura repetitiva for care va lua pe rand fiecare valoare a parametrilor
        #print(f"valoarea variabilei suma este {suma}")
        #print(f"valoarea variabilei numar este {numar}")
        suma +=numar #valoare variabilei suma se va modifica in functie de cati parametri vom avea, deoarece ea va efectua ofer
    return suma

print(suma_numere(1, 3))
print(suma_numere(2, 3, 45))
print(suma_numere())
print(suma_numere(10, 5, 11, 19))

print("---functii cu nr indefinit de parametri => **kwargs")
#functii cu nr indefinit de parametri, vom folosi => **kwargs(param cheie: valoare)
#kwargs  = prescurtarea de la keyword arguments. Putem da si alt nume, dar de regula asta este folosit ca si conventie

# Exemplu de functie cu **kwargs

def print_name(**kwargs):
    for key, value in kwargs.items():
        print(f'My {key} is {value}')

print_name(name="Carmen", middle_name="Ioana", last_name="Petre")
print_name(nume="Ion", prenume="Ioana")

def afiseaza_fotbalisti(**kwargs): #definim functia afiseaza_fotbalisti() cu parametri cheie: valoare indefiniti
    for key_echipa, value_echipa in kwargs.items(): #ne vom folosi de structura repetitiva for si de variabilele key_echipa, value_echipa pentru a prelua date din parametrii cheie: valoare definiti in momentul apelarii functiei. Vom itera prin param cu ajutorul functiei items()
        for key_jucator, value_jucator in value_echipa.items(): #ne vom folosi de structura repetitiva for si de variabilele key_jucator, value_jucator pentru a prelua date din value_echipa - care de fapt este un dict. Vom itera prin dict cu ajutorul functiei items()
            print(f"La echipa {key_echipa} joaca jucatorul: {key_jucator} ") #afisam pentru fiecare key_echipa mesajul notat in string, iar in cadrul mesajului accesam datele din variabilele key_echipa si key_jucator
            for key_detalii_jucator, value_detalii_jucator in value_jucator.items(): #ne vom folosi de structura repetitiva for si de variabilele key_detalii_jucator, value_detalii_jucator pentru a prelua date din value_jucator - care de fapt este un dict. Vom itera prin dict cu ajutorul functiei items()
                print("Detalii jucator:", f"{key_detalii_jucator}:{value_detalii_jucator}", end="; ")
                #print(f"Detalii jucator: {key_detalii_jucator}:{value_detalii_jucator}", end="; ") #afisam pentru fiecare key_jucator mesajul notat in string, iar in cadrul mesajului accesam datele din variabilele key_detalii_jucator si value_detalii_jucator
            print('\n---------')

fotbalisti_pe_echipe = {
    "Barcelona": {
        "Dica": {
            "Nume": "Nicole Dica",
            "Numar Tricou": 10
        },
        "Micu": {
            "Nume": "Tudor Micu",
            "Numar Tricou": 9
        },
        "Toader": {
            "Nume": "Tot Toader",
            "Numar Tricou": 1
        }
    },
    "Madrid": {
        "Matei": {
            "Nume": "Matei Tudose",
            "Numar Tricou": 11
        },
        "Vlad": {
            "Nume": "Vlad George",
            "Numar Tricou": 7
        },
        "Ion": {
            "Nume": "Ioan Ion",
            "Numar Tricou": 8
        }
    }
}
afiseaza_fotbalisti(**fotbalisti_pe_echipe) #apelam functia afiseaza_fotbalistii() si vom da dictionarl fotbalisti_pe_echipe ca parametru a-l functiei, iar caracterele ** inseamna despachetarea dictionarului pentru scoaterea elementelor in interiorul lor

afiseaza_fotbalisti(**{"Bucuresti": {"Dica": {"Nume": "Nicole Dica", "Numar Tricou": 10}}})#apelam functia afiseaza_fotbalistii() si vom defini dictionarul direct ca parametru. Ne folosim de ** pentru a despacheta dictionarul astfel putem pentru scoaterea elementelor in interiorul lui
#   dict cu echipele   key_echipa: value_echipa
#        dict cu jucatori           key_jucator: value_jucator
#                     dict cu detalii jucatori    key_detalii_jucator: value_detalii_jucator
#
print("-----exceptii - Tratarea Exceptiilor")
#exceptii - Tratarea Exceptiilor - cand nu ne dorim oprirea codului, putem sa facem ceea ce se numeste tratarea exceptiilor.Ne vom folosi de try , except

# print(10/0) #aici avem o eroare si o putem trata
try:
    print(10/0)
except ZeroDivisionError:
    print("Impartirea la 0 nu este permisa")



print("-----exceptii - Ridicarea Exceptiilor")
# exceptii - Ridicarea Exceptiilor - cand vrem sa fortam o eroare in cod in anumite situatii, ne folosim de conceptul de raise exception.

# nota_student = int(input(" Va rugam sa introduceti nota care trebuie sa fie procesata "))
#
# if nota_student < 5:
#     raise Exception("Nota cursantului este prea mica")
#


try:
    # execute/run this code
    x = 5 / 2
except ZeroDivisionError:
    # execute this block when exception occured
    print("Can not divide by zero!")
else:
    # execute this block if no exception occured
    print("Yeah! Your answer is: ", x)
finally:
    # always execute this block of code
    print("This is always executed!")
