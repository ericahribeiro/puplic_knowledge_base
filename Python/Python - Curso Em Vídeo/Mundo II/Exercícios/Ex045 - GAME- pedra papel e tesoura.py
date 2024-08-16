#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
itens= ('Pedra', 'Papel', 'Tesoura')
computador= randint (0,2)
jogador= int(input('''Suas opções:
            [0] PEDRA
            [1] PAPEL
            [2] TESOURA
            Qual é a sua jogada? '''))
print('JOH')
print('KEN')
print('POH')
print('=-'*20)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('=-'*20)
if computador== 0:
    if jogador==0:
        print('Empate')
    if jogador==1:
        print('Você Venceu')
    if jogador==2:
        print('Computador venceu')

elif computador== 1:
    if jogador== 0:
        print('Computadr Venceu')
    if jogador== 1:
        print('Empate')
    if jogador==2:
        print('Você venceu')

elif computador== 2:
    if jogador==0:
        print('Você venceu')
    if jogador== 1:
        print('Computador venceu')
    if jogador== 2:
        print('Empate')