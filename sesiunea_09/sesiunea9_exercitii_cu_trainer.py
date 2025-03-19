"""
Sesiunea 9 - Exercitii cu Trainer
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
IMPORTANT! Pentru toate exercitiile: apelati functia de cel putin 2 ori
cu valori diferite pentru a testa.
Daca functia are return, printeaza raspunsul.                        
"""

"""
1. Functie care returneaza aria dreptunghiului.
"""

triggered_function()

# latime = int(input("Care este latimea dreptunghiului? \n"))
# lungime = int(input("Care este lungime dreptunghiului? \n"))
#
# def aria_dreptunghiului(latime, lungime):
#     return latime * lungime
#
# print(f"Aria dreptunghiului este {aria_dreptunghiului(latime, lungime)}")



"""
2. Functie care returneaza True daca un caracter x se gaseste intr-un string dat
si False daca nu se gaseste.
"""

triggered_function()



# # implementation 1
# litera = input("Introduceti o litera: ")
# cuvant = input("Introduceti un cuvant: ")
#
# def verificare_caracter(litera, cuvant):
#     if litera in cuvant:
#         return True
#     else:
#         return False
#
# print(verificare_caracter(litera, cuvant))



# # implementation 2
# litera = input("Introduceti o litera: ")
# cuvant = input("Introduceti un cuvant: ")
#
# def verificare_caracter(litera, cuvant):
#     if cuvant.find(litera) == -1:       # returneaza -1 daca nu gaseste caracterul, iar daca gaseste caracterul returneaza indexul
#         return False
#     else:
#         return True
#
# print(verificare_caracter(litera, cuvant))



# # implementation 3
# litera = input("Introduceti o litera: ").lower()
# cuvant = input("Introduceti un cuvant: ").lower()
#
# def verificare_caracter(litera, cuvant):
#     for caracter in cuvant:
#         if caracter == litera:
#             return True
#     else:
#         return False
#
# print(verificare_caracter(litera, cuvant))



"""
3. Functie care nu returneaza nimic. Primeste doua numere si PRINTEAZA:
Primul numar x este mai mare decat al doilea numar y
Al doilea numar y este mai mare decat primul numar x
Numerele sunt egale. 
"""

triggered_function()

# def compara_numere(x, y):
#     if x > y:
#         print(f"Primul numar {x} este mai mare decat al doilea numar {y}")
#     elif y > x:
#         print(f"Al doilea numar {y} este mai mare decat primul numar {x}")
#     else:
#         print(f"Numerele sunt egale.")
#
# compara_numere(1, 2)
# compara_numere(23, 15)
# compara_numere(5, 5)



"""
4. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Printeaza ‘nu am adaugat numarul in set. Acesta există deja’ + returneaza False
"""

triggered_function()

# set_of_numbers = {1, 2, 3, 4, 5}
# print(set_of_numbers)
# print(type(set_of_numbers))
#
# def insert_number_in_set():
#
#     number = int(input("Introduceti numarul: "))
#
#     if number not in set_of_numbers:
#         set_of_numbers.add(int(number))
#         print('Am adaugat numarul nou in set')
#         return True
#     else:
#         print('Nu am adaugat numarul in set. Acesta există deja!')
#         return False
#
# insert_number_in_set()
# print(set_of_numbers)



"""
5. Functie care primeste o luna din an si returneaza cate zile are acea luna.
"""

triggered_function()


# # Map of months to days
# month_days_dict = {
#     "January": 31,
#     "February": 28,     # 29 for leap years
#     "March": 31,
#     "April": 30,
#     "May": 31,
#     "June": 30,
#     "July": 31,
#     "August": 31,
#     "September": 30,
#     "October": 31,
#     "November": 30,
#     "December": 31
# }
# # print(type(month_days_dict))
#
# def days_in_specific_month():
#     print("--- Lunile anului sunt: ---")
#
#     for month in month_days_dict:
#         print(month)
#
#     month_input = str(input("\nIntroduceti luna: ")).capitalize()
#     days = month_days_dict[month_input]
#     return days
#
# print(days_in_specific_month())



"""
6. Functie calculator care sa returneze 4 valori: Suma, diferenta, inmulțirea, impartirea a doua numere.

In final vei putea face:
a, b, c, d = calculator(10, 2)
print("Suma: ", a)
print("Diferenta: ", b)
print("Inmultirea: ", c)
print("Impartirea: ", d)
"""

triggered_function()


# # I.
# def calculator(x, y):
#     # Perform the operations
#     suma = x + y
#     diferenta = x - y
#     inmultirea = x * y
#     impartirea = x / y if y != 0 else "Eroare: Impartire la 0"
#
#     # Return the four results
#     return suma, diferenta, inmultirea, impartirea
#
# # Example usage
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)



# # II.
# def calculator(x, y):
#
#     # 1.
#     # options = ('a', 'b', 'c', 'd')
#     # print("Acesta este un calculator. Aveti urmatoarele optiuni: \na.Suma\nb.Diferenta\nc.Inmultire\nd.Impartire")
#
#     # 2.
#     options = {
#         'a': 'Suma',
#         'b': 'Diferenta',
#         'c': 'Inmultire',
#         'd': 'Impartire'
#     }
#
#     print("Acesta este un calculator. Aveti urmatoarele optiuni: ")
#
#     for key, value in options.items():
#         print(f"{key}   pentru   {value}")
#
#     chosen_options = list(input("Introduceti literele asociate cu operatiile matematice dorite: "))
#
#     # print(chosen_options)
#     # print(*chosen_options)
#
#     results = []
#
#     if 'a' in chosen_options:
#         results.append(f"Suma (x + y): {x + y}")
#     if 'b' in chosen_options:
#         results.append(f"Diferenta (x - y): {x - y}")
#     if 'c' in chosen_options:
#         results.append(f"Inmultire (x * y): {x * y}")
#     if 'd' in chosen_options:
#         if y != 0:
#             results.append(f"Impartirea (x / y): {x / y}")
#         else:
#             results.append("Eroare: Impartirea la 0")
#     if not any(option in chosen_options for option in ['a', 'b', 'c', 'd']):
#         results.append("Optiunile introduse nu sunt valide!")
#
#     return '\n'.join(results)
#
#
# print(calculator(10, 2))



"""
7. Functie care primeste o lista de cifre (adica doar 0-9) 
Exemplu: [1, 3, 1, 5, 9, 7, 7, 5, 5]
Returneaza un DICT care ne spune de cate ori apare fiecare cifra
=> dict {
0: 0
1: 2
2: 0
3: 1
4: 0
5: 3
6: 0
7: 2
8: 0
9: 1
}
"""

triggered_function()

# def count_digits(digit_list):
#
#     # 1.
#     # output_count_dict = {
#     #     0: 0,
#     #     1: 0,
#     #     2: 0,
#     #     3: 0,
#     #     4: 0,
#     #     5: 0,
#     #     6: 0,
#     #     7: 0,
#     #     8: 0,
#     #     9: 0
#     # }
#
#     # 2.
#     # Initialize a dictionary with all digits (0-9) set to 0, no hard-coding
#     digit_count = {i: 0 for i in range(10)}
#     # print(digit_count)
#
#     # 1.
#     # for digit in digit_list:
#     #     if 0 <= digit <= 9:
#     #         digit_count[digit] += 1
#     # else:
#     #     print("OUT!")
#     #
#     # return digit_count
#
#     # 2.
#     for digit in digit_list:
#         if 0 <= digit <= 9:
#             digit_count[digit] += 1
#     else:
#         print("OUT!")
#
#     formatted_dict = "{\n"
#
#     for key, value in digit_count.items():
#         formatted_dict += f"    {key}: {value},\n"
#     formatted_dict = formatted_dict.rstrip(",\n") + "\n}"
#
#     return formatted_dict
#
#
# input_list = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# # count_digits(input_list)
# print(count_digits(input_list))



"""
8. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele.
"""

triggered_function()

# def max_three(x, y, z):
#     return max(x, y, z)
#
# print(max_three(1, 2, 3))
# print(max_three(500, 0, -1))



"""
9. Functie care sa primeasca un numar si sa returneze suma tuturor numerelor de la 0 la acel numar.
Exemplu: dacă dam numarul 3, suma va fi 6 (0+1+2+3)
"""

triggered_function()

# def calculate_sum_from(x):
#
#     list = []
#
#     for number in range(x+1):
#         list.append(number)
#
#     # return print(list)
#     return sum(list)
#
# print(calculate_sum_from(5))



"""
10. Functie care primește 2 liste de numere (numerele pot fi dublate). Returnați numerele comune.

Exemplu:
list1 = [1, 1, 2, 3]
list2 = [2, 2, 3, 4]
Raspuns: {2, 3}
"""

triggered_function()

# def find_common_numbers(list1, list2):
#
#     list_common_numbers = []
#
#     for number in list1:
#         if number in list2:
#             list_common_numbers.append(number)
#
#     return set(list_common_numbers)
#
#
# # list1 = [1, 1, 2, 3]
# # list2 = [2, 2, 3, 4]
# # Raspuns: {2, 3} - OK
#
# list1 = [0, 0, 0, 3, 100, -1, 8000]
# list2 = [7999, 2, 2.9, 0, 5, 300, 0, -1]
#
# print(find_common_numbers(list1, list2))



"""
11. Functie care sa aplice o reducere de pret.
Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90 de lei.
Trateaza cazurile in care reducerea e invalida. De exemplu o reducere de 110% e invalida.
"""

triggered_function()

# # 1.
# def aplica_reducere(pret, reducere):
#     # Verificăm dacă reducerea este validă
#     if reducere < 0 or reducere > 100:
#         return "Reducerea este invalidă! Trebuie să fie între 0% și 100%."
#
#     # Calculăm prețul redus
#     pret_redus = pret * (1 - reducere / 100)
#     return f"Prețul redus este: {pret_redus:.2f} lei"
#
# # Exemplu de utilizare
# pret_initial = 100  # Prețul produsului
# reducere_aplicata = 10  # Reducerea în procente
# rezultat = aplica_reducere(pret_initial, reducere_aplicata)
# print(rezultat)


# 2.
# def aplica_reducere(pret, reducere):
#     try:
#         # Verificăm dacă reducerea este validă
#         if reducere < 0 or reducere > 100:
#             raise ValueError("Reducerea trebuie să fie între 0% și 100%.")
#
#         # Calculăm prețul redus
#         pret_redus = pret * (1 - reducere / 100)
#
#     except ValueError as e:
#         # Afișăm eroarea dacă reducerea este invalidă
#         return f"Eroare: {str(e)}"
#
#     else:
#         # Returnăm prețul redus dacă totul este în regulă
#         return f"Prețul redus este: {pret_redus:.2f} lei"
#
#     finally:
#         # Afișăm un mesaj final, indiferent de rezultatul operației
#         print("Funcția aplica_reducere s-a încheiat.")
#
#
# # Exemplu de utilizare
# pret_initial = 100  # Prețul produsului
# reducere_aplicata = 110  # Reducerea în procente (invalidă)
# print(aplica_reducere(pret_initial, reducere_aplicata))
#
# reducere_valida = 10  # Reducere validă
# print(aplica_reducere(pret_initial, reducere_valida))



"""
12. Funcție care sa afiseze data si ora curenta din Romania.
(bonus: afiseaza si data si ora curenta din China)
"""

triggered_function()

# from datetime import datetime
# import pytz
#
# def afiseaza_data_ora():
#     # Fusul orar pentru Romania
#     romania_tz = pytz.timezone('Europe/Bucharest')
#     romania_time = datetime.now(romania_tz)
#     print("Data si ora curenta in Romania:", romania_time.strftime('%Y-%m-%d %H:%M:%S'))
#
#     # Fusul orar pentru China
#     china_tz = pytz.timezone('Asia/Shanghai')
#     china_time = datetime.now(china_tz)
#     print("Data si ora curenta in China:", china_time.strftime('%Y-%m-%d %H:%M:%S'))
#
# # Exemplu de utilizare
# afiseaza_data_ora()



"""
13. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la Craciun
daca nu vrei sa ne zici cand e ziua ta :)
"""

# triggered_function()

# # Cracium
# from datetime import datetime
# def zile_pana_la_Craciun():
#     astazi = datetime.now()
#     data_Craciun = datetime(astazi.year, 12, 25)
#     if astazi > data_Craciun:
#         data_Craciun = datetime(astazi.year + 1, 12, 25)
#     zile_pana_la_Craciun = data_Craciun - astazi
#     print(f"Mai sunt {zile_pana_la_Craciun} zile pana la Craciun")
#
# zile_pana_la_Craciun()



# # TEMA - implementare pentru ziua noastra de nastere
# from datetime import datetime
# def zile_ramase_pana_la_ziua_mea_de_nastere():
#     astazi = datetime.now()
#     zi_nastere = datetime(astazi.year, 12, 7)
#     if astazi > zi_nastere:
#         zi_nastere = datetime(astazi.year + 1, 12, 7)
#     zile_pana_la_sarbatorire = zi_nastere - astazi
#     print(f"Mai sunt {zile_pana_la_sarbatorire} zile pana la ziua mea de nastere")
#
# zile_ramase_pana_la_ziua_mea_de_nastere()





# implementare formular de contact
# package: __init__.py




# TEMA: formular de inregistrare
# de folosit implementarea self.email = None
# metoda validare: password = confirm password

# DONE
