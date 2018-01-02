
import pywikibot


site = pywikibot.Site("es", "wikipedia") #Busco elemento en es.wiki
try:
    key = input('Ingrese lo que se quiera buscar en es.wiki')
except:
    print('Escriba algo coherente :-(')

if key == '':
    key = 'Douglas Adams'

page = pywikibot.Page(site, key)
# >>> print(page)
# [[wikipedia:es:Douglas Adams]]
#Esto no tira error si la página no existe (busca links rojos)

try:
    item = pywikibot.ItemPage.fromPage(page)
    # >>> print(item)
    # [[wikidata:Q42]]
except pywikibot.exceptions.NoPage:
    print("El ítem buscado no existe en Wikidata. ¿Por qué no lo creas?")
