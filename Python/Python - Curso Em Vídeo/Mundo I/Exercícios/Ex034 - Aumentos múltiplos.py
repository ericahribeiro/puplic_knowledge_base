# O exercício visa um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

# Iniciei com a variável input:
sal=float(input('Digite o valor do seu salário: R$ '))

#Fiz as condições:
if sal>1250:
    salum=float(sal+(sal*0.10))
    print("Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora.".format(sal,salum))

if sal<1250:
    saldoi=float(sal+(sal*0.15))
    print('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f} agora. '.format(sal,saldoi))