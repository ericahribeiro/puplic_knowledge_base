d=int(input('Por quantos dias você alugou o carro? '))
d2=d*60.00
k=float(input('Quantos km você rodou com o carro? '))
k2=k*0.15
t=d2+k2
print('O total a pagar é R$ {:.2f}'.format(t))