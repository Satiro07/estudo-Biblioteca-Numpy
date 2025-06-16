from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os
from unidecode import unidecode

nomes_categorias = ['Roupas/Acessórios',
                    'Eletrônicos/Tecnologia',
                    'Eletrodomésticos',
                    'Informática',
                    'Móveis/Decoração',
                    'Beleza/Higiene',
                    'Alimentos/Bebidas',
                    'Esporte/Lazer',
                    'Livros/Papelaria',
                    'Brinquedos/Jogos',
                    'Ferramentas/Construção',
                    'Pet Shop',
                    'Automotivo',
                    'Outros']

indices_categorias = ['1',
                      '2',
                      '3',
                      '4',
                      '5',
                      '6',
                      '7',
                      '8',
                      '9',
                      '10',
                      '11',
                      '12',
                      '13',
                      '14']

def menu_categorias():
    print()
    for i in range(len(nomes_categorias)):
        print(f'{i+1}. {nomes_categorias[i]}')
    print()

caminho = 'dados_categoria_de_produtos.json'

def carregar_dados(caminho: str):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            return json.load(arquivo)
    return [[],[]]


def salvar_dados(frases: list, caminho: str):
    with open(caminho, 'w', encoding='utf-8') as arquivo:
        json.dump(frases, arquivo, ensure_ascii=False, indent=4)



stopwords_portugues = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com']

def limpar_frase(frase: str):
    frase = frase.lower()
    frase = unidecode(frase)
    frase = re.sub(r'[^a-z\s0-9]', '', frase)
    return frase

frases = carregar_dados(caminho)
def treinar_modelo():
    vertorizar = CountVectorizer(stop_words=stopwords_portugues)

    frases_adicionadas = frases[0]
    categorias_frases = frases[1]

    x = vertorizar.fit_transform(frases_adicionadas)

    modelo = LogisticRegression()
    modelo.fit(x, categorias_frases)

    frase_teste = input('Digite uma frase ou palavra para treinar o modelo: ')
    frase_teste_limpa = limpar_frase(frase_teste)
    x_nova = vertorizar.transform([frase_teste_limpa])

    resultado = modelo.predict(x_nova)

    print('Categoria: ', nomes_categorias[resultado[0]])

    verificacao_acerto = ''
    while verificacao_acerto not in ['s','n']:
        verificacao_acerto = input('Eu acertei? [s/n] ').lower()
        if verificacao_acerto == 's':
            frases[0].append(frase_teste_limpa)
            frases[1].append(int(resultado[0]))
        elif verificacao_acerto == 'n':
            menu_categorias()
            categoria_certa = ''
            while categoria_certa not in indices_categorias:
                categoria_certa = input('Qual seria a categoria correta? ')
                if categoria_certa in indices_categorias:
                    frases[1].append(int(categoria_certa)-1)
                else:
                    print('Por favor digite um número válido!')
            frases[0].append(frase_teste_limpa)
    salvar_dados(frases, caminho)


while True:
    opcao = input('Deseja testar o modelo? [s/n] ').lower()
    if opcao == 's':
        treinar_modelo()
    elif opcao == 'n':
        print('Fim do programa!')
        break
    else:
        print('Por favor, digite "s" ou "n"!')
