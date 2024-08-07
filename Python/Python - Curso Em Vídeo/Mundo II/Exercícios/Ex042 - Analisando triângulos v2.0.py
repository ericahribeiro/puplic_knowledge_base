#Refaça o DESAFIO 35 dos triângulos, acrescentando o
# recurso de mostrar que tipo de triângulo será formado:
#EQUILÁTERO: todos os lados iguais
#ISÓSCELES: dois lados iguais, um diferente
#ESCALENO: todos os lados diferentes

l1=float(input('Digite o valor da primeira reta: '))
l2=float(input('Digite o valor da segunda reta: '))
l3=float(input('Digite o valor da terceita reta: '))

# Criei as condições:
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print('Os lados {}, {} e {} formam um triângulo'.format(l1, l2, l3))
    
    if l1==l2 or l1== l3 or l2==l3:
        print('Esse triâmgulo é ISÓCELES')
    
    if l1==l2 and l1==l3 and l3==l1:
        print('Esse triângulo é EQUILÁTERO')
    
    if l1!=l2 and l2!=l3 and l1!=l3:
        print('Esse triângulo é ESCALENO')
else:
    print('Os lados {}, {}, e {} NÂO formam um triângulo'.format(l1, l2, l3))