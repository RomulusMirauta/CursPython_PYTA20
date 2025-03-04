# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------

def create_triggered_function():        # definim functia "create_triggered_function()"
    call_count = 0                      # definim variabila locala call_count si o initializam cu valoarea 0

    def triggered_function():           # definim o "nested function" (o functie in interiorul altei functii)
        nonlocal call_count
        call_count += 1                 # <=> call_count = call_count + 1; incrementam "call_count" cu 1 de fiecare data cand functia "triggered_function()" este apelata
        print("-" * 150 + "\n" * 2)
        print(f"Output pentru exercitiul cu numarul [ {call_count} ]")
                                        # ⬆️ printeaza text + valoare stocata in variabila "call_count" - loop iteration, printeaza o data per apelare functie
        print()
    return triggered_function           # acest return este folosit pentru functia "create_triggered_function()"

# creeam o instanta a functiei "triggered_function()", definita in cadrul functiei "create_triggered_function()"
# returneaza o instanta a functiei "triggered_function()", care poate fi apoi apelata ori de cate ori este nevoie pentru a efectua actiunea definita in cadrul acesteia
triggered_function = create_triggered_function()

# Cum dam "trigger" la numaratoare:
# triggered_function()                  # apelarea functiei

# ------------------------------------------------------------------------------     Numaratoare automata     ------------------------------------------------------------------------------


'''
Utilizare: 
1. copiem codul scris intre liniile lungi comentate, care contin "Numaratoare automata" - la inceputul fisierului in care vom rezolva exercitiile, inainte de primul enunt
2. dupa fiecare enunt (exercitiu), trebuie adaugat un "triggered_function()" pentru a incepe/continua numaratoarea
'''