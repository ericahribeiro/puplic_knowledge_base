# O exercício é feito para que treinemos encontrar palavras dentro de uma string e se 
#for achada retornará verdadeiro, caso contrario retornará falso
# A tarefa é retornar se o sobrenome da é "silva" ou não

# Comecei criando a variável input
nome=input("Digite o seu nome completo:").upper()

print('Seu nome tem Silva? {}'.format('SILVA' in nome)) 