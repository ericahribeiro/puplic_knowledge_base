# Escreva um programa em Python que leia um número inteiro qualquer e peça 
#para o usuário escolher qual será a base de conversão: 
#1 para binário, 2 para octal e 3 para hexadecimal

# Iniciei criando a variável de entrada:
num= int(input('Digite um número: '))
base= int(input('''Escolha os para qual base numérica deseja converter:
                2 para base BINÁRIA
                8 para base OCTAL
                16 para base HEXADECIMAL
                Digite a sua escolha: '''))
if base==2:
    print("O número {} em binário é {}".format(num, bin(num)[2:])) #bin(num) converte e [2:] elimina o código 0b do binário
elif base==8:
    print("O número {} em base octal é {}".format(num, oct(num)[2:])) #oct(num) converte e [2:] elimina o código 0o do octal
elif base==16:
    print("O número {} em base hexadecimal é {}".format(num, hex(num)[2:])) #hex(num) converte e [2:] elimina o código 0x do hexadecimal
else:
    print('''Número INVÁLIDO. Tente de novo''')