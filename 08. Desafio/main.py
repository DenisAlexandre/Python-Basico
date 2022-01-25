"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa (float)
* Criar variavel com o ano atual (int)
* Obter o ano de nascimento de pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa com 2)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

nome = 'Denis'
idade = 40
altura = 1.75
peso = 140
ano_atual = 2022
ano_nascimento = int(ano_atual - idade)
imc = (peso / (altura**2))

print(f'{nome} tem {idade} anos, {altura} e pesa {peso}kg.')
print(f'{nome} pesa {peso} e seu IMC é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}')