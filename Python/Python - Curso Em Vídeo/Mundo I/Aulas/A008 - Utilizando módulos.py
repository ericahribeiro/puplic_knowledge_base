# Como usar as funcionalidades da bliblioteca math

# Primeiro vocÊ importa a Bliblioteca:
import math 
# Crie a variável de input:
num=int(input('Diga um número: '))
# Crie ima variavel com o comando que você quer fazer no número que entrou, aqui usamos o comando de raiz quadrada: 
raiz=math.sqrt(num)
# Você pode usar as funções mesmo quando cita as variáveis no format:
print("A raiz do número {} é igual a {}".format(num, math.floor(raiz)))


