""" Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse
exercício, pesquise sobre a função date da biblioteca Datetime. """

import datetime

def voto(anoNasc, anoAtual):
    idade = anoAtual - anoNasc
    if idade >18:
        print('oi')


a= int(input('nascimento: '))
b= int(input('atual: '))
voto(a, b)