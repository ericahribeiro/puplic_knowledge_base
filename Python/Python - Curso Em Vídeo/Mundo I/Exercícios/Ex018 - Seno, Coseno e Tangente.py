# O exercício pedia para criar um código que recebesse 
#o valor do ângulo de entrada e calculasse o seno, coseno
#e tangente como resultado, isso tudo usando a biblioteca math

# Comecei importando a biblioteca math
import math

# Fiz uma cariaável input cpara entrar o valor do ângulo
ang=float(input('Digite o valor do ângulo: '))

# Fiz as três variáveis para calcular os valores 
cos=float(math.cos(ang))
sen=float(math.sin(ang))
tan=float(math.tan(ang))

# Fiz o print com o resultado com apenas 3 casas decimais
print('O valor do ângulo {} tem como coseno o valor {:.3f}, como seno o valor {:.3f} e como tangente o valor {:.3f}'.format(ang, cos, sen, tan))

