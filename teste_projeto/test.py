from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os

frases_limpas = [[],[]]
if os.path.exists('dados_projetos2.json'):
    with open('dados_projetos2.json', 'r', encoding='utf-8') as arquivo:
        frases_limpas = json.load(arquivo)

def limpar_frase(frase: str):
    frase = frase.lower()
    frase = re.sub(r'[^a-zA-ZÀ-ÿ\s]', '', frase)
    return frase

while True:
    frase = input('Escreva uma frase ou "s" para sair do programa: ').lower()
    
    if frase == 's':
        break
    frase = limpar_frase(frase)
    frases_limpas[0].append(frase)
    classe_opcao = ''
    while classe_opcao not in ['positiva', 'negativa']:
        classe_opcao = input('A frase é positiva ou negativa? ').lower()
        if classe_opcao == 'positiva':
            frases_limpas[1].append(1)
            break
        elif classe_opcao == 'negativa':
            frases_limpas[1].append(0)
            break
        else:
            print('Por favor digite "positivo" ou "negativo"!')

    vetorizar = CountVectorizer()
    

    with open('dados_projetos2.json', 'w', encoding='utf-8') as arquivo:
        json.dump(frases_limpas, arquivo, ensure_ascii=False, indent=4)

    frases = frases_limpas[0]
    classes = frases_limpas[1]
    x = vetorizar.fit_transform(frases)


    modelo = LogisticRegression()
    modelo.fit(x, classes)

    frase_teste = input('Digite uma frase para testar: ')
    frase_nova_limpa = limpar_frase(frase_teste)
    x_nova = vetorizar.transform([frase_nova_limpa])
    
    resultado = modelo.predict(x_nova)
    print('Sentimento: ', 'Positivo' if resultado[0] == 1 else 'Negativo')

    acerto_erro = input('Eu acertei? [s/n] ').lower()
    if acerto_erro == 's':
        frases_limpas[0].append(frase_nova_limpa)
        frases_limpas[1].append(int(resultado[0]))
    else:
        frases_limpas[0].append(frase_nova_limpa)
        if resultado[0] == 1:
            frases_limpas[1].append(0)
        else:
            frases_limpas[1].append(1)

    with open('dados_projetos2.json', 'w', encoding='utf-8') as arquivo:
        json.dump(frases_limpas, arquivo, ensure_ascii=False, indent=4)
