# O exercício visa treinar a manipulação de string para verificar a ocorrência de letras
# Na atividade deve-se contar quantas letras "A" a frase do input possui
#também verifica a primeira e a última ocorrencia da letra "A"

# Comecei criando a variável do input
frase=str(input("Digite qualquer coisa que vocÊ quiser: ")).upper()

# Criei a variável que irá contar  quantas vezes o "A" aparece
a=frase.count("A")

# Criei a variável que irá mostrar a primeira apariçõa do A
# Adicionei +1 na posição para não ficar estranho mostrar "posição zero"
ap=frase.find("A") +1

# Criei a variável que irá contar qual a última posição que o "A" aparece
# Adicionei o rfind pra começar de trás pra frente, r=right da direita pra esquerda
#Adicionei +1 na posição para excluir o zero da contagem
al=frase.rfind("A") +1

#fiz os prints

print("Essa frase tem {} letras a".format(a))
print("A primeira vez que a letra A aparece é na posição {}".format(ap))
print("A última vez que aparece é na posição {}".format(al))