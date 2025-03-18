from abc import ABC, abstractmethod

"""
EXERCITII WORKSHOP (Sesiunea 10)
"""


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
1. Defineste o clasa abstracta FormaGeometrica:

- Conține un field PI=3.14 (atribut pe clasa)
- Conține o metodă abstractă aria
- Conține o metodă a clasei descrie() 
    - aceasta printează pe ecran ‘Cel mai probabil am colturi’
"""

triggered_function()

class FormaGeometrica(ABC):

    PI = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print('Cel mai probabil am colturi')


"""
2. Defineste o clasa Patrat, care mosteneste FormaGeometrica

- In constructor, defineste atributul latura
    - latura este proprietate privata
    - implementeaza getter, setter, deleter pentru latura
- Implementeaza metoda ceruta de interfața
"""

triggered_function()

class Patrat(FormaGeometrica):

    def __init__(self, __latura):
        self.__latura = __latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
        self.__latura = latura_noua

    @latura.deleter
    def latura(self):
        self.__latura = None

    def aria(self):
        # super().aria()
        self.aria = self.__latura ** 2
        print(f"Aria patratului este: {self.aria}.")


"""
3. Defineste o clasa Cerc, care mosteneste FormaGeometrica

- In constructor, defineste atributul raza
    - raza este proprietate privata
    - implementează getter, setter, deleter pentru rază
- Implementeaza metoda ceruta de interfata - în calcul foloseste field PI
mostenit din clasa parinte
- Defineste metoda descrie() in clasa Cerc - printeaza ‘Eu nu am colturi’
"""

triggered_function()

class Cerc(FormaGeometrica):

    def __init__(self, __raza):
        self.__raza = __raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        self.__raza = raza_noua

    @raza.deleter
    def raza(self):
        self.__raza = None

    def aria(self):
        self.aria = self.PI * (self.__raza ** 2)
        print(f"Aria cercului este: {self.aria}")

    def descrie(self):
        print('Eu nu am colturi')


"""
4. Creeaza un obiect de tip Patrat si joaca-te cu metodele lui
Creeaza un obiect de tip Cerc si joaca-te cu metodele lui
"""

triggered_function()

patrat1 = Patrat(2)
patrat2 = Patrat(5)

# print(patrat1.PI)
# print(patrat2.PI)

# print(patrat1.latura)
# print(patrat2.latura)

# patrat1.aria()
# patrat2.aria()
#
# patrat1.descrie()
# patrat2.descrie()


# print('---'*5**2)
#
# patrat1.latura = 3
# print(patrat1.latura)
# patrat1.aria()
# patrat1.descrie()


# print('---'*5**2)
#
# del patrat1.latura
# print(patrat1.latura)
# patrat1.aria()
# patrat1.descrie()



print('---'*5**2)



cerc1 = Cerc(2)
cerc2 = Cerc(5)

# print(cerc1.raza)
# print(cerc2.raza)

# cerc1.aria()
# cerc2.aria()

# cerc1.descrie()
# cerc2.descrie()


# print('---'*5**2)
#
# cerc1.raza = 3
# print(cerc1.raza)
# cerc1.aria()
# cerc1.descrie()


# print('---'*5**2)
#
# del cerc1.raza
# print(cerc1.raza)
# cerc1.aria()
# cerc1.descrie()
