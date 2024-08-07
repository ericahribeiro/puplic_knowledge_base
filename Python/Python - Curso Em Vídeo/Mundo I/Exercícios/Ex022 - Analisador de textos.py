# Este exercício vosa avaliar os o texto de entrada da variavel string

# Primeiro eu criei a variável para a entrada da string
nome= str(input("Digite o seu nome: "))

# Criei um print para informar que ue vou avaiar o nome:
print("Analisando o seu nome...")

# Criei um print para deixar o nome em caixa alta usando a funçã upper:
print('Seu nome com letras maiúsculas é: {}'.format(nome.upper()))

# Crieir um print pra deixar todas as letras minúsculas usandoa função lower:
print('Seu nome com letras minusculas é {}'.format(nome.lower()))

# Criei um print pra contar o número de letras no nome:
print('seu nome tem ao todo {} letras'.format(len(nome)))

# Criei um print mostrando o primeiro nome e quantas letras tem:
# Primeiro tem que dividir a string no meio criando uma variável com a função split:
nome.split()
# Criei uma variável com a frase dividia em forma de lista lá dentro
div=nome.split()

# Escolhemos a primeira palavra da lista ( que é a palavra zero)que o split formou:
#dentro do format colquei várias funções 
print('Seu primeiro nome é {} e tem {} letras'.format(div[0], len(div[0])))