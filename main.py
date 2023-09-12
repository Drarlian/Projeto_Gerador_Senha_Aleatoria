"""
Gerador de Senhas Aleatórias

Gera uma senha aleatória com as propriedades informadas pelo usuário.

Ao escolher 'S' nas decisões de símbolos ou números, o programa garante que independente da quantidade de caracteres
pelo menos 1 desses caracteres será de símbolos/números.
"""

from random import shuffle, choice
from validar import *


quantidade: int = validar_int('Digite a quantidade de caracteres: ')
decisao_simbolos: str = validar_caracter('Deseja adicionar símbolos especiais? [S/N] ')
decisao_numeros: str = validar_caracter('Deseja adicionar números? [S/N] ')

if quantidade > 4:
    senha: str = ''
    quantidade_final: int = quantidade

    if decisao_simbolos == 'S':
        simbolos_especiais: list = [x for x in '!@#$%=+-_*/?']
        quantidade_decisao: int = round((20/100) * quantidade)
        quantidade_final -= quantidade_decisao
        if quantidade_decisao < 1:
            quantidade_decisao = 1
        for c in range(quantidade_decisao):
            shuffle(simbolos_especiais)
            senha += choice(simbolos_especiais)

    if decisao_numeros == 'S':
        numeros: list = [numero for numero in range(1, 10)]
        quantidade_numeros: int = round((20 / 100) * quantidade)
        quantidade_final -= quantidade_numeros
        if quantidade_numeros < 1:
            quantidade_numeros = 1
        for c in range(quantidade_numeros):
            shuffle(numeros)
            senha += str(choice(numeros))

    alfabeto_minusculo: list = []
    alfabeto_maiusculo: list = []
    for letra in range(ord('a'), ord('z') + 1):  # ord() -> Pega o valor ordinal do caractere informado.
        alfabeto_minusculo.append(chr(letra))  # chr() -> Converte o valor ordinal no seu respectivo caractere.
        alfabeto_maiusculo.append(chr(letra).upper())

    shuffle(alfabeto_minusculo)
    shuffle(alfabeto_maiusculo)
    senha += choice(alfabeto_minusculo)
    senha += choice(alfabeto_maiusculo)

    quantidade_final -= 2

    lista_letras: list = []
    lista_letras.extend(alfabeto_minusculo.copy())
    lista_letras.extend(alfabeto_maiusculo.copy())

    for c in range(quantidade_final):
        shuffle(lista_letras)
        senha += choice(lista_letras)

    senha: list = [x for x in senha]
    shuffle(senha)
    senha_final: str = ''.join(senha)
    print(senha_final)
    # print(len(senha_final))

else:
    print('Quantidade Inválida')
