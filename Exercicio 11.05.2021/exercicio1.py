def menorQue(x=0,y=0):
    if x < y:
        print (x,'é menor que',y)
    elif y < x:    
        print (y,'é menor que',x)
    else:     
        print ('Valores idênticos')
    
    return menorQue



p1 = int(input('Digite o primeiro: '))
p2 = int(input('Digite o segundo: '))
menorQue(p1, p2)
