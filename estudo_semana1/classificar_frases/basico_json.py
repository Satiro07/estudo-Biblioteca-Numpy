import json

minha_lista = ['eu gostei', 'não gostei', 'ótimo', 'péssimo']

with open('dados.json', 'w', encoding='utf-8') as arquivo:
    json.dump(minha_lista, arquivo, ensure_ascii=False, indent=4)


with open('dados.json', 'r') as arquivo:
    minha_lista = json.load(arquivo)
print(minha_lista)