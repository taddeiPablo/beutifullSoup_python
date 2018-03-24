# ejemplo armado con selenium y python para realizar scrapy

from selenium import webdriver
import urllib

#  NUEVO METODO DE REALIAR SCRAPY UTLIZANDO SELENIUM FALTA PROBAR CON OTRAS PAGINAS WEBS 
# Y ADEMAS CONTENIDO DINAMICO Y OBTENER TODA LA INFORMACION REQUERIDA
class Scrapy_Selenium(object):
    def __init__(self):
        pass
    def search_data(self, key, search):
        driver = webdriver.Chrome("C:\drivers\chromedriver.exe")
        
        if key == "ml":
            url = "https://listado.mercadolibre.com.ar/" + urllib.quote_plus(search)
            
            driver.get(url)
            index = 0
            # aqui obtengo todos los items a comprar
            for x in driver.find_elements_by_xpath('//ol/li/div[@id]'):
                # aqui obtengo la imagen del item
                aux = driver.find_elements_by_xpath("//*[@id='"+ x.get_attribute('id') +"']/div/div/div/ul/li/a/img")
                # id del articulo
                print(x.get_attribute('id'))
                print(x.text.split('\n')) #aqui corto el string en partes para poder utilizarlo en diferentes atributos despues.
                # aqui recorro las imagenes y solo traigo una
                if len(aux) != 0 :
                    for x1 in aux:
                        print(x1.get_attribute('src'))
                        break

                print("*****************************************")
                index = index + 1
                print(index)
        elif key == "am":
            url = "https://www.amazon.es/s/ref=srpg_1?rh=i%3Aaps%2Ck%3Anotebooks&page=1&keywords=" + urllib.quote_plus(search)
            
            driver.get(url)
            index = 0
            for x in driver.find_elements_by_xpath('//*[@id="s-results-list-atf"]/li[@id]'):
                print(x.get_attribute('id'))
                aux = driver.find_elements_by_xpath("//*[@id='" + x.get_attribute('id') +"']/div/div/div/div[1]/div/div/a/img")
                if len(aux) != 0:
                    for x1 in aux:
                        print(x1.get_attribute('src'))
                        break
                print(x.text)


                
                print("**************************************************")
                index = index + 1
                print(index)
        
        driver.close()



if __name__ == '__main__':
    print("bienvenidos a esta prueba")
    SSC = Scrapy_Selenium()
    opcion = raw_input('ingrese donde quiere buscar :')
    busqueda = raw_input('ingrese su busqueda :')
    SSC.search_data(opcion, busqueda)

