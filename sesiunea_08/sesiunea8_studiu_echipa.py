"""
EXERCITII WORKSHOP (Sesiunea 8)
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

