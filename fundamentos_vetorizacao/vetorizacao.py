from sklearn.feature_extraction.text import CountVectorizer

frases = ["gostei do produto", "não gostei", "produto ruim"]
vetorizador = CountVectorizer() # aprende as palavraas que existem no conjunto de frases
X = vetorizador.fit_transform(frases) # aprendizado + transformação fit() todas as palavras únicas, transform() tranforma cada frase em um vetor de contagem

print(vetorizador.get_feature_names_out())
print(X.toarray())
