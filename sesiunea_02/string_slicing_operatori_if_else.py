"""

String Slicing, metode string, Operatori, conditionale

OBIECTIVE

String slicing - sa intelegem ce este și cum se face
String Methods - sa stim sa lucram cu ele
Tipuri de Operatori Sa cunoastem tipurile principale de operatori
De atribuire
Artimetici
De comparare
Logici
Conditionalul if else (flow control) Sa intelegem cum functioneaza if statement
If simplu
If/else
If/elif/else

"""


# String slicing
info = 'Afara sunt 2 grade'
##      012345

print(info[0:3:1])                                              # [0:3] = Afa
print(info[0:5])
print(info[:5])

oras = "Tulcea, Cluj-Napoca, Constanta, Bucuresti, Iasi"

print(oras[::-1])                                               # reversing the string
print(oras[::2])
print(oras[2])
print(oras[12])
print(oras[-1])                                                 # afisarea ultimului caracter din string

# string slicing syntax = start, stop, step
# step = pasul


# String methods
# len() - aflam lungimea unui string/structuri de date
lungime_oras = len(oras)
print("lungime variabila oras:", lungime_oras)
print(f"In cadrul variabilei oras avem {len(oras)} de caractere")


legume = "cartof, Ceapa, Morcov, rosie, mazare"
print(legume.replace("a", "A", 2))
print(legume.upper())
print(legume.lower())
print(legume.split(","))    # transforma in lista
print(legume.split("a"))
print(legume.index("M"))    # indexul elementului "M"
print(legume.capitalize())
print(legume.count("a"))


# Operatori
# Operatori aritmetici

numar1 = 40
numar2 = 3
print(numar1 + numar2)
print(numar1 - numar2)
print(numar1 * numar2)
print(numar1 / numar2)
print(numar1 % numar2)       # % = modulo => restul impartirii
print(numar1 ** numar2)
print(numar1 // numar2)      # // = floor division => taie zecimalele

litera_b = "b"
print(litera_b * 2)          # inmultire strings
print(litera_b + litera_b)   # concatenare strings
print("---" * 15)

x = 17
y = 2

# daca ambele numere sunt int -> rezultatul va fi int
print (x // y) # 8.5 -> rezultatul este 8

x = 17.8
y = 2

# daca cel putin unul din numere este float -> rezultatul va fi float
print(x // y) # 8.9 -> rezultatul este 8.0

print("---" * 15)


# Operatori de atribuire

z = 5
print(z)
z += 3      # z = z + 3
print(z)


# Operatori logici + de comparare

orar = True
program_dimineata_max = 11
program_seara_max = 18

print(orar == True)     # conditie simpla
print(orar == False and program_seara_max < 20)
print(orar == False or program_seara_max < 20)
print(not(orar == True))
print(not orar)         # returneaza opusul


# Conditionalul if else

# x = 5
# if x == 5:
#     print("x este egal cu 5") # indentare cod

# NOTA_DE_TRECERE = 4.5
# nota = float(input('Alege nota'))
# if nota >= NOTA_DE_TRECERE:
#     print(f'Ai luat nota {nota}')
#     print('Felicitari ai trecut examenul')
# else:
#     print(f'Ai luat doar nota {nota}')
#     print('Ne vedem la vara! Ai picat examenul 🥹')


# robotelul telefonic
optiune = int(input('alege o optiune'))
if optiune == 0:
    print('meniul anterior')
elif optiune == 1:
    print('ati ales ro')
elif optiune == 2:
    print('ati ales eng')
else:
    print('Nu am identificat optiunea, mai incearca.')



# de lucrat individual - ex: 12, 14
