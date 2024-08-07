# O exercício visa a criação de um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Deve perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado. 

# Iniciei criando as variáveis de entrada
casa= float(input("Digite o valor da casa: R$ "))
salario= float(input("Digite o valor do seu salário: R$ "))
anos= int(input("Em quantos anos deseja pagar? "))

meses= anos*12
prestacao= casa/meses
percent=salario*0.3

if percent>=salario:
    print("Para pagar uma casa de R$ {} em {} anos a prestação será de R${:.2f}".format(casa, anos, prestacao))
    print('Empréstimo CONCEDIDO!')
else:
    print("Para pagar uma casa de R$ {} em {} anos a prestação será de R${:.2f}".format(casa, anos, prestacao))
    print('Empréstimo NEGADO!')