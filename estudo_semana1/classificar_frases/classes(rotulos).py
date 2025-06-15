# frases = ['gostei do produto', 'não gostei', 'produto ruim', 'excelente', 'horrível']

# classes = [1, 0, 0, 1, 0] # 1 = positivo, 0 = negativo


# treinar modelo

import re 
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression


frases_limpas = []
def limpar_texto(texto: str): 
    texto = texto.lower()
    texto = re.sub(r'[^a-zA-Z\s]', '', texto) # remove pontuação
    return texto

frases = [    
    "horrível",
    "péssimo",             
    "não gostei",                
    "ruim",                 
    "odiei",                                            
    "nunca mais compro aqui",     
    "feio",
    'bom'   
]

for frase in frases:
    frase_limpa = limpar_texto(frase)
    frases_limpas.append(frase_limpa)

classes = [0,0,0,0,0,0,0,1]
vetorizar = CountVectorizer()
x = vetorizar.fit_transform(frases_limpas)

modelo = LogisticRegression()
modelo.fit(x, classes)

frase_nova = input('frase: ')
frase_nova_limpa = limpar_texto(frase_nova)
x_nova = vetorizar.transform([frase_nova_limpa])

resultado = modelo.predict(x_nova)

print(resultado)
print("Sentimento:", "Positivo" if resultado[0] == 1 else "Negativo")





