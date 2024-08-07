# A aula trata das condições SE/SENÂO ou IF/ELSE 
# A tarefa é fazer um código perguntando quantos anos o carro tem e 
#classificá-lo se é velho ou novo

# Iniciamos criando uma variável de input
car=int(input('Quantos anos tem seu carro? '))

#criamos a condiçõa if para carro com 3 anos ou menos
if car<=3: 
    print('Carro novo!')
else:
    print('Carro velho!')
print('--FIM--')

# Também pode ser feita a condição simplificada:
tempo=int(input('Quantos anos tem tua caranga? '))
print('Caranga nova!'if tempo<=3 else 'Caranga véia!')
print('--FIM--')