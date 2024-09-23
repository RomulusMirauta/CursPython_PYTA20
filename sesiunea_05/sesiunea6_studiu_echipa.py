"""
EXERCITII WORKSHOP (Sesiunea 6)
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
1. Avand lista:
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

Foloseste un for ca sa iterezi prin toata lista si sa afisezi 'Masina mea preferata este x':

a. Fa acelasi lucru cu un for each.
b. Fa acelasi lucru cu un while.
"""

triggered_function()

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']


# # FOR
# for i in range(len(masini)):
#     print(f"Masina mea preferata este {masini[i]}")


# # FOR EACH
# for masina in masini:
#     print(f"Masina mea preferata este {masina}")


# WHILE
# i = 0
# while i < len(masini):
#     print(f"Masina mea preferata este {masini[i]}")
#     i += 1



"""
2. Folosind aceeasi lista ca la exercitiul 1:

- foloseste un for else:
    - in for: modifica elementele din lista astfel incat sa fie scrise cu majuscule,
    exceptand primul si ultimul.
    - in else: printeaza lista
"""

triggered_function()

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']


# for i in range(len(masini)):
#     if i != 0 and i != len(masini) - 1:
#         masini[i] = masini[i].upper()
# else:
#     print(masini)




# # implementare cu for each - TEMA !!!!
# # exceptand primul si ultimul


# masini_upper = []
#
# for masina in masini:
#     if masina != 'Audi' and masina != 'Opel':
#         masini_upper.append(masina.upper())
#     else:
#         masini_upper.append(masina)
# else:
#     masini = masini_upper
#     print(masini)




"""
3. Folosind aceeasi lista ca la exercitiul 1:
Vine un cumparator care doreste sa cumpere Mercedes.
Itereaza prin lista cu masini prin modalitatea aleasa de tine.
Daca masina e 'Mercedes':
- printeaza 'Am gasit masina dorita de dvs'
- iesi din ciclu folosind un cuvant cheie care face acest lucru
altfel:
- printeaza 'Am gasit masina X. Mai cautam.'
"""

triggered_function()

# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# for masina in masini:
#     if masina == 'Mercedes':
#         print("Am gasit masina dorita de dvs")
#         break
#     else:
#         print(f"Am gasit masina {masina}. Mai cautam.")



"""
4. Folosind aceeasi lista ca la exercitiul 1:
Vine un cumparator bogat dar indecis.
Ii vom prezenta toate masinile, cu exceptia Trabant si Lastun.
Daca masina e Trabant sau Lastun:
- Foloseste un cuvant cheie sa dea skip la ce urmeaza (nu trebuie else)
- Printeaza "S-ar putea sa va placa masina X".
"""

triggered_function()

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == 'Trabant' or masina == 'Lastun':
        continue    # skip
    print(f"S-ar putea sa va placa masina {masina}")