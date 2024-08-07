# O exercício visa calcular se o ano do input é bissexto ou não
# Se o número de uma ano for divisível por 4 então ele é bissexto
# Tive que importar a bliblioteca das datas
from datetime import date

#Iniciei criando a variável de input
ano=int(input('Digite o ano que você quer saber se é bissexto: '))

# Criei as concições pra digitar a data caso a pessoa digite zero
# Criei as condições pra saber se a divisão popr 4 é igual a zero
if ano==0:
    ano=date.today().year
if ano%4==0:
    print('{} é uma ano BISSEXTO'.format(ano))
else:
    print('{} não é um ano bissexto'.format(ano))