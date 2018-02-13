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
    url = ''
    title = ''

class Product(object):
    pass

## clase utilizada para hacer scrapy de productos y servicios
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
    def search_producs(self, link):
        contents = urllib.urlopen(link)
        bet = BeautifulSoup(contest, 'lxml')
        all = bet.findAll('div', attrs={'class':'rowItem item item--stack new'})



if __name__ == "__main__":
    # aqui creo una instancia de mercadolibre_soup
    # y llamo al metodo content_categorias para traerme las categorias que ofrece mercado libre
    mercado = Mercadolibre_soup()

    cat = 'Notebooks'
    producto = 'compaq presario'

    categorias = mercado.content_categorias()

    for c in categorias:
        if c.title.find(cat) != -1 :
            final_url = c.url + producto
            #print(final_url)
            mercado.search_producs(final_url)
            break
    #for c in categorias:
        #auxiliar = c.title.split('y')
        #if len(auxiliar) > 1:
            #if auxiliar[0].find(cat) != -1:
                #aux_url = c.url + auxiliar[0] + "-" + producto
                #print(aux_url)
                #break
            #elif auxiliar[1].find(cat) != -1:
                #aux_url = c.url + auxiliar[1] + "/" + producto
                #print(aux_url)
                #break
