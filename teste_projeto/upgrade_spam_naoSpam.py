from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os
from unidecode import unidecode

stopwords_portugues = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com']

frases_para_verificar = [
    "Veja como especialistas estão faturando com isso",             # 0 (spam)
    "O relatório final será entregue até sexta-feira",             # 1 (não spam)
    "Este segredo pode mudar sua vida financeira",                 # 0 (spam)
    "Confirme sua presença na reunião com o time",                 # 1 (não spam)
    "Você está deixando dinheiro na mesa sem saber",               # 0 (spam)
    "O arquivo foi compartilhado no seu e-mail corporativo",       # 1 (não spam)
    "Liberado acesso ao curso gratuito por tempo limitado",        # 0 (spam)
    "Segue proposta atualizada com os ajustes solicitados",        # 1 (não spam)
    "Temos uma oportunidade imperdível para você",                 # 0 (spam)
    "Já revisei o código e fiz o commit no repositório"            # 1 (não spam)
]


def limpar_frase(frase: str):
    frase = frase.lower()
    frase = unidecode(frase)
    frase = re.sub(r'[^a-z\s0-9]', '', frase)
    return frase

def carregar_dados(caminho: str):
    if os.path.exists(caminho):
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    return [[],[]]


def salvar_dados(caminho: str, frases: list):
    with open(caminho, 'w', encoding='utf-8') as f:
        json.dump(frases, f, ensure_ascii=False, indent=4)

def testar_modelo():
    vetorizar = CountVectorizer(stop_words=stopwords_portugues)

    spam_nSpam = dados[0]
    detector = dados[1]

    x = vetorizar.fit_transform(spam_nSpam)

    modelo = LogisticRegression()
    modelo.fit(x, detector)

    acertos = 0
    for frase in frases_para_verificar:
        frase_limpa = limpar_frase(frase)
        x_nova = vetorizar.transform([frase_limpa])

        resultado = modelo.predict(x_nova)

        if resultado[0] == 0:
            status = 'Spam'
        else:
            status = 'Não spam'
        print('A frase: ', frase)
        print('Status: ', status)

        acerto_erro = ''
        while acerto_erro not in ['s', 'n']:
            acerto_erro = input('Eu acertei? [s/n] ').lower()
            if acerto_erro == 's':
                acertos += 1
                dados[0].append(frase_limpa)
                dados[1].append(int(resultado[0]))
            elif acerto_erro == 'n':
                dados[0].append(frase_limpa)
                if resultado[0] == 0:
                    dados[1].append(1)
                else:
                    dados[1].append(0)
            else:
                print('Por favor digite "s" ou "n"!')
        print()
    porcentagem = (acertos / len(frases_para_verificar)) * 100
    print(f'A porcentagem de acertos foi de {porcentagem:.2f}%')
    salvar_dados(caminho, dados)

caminho = 'dados_Spam_naoSpam.json'
dados = carregar_dados(caminho)

while True:
    esc = input('Verificar a porcentagem de acertos: [s/n] ').lower()
    if esc == 's':
        testar_modelo()
    elif esc == 'n':
        print('Fim do programa!')
        break
    else:
        print('Por favor digite "s" ou "n"!')