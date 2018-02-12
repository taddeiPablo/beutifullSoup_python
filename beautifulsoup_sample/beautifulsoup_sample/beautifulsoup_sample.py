
from bs4 import BeautifulSoup
import urllib

# clase categorias, que ofrece mercadolibre
class Categoria(object):
    url = ''
    title = ''

class Mercadolibre_soup(object):
    # metodo por la cual me traigo las categorias ofrecidad por mercadolibre
    def content_categorias():
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

if __name__ == "__main__":
    # aqui creo una instancia de mercadolibre_soup
    # y llamo al metodo content_categorias para traerme las categorias que ofrece mercado libre
    mercado = Mercadolibre_soup()
    mercado.content_categorias()

