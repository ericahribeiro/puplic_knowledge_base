# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo

#comecei importando a biblioteca datetime nativa do python
from datetime import date

#criei uma variável pra salvar o ano atual
atual= date.today().year

#fiz um input para colocar a data de nascimento
nasci= int(input("Digite o seu ano de nascimento:"))
#abaixo já se calcula a idade usando a data atua e o ano de nascimento
idade= atual- nasci
print("Quem naceu em {} tem {} anos em {}".format(nasci, idade, atual))

#criam-se condições para saber se a pessoa precisa se alista ou não
if idade==18:
    print("Você precisa se alistar IMEDIATAMENTE!")
#para as demais idades é necessário fazer o cálculo se irá se alista
#ou se já se alistou, usando então uma variável específica para caso a 
#a a condição se aplique:
elif idade<18:
    saldo= 18-idade
    print("Ainda faltam {} anos para o alistamento".format(saldo))
    #Mais uma variável para mostar em que ano acontecerá o alistamento
    ano= atual+saldo
    print("Seu alistamento será em {}".format(ano))
elif idade>18:
    saldo= idade-18
    print("Você deveria ter se alistado há {} anos.".format(saldo))
    #Mais uma variável para mostar qual foi o ano de alistamento
    ano=atual-saldo
    print("Seu alistamento foi em {}".format(ano))


