def numeros(a, b, limite):
    soma = a + b
    if soma > limite:
        print(True)
    else:
        print(False)

    
p1 = int(input('Digite o primeiro: '))
p2 = int(input('Digite o segundo: '))
limite = int(input('Digite o limite: '))
numeros(p1, p2, limite)