# Escreva 5 frases com sentimentos mistos (positivas e negativas)

# Limpe os textos

# Aplique CountVectorizer e mostre os vetores com print(X.toarray())

import re 
from sklearn.feature_extraction.text import CountVectorizer


frases_limpas = []
def limpar_texto(texto: str): 
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto) # remove pontuação
    return texto


for i in range(5):
    frase = input(f'Escreva a {i+1}° frase: ')
    frase = limpar_texto(frase)
    frases_limpas.append(frase)


vetorizar = CountVectorizer()
x = vetorizar.fit_transform(frases_limpas)

print(vetorizar.get_feature_names_out()) # mostra as palavras que ele aprendeu
print(x.toarray()) # cada linha representa uma frase