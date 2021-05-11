# #Faça um programa que tenha uma função chamada área(), 
# # que receba as dimensões de um terreno retangular 
# # (largura e comprimento) e mostre a área do terreno:

# def area(larg, comp):
#     area = larg*comp
#     print(f'A área do terreno é {larg} x {comp} é de {area} m².')


# #programa principal
# l = float(input('Largura (m): '))
# c = float(input('Comprimento (m): '))

# area(l, c)

#help das nossas funções
#docstrings == documentação

def area(larg, comp):
    """ 
    => função area:
    recebe 2 parametros,
    um para a largura(larg)
    outro para comprimento (comp)
    sem retorno
    criado pelo @thi.code
    """
#     area = larg*comp
#     print(f'A área do terreno é {larg} x {comp} é de {area} m².')

help(area)

#escopo de variável: escopo = espaço: variavel de scopo local, pq só pode ser 
#acessada localmente na função area.

def teste():
    global areaTerreno

    area

#retorno
def soma(n1=0, n2=0, n3=0):
    s = n1+n2+n3   #é melhor guardar o retorno em 1 variavel
    return s #ao inves do print ou (return n1+n2+n3)


print(f'as notas dos alunos: {soma(2,3,5)}')
#{soma(input('nota1: '), input('nota2: '), input('nota3: '))}
print(f'os meus seguidores: {soma(5,1,10)}')

soma(2,3,5) #notas dos alunos
soma(2,5,6) #meus seguidores insta


def media():
    som = soma(5,2,3)
    media = som/3
    return media

print(f'A média é: {media():.2f}')


def media(x,y,z):
    som = soma(x,y,z)
    media = som/3
    return media


n1=float(input('N1: '))
n2=float(input('N2: '))
n3=float(input('N3: '))
print(f'A média é: {media(n1,n2,n3):.2f}')