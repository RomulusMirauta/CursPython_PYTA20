"""
EXERCITII EXERCITII STUDIU IN ECHIPA (Sesiunea 13)
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
1.
a. Creeaza o noua baza de date folosind libraria sqlite3.
b. Creeaza un tabel nou, numit continents, cu urmatoarele coloane:
- continent_id
- continent_name
- continent_code - cod din doua litere
    - foloseste acest link: https://datahub.io/core/continent-codes
"""

# triggered_function()



"""
2. Folosind link-ul de la exercitiul 1, scrie toate query-urile SQL
astfel incat sa adaugi cele 7 continente in tabel.
"""

# triggered_function()



"""
3. Scrie un query SQL pentru a crea un tabel nou, countries, cu urmatoarele
coloane:
- country_code - cod din doua litere (ex: RO, HU, FR etc)
- country_name
- continent_id - foreign key
- population
"""

# triggered_function()



"""
4. Scrie query-uri SQL astfel incat sa adaugi cel putin 10
intrari in tabelul countries.
"""

# triggered_function()



"""
5. Scrie un query SQL care sa citeasca toate tarile din tabelul countries,
ordonate dupa nume.
"""

# triggered_function()



"""
6. Scrie un query SQL care sa numere cate tari sunt in tabelul countries.
"""

# triggered_function()



"""
7. Scrie un query SQL care sa citeasca doar acele tari care au o populatie
mai mare de 20 milioane locuitori.
"""

# triggered_function()



"""
8. Scrie un query SQL care sa citeasca doar acele tari care incep cu
o litera aleasa de tine.
"""

# triggered_function()



# PROIECT SEPARAT
# DONE
