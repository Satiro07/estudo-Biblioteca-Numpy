import re
from unidecode import unidecode

def limpar(frase):
    frase = frase.lower()
    frase = unidecode(frase) # remove acentos
    print(frase)
    frase = re.sub(r'[^a-z\s]', '', frase)
    print(frase)

limpar('Olá MUndo!')