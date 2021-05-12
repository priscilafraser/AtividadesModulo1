""" Exercício 4 - Crie um programa que tenha uma função chamada voto () que vai receber como
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma
pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse
exercício, pesquise sobre a função date da biblioteca Datetime. """

""" from datetime import date

def voto(anoNasc, anoAtual):
    idade = anoAtual - anoNasc
    if idade >=18:
        print('Obrigatório')
    elif idade >=16 or idade <18:
        print('Opcional')
    else:
        print('Negado')


a= int(input('nascimento: '))
b= int(input('atual: '))
voto(a, b) """


""" from datetime import date

def voto(y):
    anoAtual = date.today().year
    idade = anoAtual - y
    if idade >= 18 and idade <= 70:
        print('VOTO OBRIGATORIO')
    elif idade >= 70:         #or idade >= 16 or idade < 18:
        print('VOTO OPCIONAL')
    else:
        print('Negado') """



from datetime import date

def voto(y):
    anoAtual = date.today().year
    idade = anoAtual - y
    if idade >= 18 and idade <= 70:
        print('VOTO OBRIGATORIO')
    elif idade >= 70:         #or idade >= 16 or idade < 18:
        print('VOTO OPCIONAL')
    else:
        print('Negado')


anoNascimento = int(input('Em que ano você nasceu?: '))
voto(anoNascimento)
