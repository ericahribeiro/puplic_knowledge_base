# O programa visa escrever um código que escolha o maior e o
#menor número de três variáveis

#iniciei com os inputs dos3 números
pri=int(input('Digite o primeiro número:'))
seg=int(input('Digite o segundo número: '))
terc=int(input('Digite o terceiro número: '))

# Criei as condições para saber o maior de cada
if pri>seg and pri>terc:
    m=pri
if seg>pri and seg>terc:
    m=seg
if terc>seg and terc>pri:
    m=terc
print('{} é o maior número!'.format(m))

if pri<seg and pri<terc:
    me=pri
if seg<pri and seg<terc:
    me=seg
if terc<pri and terc<seg:
    me=terc
print('O menor número é {}'.format(me))