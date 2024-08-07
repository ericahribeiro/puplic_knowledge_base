# Esse exercício visa trabalhar com as primeiras e últimas occorências em uma string
# A tarefa é receber o input do nome e printar o primeiro e o último nome

# Comecei criando a variável de inpute
nome=str(input('Digite o seu nonme: '))

# Criei uma variável para fazer o split (dividir a string e criar uma lista)
nomes=nome.split()

# Criei um print pra mostrar os nomes
# Não esqueça de usar colchetes quando se trata de lista
print('O se primeiro nome é {} '.format(nomes[0]))
print('O seu último nome é {}'.format(nomes[len(nomes)-1]))