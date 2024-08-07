# Esse exercício pede para que sejam sorteados 1 entre 4 alunos

# Iniciei importando a biblioteca random
import random

# Depois fiz as variáveis de entrada
al1=input('Digite o nome do primeiro aluno: ')
al2=input('Digite o nome do segundo aluno: ')
al3=input('Digite o nome do terceiro aluno: ')
al4=input('Digite o nome do quarto aluno: ')

# *Tive que fazer uma lista dos alinos
lista= [al1,al2, al3, al4]

# Fiz a variável com a função random que vai sortear o nome
sorte=random.choice(lista)

# Fiz o print com o nome
print('O aluno sorteado é {}'.format(sorte))

