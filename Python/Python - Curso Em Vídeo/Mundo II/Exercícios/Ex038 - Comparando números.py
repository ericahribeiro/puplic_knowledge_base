# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
# O primeiro valor é maior
# O segundo valor é maior
# Não existe valor maior, os dois são iguais

# Iniciei criando as variáveis de entrada

primva= int(input("Digite o número do primeiro valor: "))
segva= int(input("Digite o número do segundo valor: "))

# Criei as condições:
if primva>segva:
    print("O PRIMEIRO valor é maior")
elif segva>primva:
    print("O SEGUNDO valor é maior")
else:
    print("OS valores são IGUAIS")
