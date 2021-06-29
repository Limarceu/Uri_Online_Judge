subtotal=0
n=1
while n>=0:
    idd,qtde,valor = input().split()
    subtotal+= int(qtde)*float(valor)
    n-=1
print('VALOR A PAGAR: R$ {:.2f}'.format(subtotal))