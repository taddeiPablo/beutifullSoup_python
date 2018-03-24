#################################################################################
#   NUEVO EJEMPLO CONSUMIENDO LA API DE MERCADO LIBRE Y TRAYENDONOS LOS PRODUCTOS
#   REQUERIDOS POR EL USUARIO
#################################################################################

import urllib
import requests
import json

# clase de tipo producto
class Product(object):
    id = 0
    site_id = ""
    title = ""
    seller = {}
    price = 0
    currency_id = ""
    reservation_price = ""
    reservation_price = None
    reservation_currency_id =  None
    available_quantity =  0
    sold_quantity =  0
    buying_mode =  ""
    listing_type_id =  ""
    stop_time =  ""
    condition =  ""
    permalink = ""
    thumbnail = ""
    accepts_mercadopago = bool
    installments = {}
    address = {}
    shipping = {}
    seller_address = {}
    attributes = []
    original_price = bool
    category_id = "",
    official_store_id = bool
    catalog_product_id =  bool
    reviews = None

## CLASE CREADA PARA UTILIZAR LAS APIS DE MERCADOLIBRE
class MercadoLibre_api(object):
    ## obtenemos los productos apartir del requests
    def get_products(self, search):
        search_encode = urllib.quote_plus(search)
        print(search_encode)
        contents = requests.get('https://api.mercadolibre.com/sites/MLU/search?q='+search_encode)
        data = json.loads(contents.text)
        results = data['results']
        product_list = []
        for x in results:
            producto = Product()
            producto = x
            product_list.append(producto)
        return product_list

class Hayak_api_test(object):
    pass

if __name__=='__main__':
    mercado = MercadoLibre_api()
    print('TESTEO DE API')
    busqueda = raw_input('ingrese la busqueda :')
    print(mercado.get_products(busqueda))
