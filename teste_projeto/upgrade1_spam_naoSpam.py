from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os
from unidecode import unidecode
from time import sleep

stopwords_portugues = ['de', 'a', 'o', 'que', 'e', 'do', 'da', 'em', 'um', 'para', 'com']

frases_para_verificar = [
     "Você foi selecionado para receber um prêmio incrível, clique para confirmar.",
    "O relatório financeiro demonstra crescimento sustentável no último semestre.",
    "Ganhe acesso exclusivo a conteúdos premium se agir agora.",
    "A equipe de marketing apresentou a estratégia para o próximo trimestre.",
    "Atualize seus dados para continuar aproveitando nossos serviços.",
    "Oferta imperdível: compre um e leve dois, somente hoje!",
    "O comitê aprovou as mudanças propostas na política interna.",
    "Descubra como milhares estão aumentando a renda usando essa técnica.",
    "Está marcada uma reunião para discutir os próximos passos do projeto.",
    "Receba notificações instantâneas sobre promoções e novidades.",
    "Clique aqui e transforme sua vida financeira em poucas semanas.",
    "O departamento de RH está recrutando novos talentos para diversas áreas.",
    "Participe da pesquisa e concorra a prêmios exclusivos.",
    "Sistema apresenta instabilidade, técnicos trabalham para resolver.",
    "Invista no seu futuro com nossas dicas exclusivas de especialistas.",
    "O conselho decidiu adiar a votação sobre a reforma tributária.",
    "Parabéns, você ganhou um cupom de desconto para sua próxima compra.",
    "O time de desenvolvimento lançou a atualização corrigindo bugs críticos.",
    "Não perca a chance de ser seu próprio chefe com essa oportunidade única.",
    "Relatórios preliminares indicam melhorias significativas no desempenho."
]

gabaritos_frases = [
    0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1
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
            print('Acertei!')
        else:
            dados[0].append(frase_limpa)
            if resultado[0] == 0:
                dados[1].append(1)
            else:
                dados[1].append(0)
            print('Errei!')

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