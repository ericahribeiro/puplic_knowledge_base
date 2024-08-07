# O exercício visa calcular o preço da passgem de acordo com 
#a distância de uma viagem: Se a viagem é até 200km o valor da passagme é 0,50 por km
#se é maior que 200km o valor  da passagemé 0.45 por km

# Iniciei criando a variável input para os kms
km=float(input('Digite a distância da sua viajem em quilômetros: '))

# Fiz as condições
if km<200:
    print('O valor da sua passagem é R$ {:.2f}'.format(km*0.45))
else:
    print('O valor da sua passagem é R$ {:.2f}'.format(km*0.50))
    