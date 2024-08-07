# Desenvolva um programa que leia o comprimento de três retas e diga ao 
# usuário se elas podem ou não formar um triângulo.

# Iniciei com a criação das variáveis input:
l1=float(input('Digite o valor da primeira reta: '))
l2=float(input('Digite o valor da segunda reta: '))
l3=float(input('Digite o valor da terceita reta: '))

# Criei as condições:
if l1+l2>l3 and l2+l3>l1 and l3+l1>l2:
    print('Os lados {}, {} e {} formam um triângulo'.format(l1, l2, l3))

else:
    print('Os lados {}, {}, e {} NÂO formam um triângulo'.format(l1, l2, l3))