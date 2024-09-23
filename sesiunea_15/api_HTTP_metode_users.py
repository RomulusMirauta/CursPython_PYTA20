""" HTTP, API - Exemple practice """

import requests


url = "https://dummyjson.com/users"

# GET all users
response = requests.get(url=url)
print(response.status_code)
print(response.text)
print("---" * 50)
dict_users = response.json()
#                                val1,       val2,      val3,   ....    val30
# dict_users = {"user": [{"id": 1}, {"id": 2}, {"id": 3}, .... {"id": 30}]
#                             index=0, index=1, index=2, ... index=29
#                  "total": val
#                  "skip": val
#                  "limit": val }


for index in range(0, 3):
    print(f'ID USER: {dict_users["users"][index]["id"]}, '
          f'PRENUME USER: {dict_users["users"][index]["firstName"]} '
          f'VARSTA USER: {dict_users["users"][index]["age"]}')

useri_ramasi = len(dict_users["users"]) - 3
print(f"Avem {useri_ramasi} de useri care nu au fost afisati.")
print("---" * 50)


# GET user by id
id = 20
response_get_user_by_id = requests.get(f"https://dummyjson.com/users/{id}")
utilizator = response_get_user_by_id.json()
print(f"ID USER: {utilizator['id']}, PRENUME: {utilizator['firstName']}")
print("---" * 50)


# Metoda HTTP POST - o folosim pentru a trimite date catre server

# json_data = {
#     "firstName": "Utilizator nou"
# }

json_data = {
        "firstName": "Jean-Claude",
        "lastName": "Van Damme",
        "age": 63,
        "gender": "male",
        "email": "jcvd@gmail.com",
        "password": "x[|Zb2JX-Rcz"
}

response = requests.post(url="https://dummyjson.com/users/add", json=json_data)
print(response.status_code)
print(response.json())
print("---" * 50)


# Metodele HTTP PUT & PATCH - le folosim pentru a actualiza date
# Metoda PUT - o folosim cand vrem sa facem o actualizare completa

# json_data = {
#     "firstName": "Nume nou",
#     "age": 23
# }

json_data = {
        "firstName": "Jean-Claude",
        "lastName": "Van Damme",
        "age": 63,
        "gender": "male",
        "email": "jcvd@gmail.com",
        "password": "x[|Zb2JX-Rcz"
}

response = requests.put(url="https://dummyjson.com/users/3", json=json_data)
print(response.status_code)
print(response.json())
print("---" * 50)

# Metoda PATCH - o folosim cand vrem sa facem o actualizare partiala

json_data = {
    "firstName": "Nume nou nou"
}

response = requests.put(url="https://dummyjson.com/users/3", json=json_data)
print(response.status_code)
print(response.json())
print("---" * 50)


# Metoda HTTP DELETE - o folosim pentru a sterge date
response = requests.delete(url="https://dummyjson.com/users/20")
print(response.status_code)
print(response.json())
print("---" * 50)


# GET all users, skip & limit
param = {
    "limit": 15,
    "skip": 5
}

# url = "https://dummyjson.com/uusseerrss"      # TEST FOR NEGATIVE FLOW/ELSE BRANCH

response = requests.get(url=url, params=param)
if response.status_code == 200:
    useri = response.json()
    print(useri)
else:
    print(f'Eroare: {response.status_code}, {response.text}')
print("---" * 50)


# GET search user
param = {
    "q": "Michael",
    "limit": 5
}

url_search = "https://dummyjson.com/users/search"
# url_search = "https://dummyjson.com/users/searc"      # TEST FOR NEGATIVE FLOW/ELSE BRANCH

response = requests.get(url=url_search, params=param)
if response.status_code == 200:
    useri = response.json()
    print(useri)
else:
    print(f'Eroare: {response.status_code}, {response.text}')
