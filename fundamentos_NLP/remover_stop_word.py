from sklearn.feature_extraction.text import CountVectorizer
import re
from unidecode import unidecode

def limpar(frase):
    frase = frase.lower()
    frase = unidecode(frase)
    frase = re.sub(r'[^a-z\s]', '', frase)
    return frase

stopwords_portugues = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com']


frases = ['eu gosto de estudar',
          'você gosta de programar']

frases = [limpar(frase) for frase in frases]

vetorizar = CountVectorizer(stop_words=stopwords_portugues)
x = vetorizar.fit_transform(frases)


print(vetorizar.get_feature_names_out())
