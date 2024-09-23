""" HTTP, API - Exemple practice """

import requests


url = "https://dummyjson.com/products"

# GET all products
response = requests.get(url=url)
print(response.status_code)
# print(response.text)
dict_products = response.json()
#                                val1,       val2,      val3,   ....    val30
# dict_products = {"product": [{"id": 1}, {"id": 2}, {"id": 3}, .... {"id": 30}]
#                             index=0, index=1, index=2, ... index=29
#                  "total": val
#                  "skip": val
#                  "limit": val }


for index in range(0, 3):
    print(f'ID PRODUS: {dict_products["products"][index]["id"]}, '
          f'NUME PRODUS: {dict_products["products"][index]["title"]} '
          f'PRET PRODUS: {dict_products["products"][index]["price"]}')

produse_ramase = len(dict_products["products"]) - 3
print(f"Avem {produse_ramase} de produse care nu au fost afisate.")


# GET product by id
id = 20
response_get_product_by_id = requests.get(f"https://dummyjson.com/products/{id}")
produs = response_get_product_by_id.json()
print(f"ID PRODUS: {produs['id']}, NUME: {produs['title']}")
print("---" * 50)

# Metoda HTTP POST - o folosim pentru a trimite date catre server
json_data = {
    "title": "Produs nou"
}

response = requests.post(url="https://dummyjson.com/products/add", json=json_data)
print(response.status_code)
print(response.json())
print("---" * 50)



# Metodele HTTP PUT & PATCH - le folosim pentru a actualiza date
# Metoda PUT - o folosim cand vrem sa facem o actualizare completa

json_data = {
    "title": "Titlu nou",
    "price": 203.23
}

response = requests.put(url="https://dummyjson.com/products/3", json=json_data)
print(response.status_code)
print(response.json())
print("---" * 50)

# Metoda PATCH - o folosim cand vrem sa facem o actualizare partiala

json_data = {
    "title": "Titlu nou nou"
}

response = requests.put(url="https://dummyjson.com/products/3", json=json_data)
print(response.status_code)
print(response.json())
print("---" * 50)


# Metoda HTTP DELETE - o folosim pentru a sterge date
response = requests.delete(url="https://dummyjson.com/products/20")
print(response.status_code)
print(response.json())
print("---" * 50)


# GET all products, skip & limit
param = {
    "limit": 15,
    "skip": 5
}

# url = "https://dummyjson.com/prod"

response = requests.get(url=url, params=param)
if response.status_code == 200:
    produse = response.json()
    print(produse)
else:
    print(f'Eroare: {response.status_code}, {response.text}')
print("---" * 50)


# GET search product
param = {
    "q": "phone",
    "limit": 5
}

url_search = "https://dummyjson.com/products/search"
response = requests.get(url=url_search, params=param)
if response.status_code == 200:
    produse = response.json()
    print(produse)
else:
    print(f'Eroare: {response.status_code}, {response.text}')
