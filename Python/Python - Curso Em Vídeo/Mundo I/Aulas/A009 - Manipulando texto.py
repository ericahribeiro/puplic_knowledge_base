# A Aula trata de abordgens possíveis na hora de manupular strings

#cria-se primeiro ma string
Frase= "hoje tem mentoria"

# Podemos faer um print da frase onde vamos ver o que há nelha deade o
#caractere "envelopado" com o número 3 (quarta letra) até o décimo caractere
# * Lembre-se de usar colchetes
print(Frase[3:10])

# Lembre-se que, se não tiver número no início, então o ínicio sera o caractese 0
print(Frase[:10])

# Também pode-se aumentar a complexidade do print ao pedir para pular de dois em dois
#caracteres
print(Frase[1:10:2])

# Contar o número de vezes que um letra ocorre
print(Frase.count('o'))

# Poso juntar "funções" nas aspas depois do print citando só uma vez a mesma variável
#lembre-se que vai retornar zero se não tiver minúsculas o maúsculas
print(Frase.upper().count('O')) 

# Para descobrir o tamanho da string
print(len(Frase))

# Pode usar o ponto quando citar a variável depois do length
print(len(Frase.replace('mentoria', 'café')))

# Verifica se a palavra "hoje" está na frase
print("hoje" in Frase)

# Mostra a posição que a palavra "hoje" começa
print(Frase.find('hoje'))

# Parte as palavras da string e cria listas
print(Frase.split())

# Mostra só  aprimeira palavra da lista criada
dividido= Frase.split()
print(dividido[0])
#mostra a terceira palavra da lista criada com o split
print(dividido[2])
#mostra a letra 2 da palavra 2 da lista
print(dividido[1][1])