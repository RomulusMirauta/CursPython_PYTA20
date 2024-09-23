"""
Exercitii sesiunea 10
"""

# overriding method = suprascriere metoda
#
# Yes, "overriding method" in English translates to "suprascriere metodă" in Romanian. This refers to the concept in object-oriented programming where a
# subclass provides a specific implementation of a method that is already defined in its superclass. The method in the subclass overrides the one in the superclass.

















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










"""
EX5: Defineste o clasa abstracta AbstractVideo.
Aceasta va avea o metoda abstracta show_details.
De asemenea, va mai avea o metoda, play, care va afisa mesajul
'Video is playing.'
"""











"""
EX6: Defineste o clasa Videoclip.
Aceasta va implementa clasa abstracta AbstractVideo.
Va avea atribute in constructor: title, duration.
Va implementa metoda show_details, in care va afisa mesajul:
'<title> has a duration of <duration> minutes.'
"""











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


