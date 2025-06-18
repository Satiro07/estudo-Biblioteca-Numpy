from sklearn.feature_extraction.text import CountVectorizer
import re
from sklearn.linear_model import LogisticRegression
import json
import os
from unidecode import unidecode


dicionario_respostas = {
    'pergunta': [
        "Ótima pergunta! Vou te ajudar com isso.",
        "Claro! Deixe-me pensar um pouco...",
        "Essa é fácil! Olha só...",
        "Você quer saber mais sobre isso? Vamos lá."
    ],
    'elogio': [
        "Obrigado! Fico feliz que tenha gostado. 😄",
        "Você é muito gentil!",
        "Valeu pelo elogio!"
    ],
    'reclamacao': [
        "Poxa, sinto muito. Vou tentar melhorar.",
    "Desculpe por isso. O que posso fazer para ajudar?",
    "Vamos resolver isso agora mesmo!"
    ]
}

for k, v in dicionario_respostas.items():
    print(k)
    for i in v:
        print(i)
    print()