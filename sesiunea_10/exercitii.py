
from abc import ABC, abstractmethod


"""
Exercitii sesiunea 10
"""

# overriding method = suprascriere metoda
#
# Yes, "overriding method" in English translates to "suprascriere metodă" in Romanian. This refers to the concept in object-oriented programming where a
# subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass overrides the one in the superclass.



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
EX1: MOSTENIRE
a. Defineste o clasa numita Persoana.
Aceasta clasa va avea urmatoarele atribute (in constructor):
- nume
- varsta

Implementeaza metoda descrie(), care va afisa mesajul:
'Persoana {nume} are {varsta} ani.'

b. Defineste clasa Angajat, care mosteneste din clasa Persoana.
Aceasta clasa va lua in constructor inca doi parametri,
salariu si post.
Defineste metoda afiseaza_salariu, care returneaza
atributul salariu.

c. Creeaza un obiect de tip clasa Persoana.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metoda descrie.

d. Creeaza un obiect de tip Angajat.
Acceseaza si afiseaza proprietatile acesteia.
Apeleaza/invoca metodele disponibile pe aceasta.

e. Extinde metoda descrie din clasa Angajat,
astfel incat sa se afiseze
si o propozitie care contine atributele salariu si post.
"""

triggered_function()

# class Persoana:
#
#     def __init__(self, nume, varsta):
#         self.nume = nume
#         self.varsta = varsta
#
#     def descrie(self):
#         print(f'Persoana {self.nume} are {self.varsta} ani.')
#
# class Angajat(Persoana):
#     def __init__(self, nume, varsta, salariu, post):
#         super().__init__(nume, varsta)
#         self.salariu = salariu
#         self.post = post
#
#     def afiseaza_salariu(self):
#         return(self.salariu)
#
#     def descrie(self):
#         print(f'Persoana {self.nume} are {self.varsta} ani. Aceasta persoana este angajata si are salariul de {self.salariu} lei, ocupand funtia de {self.post}.')
#
# persoana1 = Persoana('David', 30)
#
# print(persoana1.nume)
# print(persoana1.varsta)
# persoana1.descrie()
#
# angajat1 = Angajat('Ares', 29, 10000, 'Software Tester')
#
# print(angajat1.nume)
# print(angajat1.varsta)
# print(angajat1.salariu)
# print(angajat1.post)
#
# angajat1.descrie()
# print(angajat1.afiseaza_salariu())
#
# print('---'*5**2)
#
# persoana1.descrie()
# angajat1.descrie()



"""
EX2: POLIMORFISM

a. Defineste o clasa Pasare care implementeaza metoda 
zboara.
In metoda zboara, afiseaza mesajul 'Majoritatea pasarilor
pot zbura.'

b. Defineste o clasa Strut, care mosteneste din clasa 
Pasare.
Defineste metoda zboara, si afiseaza mesajul 
'Strutii nu pot zbura."
(Nu extindem metoda din clasa de baza, 
ci o suprascriem -> OVERRIDING)

c. Defineste clasa Rata, care mosteneste din clasa Pasare.
Defineste metoda zboara, si afiseaza mesajul 
"Ratele pot zbura."

d. Instantiaza cele 3 clase si apeleaza metoda zboara
pe fiecare obiect.
POLIMORFISM => aceeasi metoda (acelasi nume) -> 
comportament diferit.
"""

triggered_function()

# class Pasare:
#     def zboara(self):
#         print('Majoritatea pasarilor pot zbura.')
#
# class Strut(Pasare):
#     def zboara(self):
#         print('Strutii nu pot zbura.')
#
# class Rata(Pasare):
#     def zboara(self):
#         print('Ratele pot zbura.')
#
# # Instanțierea unei clase = crearea unui obiect al acelei clase => un obiect = o instanta
# pasare1 = Pasare()
# strut1 = Strut()
# rata1 = Rata()
#
# pasare1.zboara()
# strut1.zboara()
# rata1.zboara()



"""
EX3: ABSTRACTIZARE
a. Defineste interfata Car. Aceasta va avea o metoda
abstracta numita car_model.

b. Defineste clasele Tesla si BMW, care implementeaza
interfata Car.
Metoda car_model trebuie sa afiseze un mesaj legat
de modelul masinii.

Instantiaza clasele Tesla si BMW si invoca metoda 
car_model pe fiecare din acestea.
"""

triggered_function()

# # Car este o interfata, deoarece contine doar o metoda, aceasta fiind abstracta.
# # Daca ar fi continut si o metoda concreta (complet definita si implementata), Car ar fi fost o clasa abstracta.
# class Car:
#     @abstractmethod
#     def car_model(self):
#         pass
#
# class Tesla(Car):
#     def car_model(self):
#         print("Ultimul model de masina dezvoltat de Tesla este: Y.")
#
# class BMW(Car):
#     def car_model(self):
#         print("Ultimul model de masina dezvoltat de BMW este: M8.")
#
# tesla1 = Tesla()
# bmw1 = BMW()
#
# tesla1.car_model()
# bmw1.car_model()



"""
EX4: ENCAPSULARE
a. Defineste o clasa Produs.
Aceasta va avea in constructor urmatoarele atribute:
- nume
- pret
- discount - atribut privat

b. Defineste proprietatea discount:
- getter
- setter -> inainte de a seta o valoare pentru discount,
asigura-te ca acesta e cuprins intre 0-100.
- deleter
"""

triggered_function()

class Produs:
    def __init__(self, nume, pret, discount):
        self.nume = nume
        self.pret = pret
        self.__discount = discount

    @property
    def discount(self):
        # return self.__discount
        # return None
        return " --- @property finished --- "

    @discount.getter
    def discount(self):
        print(f"Getter: Discount-ul este {self.__discount}")
        # return self.__discount
        return " --- getter finished --- "

    @discount.setter
    def discount(self, discount_nou):
        if 0 < discount_nou < 100:
            print(f"Setter: Noul discount este: {discount_nou}")
            self.__discount = discount_nou
        else:
            print(f"Discount-ul {discount_nou} nu este cuprins intre 0 si 100!")
        return " --- setter finished --- "

    @discount.deleter
    def discount(self):
        print("Deleter: Am sters discount-ul")
        self.__discount = None
        return " --- deleter finished --- "


# TESTING EVERYTHING
produs1 = Produs('Cafea', 30, 0)

# print(produs1.nume)
# print(produs1.pret)
# print(produs1.discount) # print on print!


# produs1.discount

# print('---'*5**2)

# produs1.discount = None # error, good
# produs1.discount

# produs1.discount = -1 # error, good
# produs1.discount

# produs1.discount = 0 # error, good
# produs1.discount

# produs1.discount = 1
# produs1.discount


# produs1.discount = 50
# produs1.discount
# print(produs1.discount == 50)

# print(produs1.discount)
# produs1_discount_out = produs1.discount
# print(produs1_discount_out)

# if '50' in produs1_discount_out:
#     print("True")
# else:
#     print("False")

# if produs1_discount_out.find("50") != -1:
#     print("True")
# else:
#     print("False")


# produs1.discount = 99
# print(produs1.discount) # error, good

# produs1.discount = 100
# print(produs1.discount) # error, good

# produs1.discount = 101
# print(produs1.discount) # error, good


# del produs1.discount
# print(produs1.discount)



"""
EX5: Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""

triggered_function()

# class AbstractVideo:
#
#     @abstractmethod
#     def show_details(self):
#         pass
#
#     def play(self):
#         print('Video is playing.')


# abstract_video1 = AbstractVideo()
# abstract_video1.show_details()
# abstract_video1.play()



"""
EX6: Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""

triggered_function()

class AbstractVideo(ABC):
    @abstractmethod
    def show_details(self):
        pass

    def play(self):
        print('Video is playing.')

class Videoclip(AbstractVideo):
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show_details(self):
        # print('<title> has a duration of <duration> minutes.')
        print(f'{self.title} has a duration of {self.duration} minutes.')


# videoclip1 = Videoclip("Python 101", 60)
# videoclip1.show_details()
# videoclip1.play()



"""
EX7:
a. Defineste o clasa numita Movie care va mosteni clasa Videoclip.
Extinde constructorul/metoda de initializare a clasei Movie,
astfel incat sa aiba ca atribute si :
- genre (str)
- director (str) -> ATRIBUT PRIVAT!
- actors (list)

b. Extinde metoda show details, astfel incat sa se afiseze si
mesajul: 
'Is directed by {director} and the actors are {actors}.'

c. Defineste o proprietate director, cu getter, setter si deleter,
care incapsuleaza atributul privat __director.
"""

triggered_function()

class Movie(Videoclip):
    def __init__(self, title, duration, genre: str, __director: str, actors: list):
        # Calls the parent class' constructor
        super().__init__(title, duration)
        # Extends functionality
        self.genre = genre
        self.__director = __director
        self.actors = actors

    def show_details(self):
        super().show_details()
        # print(f"Is directed by {self.__director} and the actors are {self.actors}.")

        # actors is a list, we cannot unpack a list with *
        # Using * directly in an f-string expands the list, but it will format the output as a tuple.
        # print(f"Is directed by {self.__director} and the actors are: {*self.actors,}.")

        # Converts the list of actors into a single string, with each actor separated by a comma and a space.
        print(f"Is directed by {self.__director} and the actors are: {', '.join(self.actors)}.")

    @property
    def director(self):
        print(f"The director is {self.__director}.")
        return self.__director

    # @director.getter
    # def director(self):
    #     print(f"The director is {self.__director}.")

    @director.setter
    def director(self, director_new):
        print(f"The new director is {self.__director}.")
        self.__director = director_new

    @director.deleter
    def director(self):
        print("The director was just deleted!")
        self.__director = None

        # șterge complet atributul folosind del => eroare la apelarea: movie1.show_details()
        # del self.__director


#TESTING EVERYTHING
movie1 = Movie("The Avengers", 120, "Action", "Joss Whedon", ["Chris Evans", "Robert Downey Jr.", "Scarlett Johansson", "Chris Hemsworth", "Mark Ruffalo", "Jeremy Renner", "Tom Hiddleston", "Samuel L. Jackson", "Hayley Atwell", "Gwyneth Paltrow", "Cobie Smulders", "Clark Gregg"])

print(movie1.title)
print(movie1.duration)
print(movie1.genre)
movie1.director

# movie1.director = "Joss"
# movie1.director

# print('---'*5**2)
# movie1.show_details()

# del movie1.director
# movie1.director

# print('---'*5**2)
# movie1.show_details()


# print(movie1.actors)

# afisare actori in folosind for each
# print("\n-----   The actors are:   -----")
# for actor in movie1.actors:
#     print(actor)
#
# print("\n-----   The End of 'The actors'  -----")


print('---'*5**2)
movie1.show_details()
