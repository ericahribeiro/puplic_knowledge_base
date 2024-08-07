#Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros

print('{}Lojas Ribeiro{}'.format('='*10,'='*10))
valor=float(input('Digite o valor das suas compras: R$ '))
metodo=int(input('''Escolha o modo de pagamento:
                 Opção 1: À vista/Dinheiro/cheque
                 Opção 2: À vista cartão
                 Opção 3: 2x no cartão
                 Opção 4: 3x ou mais no cartão
                 DIGITE O NÚMERO DA SUA OPÇÃO: '''))
#parcela=int(input("Deigite o número de vezes deseja pagar: "))

if metodo==1:
    total= valor-(valor*0.10)
    print('''Pagando à vista no dinheiro ou no cheque você ganha 10 por cento desconto!
As suas compras custariam R$ {:.2f} e com o desconto custarão R$ {:.2f}'''.format(valor, total))

elif metodo==2:
    total=valor-(valor*0.05)
    print('''Pagando à vista no cartão você ganha 5 por cento de desconto!
As suas compras custariam R$ {:.2f} e com o desconto custarão R$ {:.2f}'''.format(valor,total))

elif metodo==3:
    parcela=valor/2
    print('''Suas compras serão parceladas em 2x sem juros
Você pagará 2 parcelas de R$ {}'''.format(parcela))
    
elif metodo==4:
    total= valor+(valor*0.20)
    numero=int(input("Deigite o número de vezes deseja pagar: "))
    parcelas= total/numero
    print('''Suas compras serão parceladas em {} vezes de R$ {:.2f} COM JUROS.
As suas dempras de R$ {:.2f} custarão R$ {:.2f}
'''.format(numero,parcelas, valor, total ))