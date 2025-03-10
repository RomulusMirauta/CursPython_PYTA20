"""
EXERCITII WORKSHOP (Sesiunea 8)
"""
import math


# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------

def create_triggered_function():        # definim functia "create_triggered_function"
    call_count = 0                      # defineste variabila locala call_count si o initializeaza cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function" este apelata
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
1.Implementeaza clasa Cerc:
- atribute: rază, culoare
- constructor pentru ambele atribute
- metode:
    - descrie_cerc() - va PRINTA culoarea și raza
    - aria() - va RETURNA aria 
    - diametru() 
    - circumferinta()
"""

triggered_function()

class Cerc:
    raza = None
    culoare = None

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f"Cercul are raza {self.raza} si culoarea {self.culoare}")

    def aria(self):
        calcul_arie = math.pi * (self.raza ** 2)    # self.raza ** 2 = self.raza * self.raza
        return f"Aria cercului este {calcul_arie}"

    def diametru(self):
        calcul_diametru = 2 * self.raza
        return f"Diametrul cercului este {calcul_diametru}"

    def circumferinta(self):
        calcul_circumferinta = 2 * math.pi * self.raza
        return f"Circumferinta cercului este {calcul_circumferinta}"

# TESTING
cerc1 = Cerc(2, "albastru")
cerc2 = Cerc(29, "verde")

# cerc1.descrie_cerc()
# print(cerc1.aria())
# print(cerc1.diametru())
# print(cerc1.circumferinta())

cerc2.descrie_cerc()
print(cerc2.aria())
print(cerc2.diametru())
print(cerc2.circumferinta())



"""
2. Implementeaza clasa Dreptunghi:
- atribute: lungime, lățime, culoare
- constructor pentru toate atributele
- metode:
    - descrie()
    - aria()
    - perimetrul()
    - schimbă_culoarea(noua_culoare):
        - această metodă nu returneaza nimic. 
        - Ea va lua ca parametru o noua culoare si va suprascrie atributul self.culoare.
        - Poti verifica schimbarea culorii prin apelarea metodei descrie().
"""

triggered_function()

class Dreptunghi:
    lungime = None
    latime = None
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie(self):
        return print(f"Dreptunghiul are lungimea {self.lungime}, latimea {self.latime} si culoarea {self.culoare}")

    def aria(self):
        arie_calcul = self.lungime * self.latime
        print(f"Aria dreptunghiului este {arie_calcul}")

    def perimetrul(self):
        perimetru_calcul = 2 * (self.lungime + self.latime)
        print(f"Perimetrul dreptunghiului este {perimetru_calcul}")

    def schimba_culoarea(self, noua_culoare):
        # self.noua_culoare = str(input("Introduceti noua culoare: "))
        self.culoare = noua_culoare


# TESTING
dreptunghi1 = Dreptunghi(4,2, "violet")
dreptunghi2 = Dreptunghi(40, 20, "silver")


# dreptunghi1.descrie()
# dreptunghi1.aria()
# dreptunghi1.perimetrul()
#
# dreptunghi1.schimba_culoarea("alb")
# dreptunghi1.descrie()


dreptunghi2.descrie()
dreptunghi2.aria()
dreptunghi2.perimetrul()

dreptunghi2.schimba_culoarea("negru")
dreptunghi2.descrie()