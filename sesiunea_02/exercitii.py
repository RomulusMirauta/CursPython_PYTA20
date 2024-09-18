"""
Rezolvari exercitii sesiunea 2
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
EX1: Se da string-ul prop3 = 'Concertul va avea loc maine."
a. Salveaza intr-o variabila, folosind slicing, primul cuvant.
b. Extrage primele 3 caractere din prop3.
c. Afiseaza prop3 cu caracterele inversate.
"""

triggered_function()

# print("Rezolvare - ex 1")

prop3 = "Concertul va avea loc maine."
# print(prop3)
info = prop3[0:9]
# print(info)
primele_3caractere = prop3[0:3]
# print(primele_3caractere)
# inversare_prop3 = prop3[::-1]
# print(inversare_prop3)
print(prop3[::-1])



"""
EX2: Se da variabila prop1 = 'Andy este prescurtarea de la Andrei"
a. Afiseaza primul caracter.
b. Afiseaza al 4-lea caracter.
c. Afiseaza ultimul caracter.
"""

triggered_function()

prop1 = 'Andy este prescurtarea de la Andrei'
print(prop1[0])
print(prop1[3])
print(prop1[-1])



"""
EX3: Se da string-ul prop2 = 'Masina e rosie.'
Afiseaza lungimea string-ului prop2.
"""

triggered_function()

# print("Rezolvare - ex 3")

prop2 = 'Masina e rosie.'
print("Lungimea stringului prop2 este: ", len(prop2))



"""
EX4: Se da string-ul my_str = 'vacanta'.
a. Foloseste metoda find() pentru a afla primul index la care se gaseste caracterul 'a'.
b. Foloseste metoda count() pentru a afla de cate ori apare caracterul 'a' in my_str.
c. Foloseste metoda capitalize() pentru a scrie cuvantul cu prima litera mare.
d. Foloseste metoda upper() pentru a scrie cuvantul cu litere mari.
"""

triggered_function()

my_str = 'vacanta'

print(my_str.find('a'))
print(my_str.count('a'))
print(my_str.capitalize())
print(my_str.upper())



"""
EX5: Exploreaza urmatoarele metode ajutatoare ale string-ului:
a. endswith()
b. index()
c. lower()
d. replace()
e. strip()
"""

triggered_function()

str1 = '   Un SiMpLu StRiNg   '

print(str1.endswith(' '))
print(str1.endswith('G'))
print(str1.index('S'))
print(str1.lower())
print(str1.replace('S', 's'))
print(str1.replace('   ', '___'))
print(str1.strip())     # strip() sterge spatiile aflate la inceput si la sfarsit



"""
EX6: Se dau doua variabile, a = 10, b = 2.
Efectueaza toate operatiile pe cele 2 variabile, folosind operatorii aritmetici.
"""

triggered_function()

a = 10
b = 2

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)



"""
EX7: Pentru fiecare din exemplele de mai jos, scrie intr-un comentariu rezultatul asteptat, apoi decomenteaza codul de la fiecare exemplu, pe rand 
si ruleaza exemplele si verifica output-ul.
"""

triggered_function()

# Exemplul 1:
a = True
b = False
print(not(a)) # False
print(not(b)) # True

print("---------------------------")

# Exemplul 2:
a = True
b = False
x = not(a)      # => x = False
y = not(b)      # => y = True
print(a or b)   # True
print(x or y)   # True
print(a or x)   # True
print(x or b)   # False

print("---------------------------")

# Exemplul 3:
a = False
b = False
x = not(a)      # x = True
y = not(b)      # y = True
print(a and b)  # False
print(a and x)  # False
print(y and b)  # False
print(x and y)  # True



"""
EX8: Se da variabila num = 12
a. Verifica daca num citit este pozitiv.
b. verifica daca num este mai mare decat 5.
verifica daca num este mai mic decat 25.
c. verifica daca num este intre 0 si 20.
"""

triggered_function()

num = 12

print(num > 0)
print(num > 5)
print(num < 25)
print(0 < num < 20)



"""
EX9: Verifica daca varsta introdusa de utilizator este mai mare decat 18 ani.
"""

triggered_function()

# varsta = int(input('Introdu varsta: '))
# if varsta > 18:
#     print('Varsta introdusa este mai mare decat 18 ani.')



"""
EX10: Verifica daca pretul introdus de utilizator este mai mic sau egal cu 100 de dolari.
"""

triggered_function()

# pret = float(input('Introdu pretul: '))
# if pret <= 100:
#     print('Pretul introdus este mai mic sau egal cu 100 de dolari.')



"""
EX11:
a. Citeste un numar de la tastatura.
b. Verifica daca numarul este par sau impar si afiseaza un mesaj sugestiv in fiecare situatie.
"""

triggered_function()

# nr = int(input('Alege numar: '))
# if (nr % 2) == 0:
#     print('Numarul ales este par.')
# else:
#     print('Numarul ales este impar.')



"""
EX12:
a. Citeste de la tastatura viteza medie cu care conduce utilizatorul.
b. Daca viteza este sub 50 sau egala cu 50, afiseaza mesajul "Viteza normala".
c. Daca viteza este mai mare de 50, afiseaza mesajul "Viteza depasita".
"""

triggered_function()

# viteza_medie = int(input('Alege viteza: '))
# if viteza_medie <= 50:
#     print('Viteza normala')
# else:
#     print('Viteza depasita')



"""
EX13: Citeste de la tastatura varsta utilizatorului si afiseaza categoria de varsta in care se incadreaza.
Tine cont de aceste categorii de varsta:
- intre 0-18 ani: minor
- intre 18-65 ani: adult
- peste 65 ani: senior
"""

triggered_function()

# varsta = int(input('Introdu varsta utilizatorului: '))
# if 0 <= varsta < 18: # daca nu folosim "<=", iar varsta = 0 => senior
#     print('minor')
# elif 18 <= varsta < 65:
#     print('adult')
# else:
#     print('senior')



"""
EX14: Saptamana aceasta, supermarket-ul X ofera clientilor o reducere la intreg cosul de cumparaturi, in functie de totalul cosului de cumparaturi.
Reducerea se aplica in felul urmator:
- Total este intre 100 si 200 lei -> reducere 10%
- Total intre 200 - 300 lei -> reducere 15%
- Total intre 300-400 -> reducere 20 %
- Total mai mare de 400 -> reducere 30 %.
a. Citeste de la tastatura totalul cosului de cumparaturi al utilizatorului.
b. Afiseaza pretul pe care utilizatorul trebuie sa il plateasca pe cumparaturi dupa aplicarea reducerii.
"""

triggered_function()

total = int(input('Introdu totalul cosului de cumparaturi: '))
if 100 < total < 200:
    total -= total * 0.1    # <=> total = total - total * 0.1
    print('reducere 10% => pret final = ', total)
elif 200 <= total < 300:
    total -= total * 0.15
    print('reducere 15% => pret final = ', total)
elif 300 <= total <= 400:
    total -= total * 0.2
    print('reducere 20% => pret final = ', total)
elif total > 400:
    total -= total * 0.3
    print('reducere 30% => pret final = ', total)
else:
    print('FARA REDUCERE => pret final = ', total)
