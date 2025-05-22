import requests
from bs4 import BeautifulSoup

with open(r"D:\Pycharm\PycharmProjects\Cours_python\P3\P3C2\énoncé\index.html", "r") as file:
    soup = BeautifulSoup(file.read(), 'html.parser')
titre = soup.title.string
print(f"Voici le titre de la page : {titre}")

h1_titre = soup.find('h1', id="titre").string
print(f"Voici le h1 avec l'id 'titre' : {h1_titre}")

h2 = soup.find_all("h2")
print(f"voici les noms des produits : {h2}")

products_all = dict()
description = []
products = soup.find_all('li')
for product in products:
    name = product.find('h2').string
    price_str = product.find('p', class_='price').string
    price_list = price_str.split(" ")
    price_list[1] = price_list[1].removesuffix('â‚¬')
    price_list[1] = price_list[1].__add__('€')
    description = product.find_all('p')[-1].string.removeprefix("Description : ")
    products_all[name] = {"Prix" : price_list[1], "Description" : description}

print("Produits :", products_all)

#print(description)
#print(products_all)