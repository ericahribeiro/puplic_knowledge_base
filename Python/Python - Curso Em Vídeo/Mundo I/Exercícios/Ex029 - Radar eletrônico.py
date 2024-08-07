# A tarefa consiste em ter a velocidade do carro no input e 
#o programa deve calcular cada km por hora a mais valendo 7 reais
#e finalizar mostrando o valor total

vel=float(input('A quantos km por hora o seu carro estava? '))
if vel>80:
    print('A multa que você deve pagar é R${:.2f}'.format((vel-80)*7))
else:
    print('Parabéns! Você naõ ultrapassou a velocidade!')