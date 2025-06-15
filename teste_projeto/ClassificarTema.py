from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os
from unidecode import unidecode

stopwords_portugues = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com']
def menu_categorias():
    print('1. Esporte')
    print('2. Tecnologia')
    print('3. Política')
    print('4. Desconhecida')
    
def carregar_dados(caminho: str):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return [[],[]]
caminho = 'dados_ProjetoClassificaTema.json'

frases = carregar_dados(caminho)

def salvar_dados(caminho: str, frases: list):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(frases, arquivo, ensure_ascii=False, indent=4)

def limpar_frase(frase: str):
    frase = frase.lower()
    frase = unidecode(frase)
    frase = re.sub(r'[^a-z\s0-9]', '', frase)
    return frase

def adicionar_categorias():
    frase = input('Escreva uma frase que tenha um contexto de ["Esporte" ou "Tecnologia" ou "Política" ou "Desconhecida"] ou sair: ').lower()
    if frase == 'sair':
        return 'fim'
    frase_limpa = limpar_frase(frase)
    frases[0].append(frase_limpa)
    opcao_categoria = ''
    while opcao_categoria not in ['1', '2', '3', '4']:
        menu_categorias()
        opcao_categoria = input('Digite um número respectivo a frase que você digitou: ')
        if opcao_categoria == '1':
            frases[1].append(0)
        elif opcao_categoria == '2':
            frases[1].append(1)
        elif opcao_categoria == '3':
            frases[1].append(2)
        elif opcao_categoria == '4':
            frases[1].append(3)
        else:
            print('Por favor digite um número válido!')
    salvar_dados(caminho, frases)

def treinar_modelo():
    vetorizar = CountVectorizer(stop_words=stopwords_portugues)
    frases_dados = frases[0]
    classes = frases[1]
    x = vetorizar.fit_transform(frases_dados)

    modelo = LogisticRegression()
    modelo.fit(x, classes)

    frase_teste = input('Digite uma frase para testar: ')
    frase_teste_limpa = limpar_frase(frase_teste)
    x_nova = vetorizar.transform([frase_teste_limpa])

    resultado = modelo.predict(x_nova)

    if resultado[0] == 0:
        categoria = 'Esporte'
    elif resultado[0] == 1:
        categoria = 'Tecnologia'
    elif resultado[0] == 2:
        categoria = 'Politica'
    else:
        categoria = 'Desconhecida'

    print('Categoria: ',categoria)
    verificacao_acerto = ''
    while verificacao_acerto not in ['s', 'n']:
        verificacao_acerto = input('Eu acertei? [s/n] ').lower()
        if verificacao_acerto == 's':
            frases[0].append(frase_teste_limpa)
            frases[1].append(int(resultado[0]))
        elif verificacao_acerto == 'n':
            opcao_categoria = ''
            while opcao_categoria not in ['1', '2', '3', '4']:
                menu_categorias()
                opcao_categoria = input('Qual seria a categoria correta? ')
                if opcao_categoria == '1':
                    frases[1].append(0)
                elif opcao_categoria == '2':
                    frases[1].append(1)
                elif opcao_categoria == '3':
                    frases[1].append(2)
                elif opcao_categoria == '4':
                    frases[1].append(3)
                else:
                    print('Por favor digite um número válido!')
            frases[0].append(frase_teste_limpa)
    salvar_dados(caminho, frases)



while True:
    add_categorias = adicionar_categorias()
    if add_categorias == 'fim':
        treinar = ''
        while treinar not in ['s', 'n']:
            treinar = input('Deseja treinar o modelo? [s/n] ').lower()
            if treinar == 's':
                continuar = ''
                while continuar not in ['n']:
                    treinar_modelo()
                    continuar = input('Deseja treinar mais o modelo? [s/n] ').lower()
                    if continuar == 's':
                        continue
                    elif continuar == 'n':
                        break
                    else:
                        print('Por favor, digite "s" ou "n"!')
                break
            elif treinar == 'n':
                break
            else:
                print('Por favor, digite "s" ou "n"!')
        break
   
