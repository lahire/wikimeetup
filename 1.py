import pywikibot


SITE = pywikibot.Site("es", "wikipedia") #Busco elemento en es.wiki
KEY = input('Ingrese lo que se quiera buscar en es.wiki:\n')
if KEY == '':
    KEY = 'Douglas Adams'

PAGE = pywikibot.Page(SITE, KEY)
# >>> print(page)
# [[wikipedia:es:Douglas Adams]]
#Esto no tira error si la página no existe (busca links rojos)

try:
    ITEM = pywikibot.ItemPage.fromPage(PAGE)
    # >>> print(item)
    # [[wikidata:Q42]]
except pywikibot.exceptions.NoPage:
    print("El ítem buscado no existe en Wikidata. ¿Por qué no lo creas?")

print(ITEM)
print(dir(ITEM))
ITEM_DICT = ITEM.get()
print(ITEM_DICT.keys())
