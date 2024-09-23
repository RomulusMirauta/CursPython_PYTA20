"""
Exercitii - sesiunea 8
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
EX:
a. Defineste o clasa noua Dog.
b. Obiectele de tip Dog vor avea obligatoriu 2 atribute:
name si age.
c. Creeaza doua obiecte de tip clasa Dog, acceseaza atributele
si afiseaza-le.
d. Schimba atributul nume pentru unul din obiecte
si afiseaza-l din nou.
e. Creaza o metoda description, care returneaza
mesajul '{nume} is {age} years old'.
f. Folosind unul din obiectele instantiate la exercitiul
apeleaza metoda description, salveaza rezultatul
intr-o variabila si afiseaza variabila.
g. Clasa Dog este caracterizata si de atributul rasa.
Adauga acest atribut ca si un atribut al clasei (nu al obiectului)
h. Adauga o noua metoda in clasa Dog, numita speak,
care ia un parametru numit sound.
Metoda trebuie sa returneze mesajul "<name> says <sound>."
i. Apeleaza metoda speak pe unul din obiecte si afiseaza
rezultatul.
"""

# triggered_function()

class Dog:
    rasa = None
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def description(self):
        return f"Cainele {self.name} are {self.age} ani"

    def speak(self, sound):
        return f"{self.name} says {sound}"

dog1 = Dog("Max", 3)
dog2 = Dog(name="Oscar", age=2)

print(dog1.name)
print(dog1.age)
print(f"Cainele {dog2.name} are {dog2.age} ani")

dog2.name = "Johnny"
print(dog2.name)

mesaj = dog1.description()
print(mesaj)

print(dog1.speak("ham"))