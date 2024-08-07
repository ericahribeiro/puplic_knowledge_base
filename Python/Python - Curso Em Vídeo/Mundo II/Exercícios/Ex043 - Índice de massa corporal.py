#Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida

# Eu iniciei crand a variável de input para a entrada dos daso de masa coporal
massa=float(input("Digite a sua massa em kg: "))
# Crei a variável de altura:
altura= float(input("Digite a sua altura em metros: "))
#Criei a variável pra calcular o IMC
imc=massa/altura**2

if imc<18.5:
    print("Seu IMC é igual a {:.2f} e está abaixo de 18.5. Você está ABAIXO de peso ideal.".format(imc))
    
if imc>=18.5 and imc<25:
    print("Seu IMC é igual a {:.2f} e está entre 18.5 e 25. Você possui o peso IDEAL".format(imc))

if imc>=25 and imc<30:
    print("Seu IMC é igual a {:.2f} e está entre 25 e 30. Te classificando com SOBREPESO.".format(imc))

if imc>=30 and imc<40:
    print("Seu IMC é igual a {:.2f} e está entre 30 e 40. Te classificando com OBESIDADE.".format(imc))

if imc>40:
    print("Sei IMC é igual a {:.2f}, acima de 40 pontos. Isso te classifica com OBESIDADE MÓRBIDA.".format(imc))
    




