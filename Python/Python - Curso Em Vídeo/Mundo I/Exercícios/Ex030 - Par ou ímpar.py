# A tarefa é criar um programa que leia se o núero é par ou ímpar

num=int(input('Digite qualquer número: '))

#se o resto da divisão por 2 é zero então é um número par
if num%2==0:
    print('{} é um número par!'.format(num))
else:
    print('{} é um número ímpar'.format(num))