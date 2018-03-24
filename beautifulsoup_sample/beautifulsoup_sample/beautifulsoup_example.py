########################################################
#  NUEVO EJEMPLO DE COMO ARMAR UN SCRAPY CON BEAUTIFUL
########################################################



from bs4 import BeautifulSoup
import urllib
import requests
import json

class items(object):
    url_redirec = ""
    img = ""
    price = ""
    free_interest_text= ""
    model = ""
    location = ""

#clase que maneja los items de mercadolibre
class MercadoLibre(object):
    def __init__(self):
        self.contents = ""
        self.beauti = None
        self.items = None
        self.paginas = None
        self.agent = None
    def result_search(self, search):
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'https://listado.mercadolibre.com.ar/' + urllib.quote_plus(search)
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beauti = BeautifulSoup(self.contents, 'lxml')
        self.items = self.beauti.findAll('ol', attrs={'id': 'searchResults'})
        self.scrape_page_items(self.items)
        self.paginas = self.beauti.findAll('li',attrs={'class':'pagination__page'})
    def scrape_page_items(self, ite):
        # proceso de scrapy para mercadolibre y sus items
        for its in ite[0].find_all('li'):
            aux = its.find_all("div", class_="carousel")
            if len(aux) != 0:
                print("========================================================")
                #print(aux[0].ul.li.a.img)
                aux1 = its.find_all("span", class_="price__symbol") #simbolo moneda
                aux2 = its.find_all("", class_="price__fraction") #precio
                print(aux1[0].text)
                print(aux2[0].text)
                aux3 = its.find_all("span", class_="price-old") #precio antiguo
                print(aux3)
                aux4 = its.find_all("div", class_="item__discount") # % descuento
                print(aux4)
                aux5 = its.find_all("h2", class_="item__title list-view-item-title") #title
                print(aux5[0].text)
                aux6 = its.find_all("div", class_="item__reviews-total") #reviews totales
                print(aux6)
                aux7 = its.find_all("div", class_="item__condition") #condicion y ubicacion
                print(aux7[0].text)
                print("=========================================================")
    def next_to_pages(self, paginas):
        pass
#End class
#clase que maneja los items proporcionados por Olx
class Olx(object):
    def __init__(self):
        self.contents = None
        self.beuti = None
        self.items = None
        self.paginas = None
        self.agent = None
    def result_search(self, search):
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'https://www.olx.com.ar/search/' + urllib.quote_plus(search)
        print(self.url)
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beuti = BeautifulSoup(self.contents, 'lxml')
        self.paginas = self.beuti.findAll('li', attrs={'class', 'items-pagination'})
        self.items = self.beuti.findAll('ul', attrs={'class', 'items-list'})
        self.scrape_page_items(self.items)
    def scrape_page_items(self, ite):
        for its in ite[0].find_all('li'):
            print("=================================================")
            aux = its.find_all("figure", class_="items-image")
            if len(aux) != 0:
                print(aux[0].img)
            aux1 = its.find_all("div", class_="items-info")
            if len(aux1) != 0:
                print(aux1[0])
            aux2 = its.find_all("p", class_="items-price")
            if len(aux2) != 0:
                print(aux2[0])
            aux3 = its.find_all("p", class_="items-date")
            if len(aux3) != 0:
                print(aux3[0])
            aux4 = its.find_all("p", class_="featuredad")
            if len(aux4) != 0:
                print(aux4[0])
            print("=================================================")
            print("\n")
    def next_to_pages(self, paginas):
        pass
#End class
#clase que maneja los items proporcionados por Amazon
class Amazon(object):
    def __init__(self):
        self.contents = None
        self.beuti = None
        self.items = None
        self.paginas = None
        self.agent = None
    def result_search(self, search):
        self.agent = {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        #https://www.amazon.es/s/ref=sr_pg_1?rh=i%3Aaps%2Ck%3Anotebooks&page=1&keywords=notebooks
        #https://www.amazon.es/s/field-keywords=
        self.url = 'https://www.amazon.es/s/ref=srpg_1?rh=i%3Aaps%2Ck%3Anotebooks&page=1&keywords=' + urllib.quote_plus(search)
        print(self.url)
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beuti = BeautifulSoup(self.contents, 'lxml')
        #print(self.beuti)
        #self.paginas = self.beuti.findAll('span', attrs={'class', 'pagnLink'})
        self.items = self.beuti.findAll('ul', attrs={'class', 's-result-list'})
        #print(self.beuti.ul)
        self.scrape_page_items(self.items)
    def scrape_page_items(self, ite):
        print(ite)
        for its in ite[0].find_all('li'):
            print(its)
            print("\n")

class Ebay(object):
    def __init__(self):
        self.contents = None
        self.beuti = None
        self.items = None
        self.paginas = None
        self.agent = None
    def result_search(self, search):
        self.agent= {"User-Agent":'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw='+urllib.quote_plus(search)+'&_sacat=0'
        self.contents = requests.get(self.url, headers=self.agent).text#urllib.urlopen(self.url).read()
        self.beuti = BeautifulSoup(self.contents, 'lxml')
        self.items = self.beuti.findAll('div', attrs={'class', 'clearfix'})
        self.scrape_page_items(self.items)
    def scrape_page_items(self, ite):
        for its in ite[0].find_all('ul'):
            print(its)






if __name__== "__main__":
    Ml = MercadoLibre()
    Ol = Olx()
    am = Amazon()
    eb = Ebay()
    print("bienvenido a esta prueba")
    busqueda = raw_input('ingrese la busqueda :')
    #Ml.result_search(busqueda)
    #Ol.result_search(busqueda)
    #am.result_search(busqueda)
    eb.result_search(busqueda)
