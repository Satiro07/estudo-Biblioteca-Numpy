# Mostrar vetor com as palavras lado a lado

import re 
from sklearn.feature_extraction.text import CountVectorizer


frases_limpas = []
def limpar_texto(texto: str): 
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto) # remove pontuação
    return texto


for i in range(4):
    frase = input(f'Escreva a {i+1}° frase: ')
    frase = limpar_texto(frase)
    frases_limpas.append(frase)


vetorizar = CountVectorizer()
x = vetorizar.fit_transform(frases_limpas)

palavras  = vetorizar.get_feature_names_out() # mostra as palavras que ele aprendeu
vetores = x.toarray() # cada linha representa uma frase

for i, frase in enumerate(frases_limpas):
    print(f'Frase: {frase}')
    for j, valor in enumerate(vetores[i]):
        print(f'{palavras[j]}: {valor}')
    print()