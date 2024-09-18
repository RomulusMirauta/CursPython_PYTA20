"""
Miniproiect Piloni OOP - Sesiunea 11
"""

"""
MINI PROIECT OOP GESTIONARE PRODUSE SI UTILIZATORI
"""


"""
1. Implementeaza o interfata abstracta cu urmatoarele metode abstracte:
- create -> ia un parametru, numit data
- read -> ia un parametru, numit entry_id
- update -> ia 2 parametri, entry_id si new_data
- delete -> ia 1 parametru, entry_id
"""


"""
2. Implementeaza clasa Product:
- parametri constructor: product_id, name, price, quantity
! quantity va fi un parametru optional care vine din constructor (va avea valoarea default 1)
- atribute pe obiect: product_id, name, price, quantity
"""


"""
3. Implementeaza clasa ProductsRepository:
- va implementa interfata RepositoryInterface
- va avea in constructor un atribut pe obiect, numit products
! Acesta nu va primi valoare din constructor, ci va fi o lista goala.

- implementeaza metodele cerute de interfata implementata:
    - create():
        - primeste ca parametru un dictionar, care contine datele despre un produs
        - creeaza un obiect din clasa Product cu datele venite din dictionar
        ! Asigura-te ca id-ul produsului il generezi tu, avand in vedere urmatoarea pozitie
ce o va ocupa in lista de produse (products)
        - adauga obiectul creat in atributul products.
    - read():
        - primeste ca parametru id-ul produsului pentru care dorim sa obtinem informatii
        - verifica daca produsul se afla in lista de produse:
            - daca da, afiseaza un mesaj in consola cu caracteristicile acestuia
            - daca nu, afiseaza un mesaj in consola "The product with id {id} is not available."
    - update():
        - primeste doi parametri: id-ul produsului pe care dorim sa il actualizam si un dictionar
cu noile date
        - gaseste produsul in lista de produse, dupa id
        - daca produsul a fost gasit, actualizeaza-l
        - trateaza si cazul in care produsul nu a fost gasit.
    - delete():
        - primeste un parametru: id-ul produsului pe care dorim sa il stergem
        - gaseste produsul in lista de produse, dupa id
        - daca produsul a fost gasit, sterge-l
        - trateaza si cazul in care produsul nu a fost gasit.
"""


"""
4. Creeaza o instanta din clasa ProductsRepository si:
- adauga produse
- citeste detalii despre anumite produse
- actualizeaza produse
- sterge produse
"""
