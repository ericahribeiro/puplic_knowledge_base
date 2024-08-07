# O execício pede para criar uma variáel onde um número float entrará
#um print deve ser apresentado mostrando apenas a sua parte inteira

# Inicio o código importando a biblioteca math
import math

# Crio uma variaável input para ter um número de entrada
num=float(input('Digite um número com vírgula: '))

#Crio uma variável que irá transformar o número de entrada em inteiro
numint=math.trunc(num)

#faço um print com as variáveis
print('O número digitado é {} e a sua porção inteira é {}'.format(num, numint))
      
