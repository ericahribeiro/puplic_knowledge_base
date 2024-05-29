n1=float(input('Digite o valor do produto: R$ '))
n2=float(n1*0.05)
n3=n1-n2
print('O produto custava R$ {} e com o valor do desconto de 5% vai custar R$ {:.2f}'.format(n1,n3))