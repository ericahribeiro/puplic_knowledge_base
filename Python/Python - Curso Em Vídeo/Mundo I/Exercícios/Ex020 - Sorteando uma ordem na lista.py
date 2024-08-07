# O exercício pede para sortear a ordem em que os alunos apresentarão os seu strabalhos

# Iniciei importando a biblioteca random
import random

# Fiz as variáveis de entrada para os 4 alunos
al1=input('Digite o nome do primeiro aluno: ')
al2=input('Digite o nome do segundo aluno: ')
al3=input('Digite o nome do terceiro aluno: ')
al4=input('Digite o nome do quarto aluno: ')

# Fiz uma lista com os nomes
lista=[al1, al2, al3, al4]

# *Criei a variável coma função random, achei que a função fosse randrange,
#mas era a função shuffle. Não precisava uma variável, só mandar bagunçar a lista
random.shuffle(lista)

print('A ordem de apresentação será: {}'.format(lista))