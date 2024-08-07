# O exercício visa trabalahr com um programa interativo onde o computador
#e com a biblioteca random

# A tarefa é criar um progrmama e interaja com o usuário para ver se 
#a pessoa adivinha um número alatório de 0 a 5 gerado pelo computador

# Iniciei importando a função randint da biblioteca random
#essa função gera números inteiros randomizados
from random import randint
alenum= randint(0,5)
print('-=-'*10)
print('Vou pensarm em um número... ')
print('-=-'*10)
numero=int(input('Em que número eu pensei? '))
if alenum == numero:
    print('Parabéns! Èo número {}'.format(alenum))
else:
    print('Você errou! eu pensei no número {}'.format(alenum))
print('Tente outra vez!S2')