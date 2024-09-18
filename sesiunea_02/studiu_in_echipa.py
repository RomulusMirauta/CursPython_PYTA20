"""
EXERCITII WORKSHOP (Sesiunea 2)
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
NOTA: Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
Indirect vei exersa si operatorii in cadrul conditiilor ramurilor din if.

x poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte. 
X este un int.
"""

x = int(input("Introduceti valoarea lui x: "))



"""
1. Explica, cu cuvintele tale, in cadrul unui comentariu,
cum functioneaza un if else.
"""

triggered_function()

"""
if else
instructiune if verifica daca conditia aleasa este adevarata;
conditie adevarata => este executat codul aferent instructiunii if

instructiune else (optionala) verifica daca conditia aleasa este falsa
conditie falsa => este executat codul aferent instructiunii else
"""



"""
2. Verifica si afiseaza daca x este numar natural sau nu.
"""

triggered_function()

# if x > 0:
#     print("x este numar natural")
# else:
#     print("x NU este numar natural")



"""
3. Verifica si afisează daca x este numar pozitiv, negativ sau neutru.
"""

triggered_function()

# if x > 0:
#     print("x este numar pozitiv")
# if x < 0:
#     print("x este numar negativ")
# if x == 0:
#     print("x este numar neutru")



"""
4. Verifica si afisează daca x este intre -2 si 13.
"""

triggered_function()

# if -2 < x < 13:
#     print("x este intre -2 si 13")



"""
5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5.
"""

triggered_function()

# y = 5
#
# if x - y < 5:
#     print("Diferenta dintre x si y este mai mica de 5")



"""
6. Verifica daca x NU este intre 5 si 27  - a se folosi ‘not’.
"""

triggered_function()

# if not(5 < x < 27):
#     print("x NU este intre 5 si 27")



"""
7.
x si y (int)
Verifica si afiseaza daca sunt egale, daca nu, afiseaza care din ele este mai mare.
"""

triggered_function()

y = 5

# if x == y:
#     print("x si y sunt egale")
# else:
#     # cel_mai_mare_numar = {max(x, y)}    # max este folositoare doar pentru a manipula valoarea variabilei
#     print(f"Dintre x si y, {max(x, y)}")


if x == y:
    print("x si y sunt egale")
elif x > y:
    print("x este mai mare")
else:
    print("y este mai mare")
