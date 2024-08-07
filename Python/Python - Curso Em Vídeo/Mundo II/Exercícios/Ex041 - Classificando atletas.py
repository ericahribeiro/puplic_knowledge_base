#A Confederação Nacional de Natação precisa de um programa que l
# eia o ano de nascimento de um atleta e mostre sua categoria,
# de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JÚNIOR
#Até 25 anos: SÊNIOR
#Acima de 25 anos: MASTER

#inciei criando a variável de input para a idade
idade=int(input("Quantos anos você tem: "))

if idade<=9:
    print("Sua Categoria é MIRIM ")
elif idade>9 and idade<=14:
    print("Sua categoria é INFANTIL ")
elif idade>14 and idade<=19:
    print(" A sua categoria é JÚNIOR")
elif idade>19 and idade<=25:
    print("Sua categorai é SÊNIOR ")
else:
    print("Sua categoria é MASTER")