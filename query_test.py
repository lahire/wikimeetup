import pandas
import matplotlib
import matplotlib.pyplot
import requests


matplotlib.style.use('ggplot')
info = '\nData: Wikidata - wikidata.org'
tamaniofuente = 10

QUERY = """
SELECT ?tonalityLabel (COUNT(?tonalityLabel) as ?count) WHERE {
  ?work wdt:P826 ?tonality.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "es" }
}
GROUP BY ?tonalityLabel
ORDER BY DESC(?count)
"""

URL = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql'
DATA = requests.get(URL, params={'query': QUERY, 'format': 'json'}).json()
tonalidades = []
for item in DATA['results']['bindings']:
    tonalidades.append({
     'nombre':item['tonalityLabel']['value'],
	 'cantidad':item['count']['value']
	})
df = pandas.DataFrame(tonalidades)
print(len(df))
print(df)
print(df.dtypes)
##### LO DE ABAJO ESTA TODO ROTO
#titulo="Tonalidades más utilizadas"
#footer="esto es un footer"
#df['nombre'] = df['nombre'].apply(lambda x: x.capitalize())
#s = df.groupby('cantidad').agg('count')['nombre']
#
#ax = s.plot(kind='barh',figsize=(10,8),title=titulo)
#ax.yaxis.set_label_text('')
#ax.xaxis.set_label_text('Tonalidades')
#ax.annotate(footer, xy=(0,-1.16),xycoords='axes fraction', fontsize=tamaniofuente)
#matplotlib.pyplot.savefig('elmegapath', bbox_inches='tight')
#print(DATA)
#input()
