from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os
from unidecode import unidecode
from time import sleep

stopwords_portugues = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com']

frases_para_verificar = [
    "Clique aqui e ganhe um iPhone grátis!",
    "Reunião amanhã às 14h com a equipe de projetos.",
    "Você foi selecionado para um prêmio exclusivo.",
    "Compre agora e leve o segundo de graça!",
    "Relatório financeiro já está disponível no sistema.",
    "Última chance! Descontos de até 90% só hoje!",
    "Segue anexo o contrato atualizado para revisão.",
    "Parabéns! Você acaba de ganhar um vale-compras.",
    "Vamos almoçar juntos depois da reunião?",
    "Receba dinheiro rápido sem sair de casa!"
]

gabaritos_frases = [
    0, 1, 0, 0, 1, 0, 1, 0, 1, 0
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
    indice = 0
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


        if resultado[0] == gabaritos_frases[indice]:
            acertos += 1
            dados[0].append(frase_limpa)
            dados[1].append(int(resultado[0]))
        else:
            dados[0].append(frase_limpa)
            if resultado[0] == 0:
                dados[1].append(1)
            else:
                dados[1].append(0)

        indice += 1
        print()
    porcentagem = (acertos / len(frases_para_verificar)) * 100
    print(f'A porcentagem de acertos foi de {porcentagem:.2f}%')
    salvar_dados(caminho, dados)

caminho = 'dados_Spam_naoSpam.json'
dados = carregar_dados(caminho)

while True:
    esc = input('Verificar a porcentagem de acertos: [s/n] ').lower()
    if esc == 's':
        print('A verificação será feita automaticamente! O usuário não irá precisar corrigir!')
        print('Pode ser que aconteça erros!')
        sleep(4)
        testar_modelo()
    elif esc == 'n':
        print('Fim do programa!')
        break
    else:
        print('Por favor digite "s" ou "n"!')