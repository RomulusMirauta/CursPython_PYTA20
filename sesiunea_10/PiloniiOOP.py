'''
Obiective sesiune: Pilonii OOP
Sa intelegem pilonii OOP (Mostenire,  Encapsulare, Abstractizare, Polimorfism)
Sa practicati crearea de clase si obiecte in contextul celor patru piloni ai programarii
'''



print("----Mostenire----")
# Mostenire - reprezinta posibilitatea unei clase de a mosteni atribute si metode definite intr-o clasa parinte.
# Mostenirea se implementeaza prin specificarea numelui clasei parinte intre paranteze langa numele clasei mostenitoare.
# O clasa copil poate sa mosteneasca un numar nelimitat de clase parinte.
class Animal:
    def __init__(self, nume, specie):
        self.nume = nume
        self.specie = specie

    def sunet_animal(self):
        pass

    def info(self):
        return f"{self.nume} este un animal din specia {self.specie} "

class Pisica(Animal):
    def __init__(self, nume, rasa):
        # Apelăm constructorul clasei părinte folosind funcția super()
        # self.nume = nume
        # self.specie = "pisica"
        super().__init__(nume, specie="pisica")
        self.rasa = rasa

    def sunet_animal(self):
        return "Miau, miau!"

    def info(self):
        return f"{self.nume} este o {self.specie} {self.rasa}."

    def igienizare_pisica(self):
        return f"{self.specie} se spala singura"

class Caine(Animal):
    def __init__(self, nume, rasa):
        # Apelăm constructorul clasei părinte folosind funcția super()
        # self.nume = nume
        # self.specie = "caine"
        super().__init__(nume, specie="caine")
        self.rasa = rasa

    def sunet_animal(self):
        return "Ham, Ham!"

    def info(self):
        return f"{self.nume} este un {self.specie} {self.rasa}."

# Cream un obiect folosindu-ne de clasa Pisica() si apelam metodele definite in clasa parinte Animal() si clasa copil Pisica()
my_cat_1 = Pisica(nume="Bubu", rasa="Siamese")
my_cat_2 = Pisica(nume="Ani", rasa="British")
print(my_cat_1.info())
print(my_cat_2.info())
print(my_cat_2.igienizare_pisica())
print(my_cat_1.sunet_animal())
print()

my_dog = Caine(nume="Puf", rasa="Dalmatian")
print(my_dog.info())

print("----Abstractizare----")

# abstractizare - reprezinta crearea a ceea ce putem sa  numim un tipar pentru celelalte clase, astfel incat oricare clasa va veni si va mosteni clasa abstracta va fi obligata sa implementeze (adica sa dea un comportament) metodelor abstracte definite in acea clasa.
# Clasa este marcata ca fiind abstracta folosind utilitarul ABC (Abstract Base Class)
# Metoda dintr-o clasa abstracta este marcata ca fiind abstracta prin intermediul decoratorului @abstractmethod
from abc import ABC, abstractmethod


class Gradinita(ABC):

    @abstractmethod
    def joaca(self):
        raise NotImplementedError  # am instruit sistemul sa returneze o eroare specifica daca metoda nu este implementata

    def somn(self):
        pass

    @abstractmethod
    def activitati(self):
        pass


class Gradinita_privata(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("copiii alearga")

    def activitati(self):
        print("Copiii coloreaza")


class Gradinita_publica(Gradinita):
    nr_copii = 0
    adresa = None
    orar = None

    def joaca(self):
        print("copiii sar coarda")

    def activitati(self):
        print("Copiii canta")

gradinita_pub = Gradinita_publica()
gradinita_pub.joaca()

gradinita_priv = Gradinita_privata()
gradinita_priv.joaca()

print('----Polimorfism----' )
# Polimorfism - reprezinta posibilitatea crearii a doua functii cu nume identic dar cu comportament diferit
class America:
    limba = "Engleza"
    drapel = "American"
    imn = "Imnul americii"

    def printeaza_limba(self):
        print(f"Limba care se vorbeste in America este {self.limba}")


class Romania:
    limba = "Romana"
    drapel = "tricolor"
    imn = "desteapta-te romane"

    def printeaza_limba(self):
        print(f"Limba care se vorbeste in Romania este {self.limba}")


obiect_america = America()
obiect_romania = Romania()

obiect_romania.printeaza_limba()
obiect_america.printeaza_limba()

print('------ Encapsulare ------' )

# Encapsulare - este o modalitate prin care putem sa ascundem anumite atribute sau metode utilizatorului
# Motivul pentru care vrem sa facem asta este fie din motive de securitate fie pentru a controla

class Casa_encapsulare:
    # decorator = elemente care modifica comportamentul unei functii
    _numar_etaje = None #atribut protected
    numar_camere = None  #atribut public
    numar_bai = None  #atribut public
    __material_constructie = None  #atribut private
    suprafata = None  #atribut public
    an_constructie = None  #atribut public
    adresa = None  #atribut public
    clasa_energetica = None  #atribut public
    pret = None  #atribut public

    def __init__(self, numar_etaje, numar_camere, numar_bai, material_constructie, suprafata, adresa):
        self._numar_etaje = numar_etaje
        self.numar_camere = numar_camere
        if numar_bai > 2:
            print("Nu putem construi mai mult de doua bai")
        else:
            self.numar_bai = numar_bai
        self.__material_constructie = material_constructie
        self.suprafata = suprafata
        self.adresa = adresa

    def calculeaza_aprobare_numar_etaje(self):  # metoda public
        if self._numar_etaje > 5:
            print(
                "Apartamentul are mai mult de 5 etaje, drept urmare se poate acorda aprobarea necesara")
        else:
            self.aprobare = True

    def __actualizeaza_an_constructie(self, an_constructie):  # metoda private
        self.an_constructie = an_constructie
        return self.an_constructie

    def vinde_casa(self):  # metoda public
        print(f"Apartament de vanazare in zona lalelelor"
              f"Numar camere: {self.numar_camere}"
              f"Numar etaje: {self._numar_etaje}"
              f"Numar bai: {self.numar_bai}"
              f"An constructie: {self.an_constructie},"
              f"Suprafata: {self.suprafata}"
              f"Material constructie: {self.__material_constructie}")

    def update_materiale_constructie(self, material):
        self.__material_constructie = material

    @property
    def materiale_constructie(self):
        pass

    @materiale_constructie.getter  # cu ajutorul getter-elor avem acces la valorile atributelor
    def materiale_constructie(self):
        return self.__material_constructie

    @materiale_constructie.setter  # cu ajutorul setter-elor setam valori atributelor
    def materiale_constructie(self, material_constructie):
        self.__material_constructie = material_constructie
    #
    # @materiale_constructie.deleter  # cu ajutorul deteler stergem valorile atributelor
    # def materiale_constructie(self):
    #     self.__material_constructie = None


garsoniera = Casa_encapsulare(0, 1, 1, "beton", 40,"Strada Lalelelor 23")  # cream obiectul gasonier cu ajurorul clasei Casa_encapsulare()

print(f"materiale de constructie returnate prin getter inainte de update: {garsoniera.materiale_constructie}")  # apelare getter
print(f'afiseaza nr camere {garsoniera.numar_camere}')
garsoniera.numar_camere = 3
print(f'afiseaza nr camere {garsoniera.numar_camere}')
garsoniera.materiale_constructie = 'caramida'
print(garsoniera.Casa_encapsulare__material_constructie)

print(f"materiale de constructie returnate prin getter inainte de update: {garsoniera.materiale_constructie}")
# garsoniera.materiale_constructie = "caramida"  # setter
# print(f"materiale de constructie returnate prin getter dupa update: {garsoniera.materiale_constructie}")  # apelare getter
# garsoniera.update_materiale_constructie("beton si caramida")
# print(f"materiale de constructie returnate prin getter dupa update: {garsoniera.materiale_constructie}")  # apelare getter
# del garsoniera.materiale_constructie
# print(f"materiale de constructie returnate prin getter dupa delete: {garsoniera.materiale_constructie}")  #apelare getter
