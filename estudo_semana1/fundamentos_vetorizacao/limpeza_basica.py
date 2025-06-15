import re

def limpar_texto(texto):
    texto = texto.lower() 
    texto = re.sub(r'[^a-zA-Z\s]', '', texto)  # remove pontuação
    return texto

print(limpar_texto("Gostei MUITO desse produto!!!"))
# saída: "gostei muito desse produto"
