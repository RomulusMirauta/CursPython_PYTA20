"""
EXERCITII WORKSHOP (Sesiunea 4)
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
1. 
a. Declara o lista, numita note_muzicale, in care sa pui: do re mi etc până la do.
b. Afiseaz-o.
c. Inverseaza ordinea folosind slicing si suprascrie aceasta lista.
d. Printeaza varianta actuala (inversata).
e. Pe lista de la punctul d aplica o metoda care banuiesti ca face acelasi lucru,
adica sa ii inverseze ordinea.
Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat.
f. Printeaza varianta actuala a listei. (Practic ai ajuns inapoi la varianta initiala.)

CONCLUZII:
- slicing e temporar. Daca vrei sa pastrezi noua varianta, va trebui sa suprascrii
lista sau sa o salvezi intr-o lista noua.
- Metoda gasita de tine face suprascrierea automat si permanentizeaza aceste modificări.
Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.
"""

triggered_function()

note_muzicale = ["Do", "Re", "Mi", "Fa", "Sol", "La", "Ti", "Do"]

print(note_muzicale)

note_muzicale = note_muzicale[::-1]

print(note_muzicale)

note_muzicale.reverse()

print(note_muzicale)



"""
2. Folosind lista de la exercitiul 1, afiseaza de cate ori apare ‘do’.
"""

triggered_function()

print(note_muzicale.count('Do'))



"""
3. Transforma lista de la exercitiul 1 intr-o tupla.
Incearca sa adaugi o nota noua.
"""

triggered_function()

note_muzicale = tuple(note_muzicale)
print(note_muzicale)

# nu putem adauga elemente noi intr-o tupla, deoarece este tupla este immutable



"""
4. Declara un dictionar cu notele muzicale de la exercitiul 1.
Cheia va fi nota, iar valoarea un numar care arata de cate ori apare nota in gama. 
Afiseaza-l.
"""

triggered_function()

note_muzicale2 = {
    "Do": 2,
    "Re": 1,
    "Mi": 1,
    "Fa": 1,
    "Sol": 1,
    "La": 1,
    "Ti": 1
}

print(note_muzicale2)

