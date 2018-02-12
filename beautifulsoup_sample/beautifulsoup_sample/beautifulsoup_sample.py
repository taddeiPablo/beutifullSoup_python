# EJEMPLO DE COMO UTLIZAR EL WEB SCRAPY CON BEUTIFULSOUP ESTE FUE EL PRIMER EJEMPLO DE COMO HACER SCRAPY CON PYTHON
#
#
# =================================================================================================================
from bs4 import BeautifulSoup
import urllib
import requests
import json

# clase categorias, que ofrece mercadolibre
class Categoria(object):
    id = ''
    name = ''

class Product(object):
    pass

class Mercadolibre_soup(object):
    # metodo por la cual me traigo las categorias ofrecidad por mercadolibre
    def content_categorias(self):
        contents = urllib.urlopen('https://www.mercadolibre.com.ar/categories.html').read()
        bet = BeautifulSoup(contents, 'lxml')
        all = bet.findAll('span',attrs={'class':'ch-g1-3'})
        categorias = []
        for al in all:
            categoria = Categoria()
            categoria.url = al.a['href']
            categoria.title = al.a['title']
            categorias.append(categoria)
        return categorias
    def categories_get(self):
        response = requests.get('https://api.mercadolibre.com/sites/MLA/categories')
        list = response.json()
        categories = []
        for x in list:
            cate = Categoria()
            cate.name = x['name']
            cate.id = x['id']
            categories.append(cate)
        for y in categories:
            print(y.id + y.name)


if __name__ == "__main__":
    # aqui creo una instancia de mercadolibre_soup
    # y llamo al metodo content_categorias para traerme las categorias que ofrece mercado libre
    
    cat = 'Notebooks'
    producto = 'compac presario'

    mercado = Mercadolibre_soup()
    categorias = mercado.content_categorias()
    #mercado.categories_get()
    for c in categorias:
        if c.url.find(cat) != -1 :
            print('contiene')
        auxiliar = c.title.split('y')

        if len(auxiliar) > 1:
            if auxiliar[0].find(cat) != -1:
                aux_url = c.url + auxiliar[0] + "-" + producto
                print(aux_url)
                break
            elif auxiliar[1].find(cat) != -1:
                aux_url = c.url + auxiliar[1] + "/" + producto
                print(aux_url)
                break