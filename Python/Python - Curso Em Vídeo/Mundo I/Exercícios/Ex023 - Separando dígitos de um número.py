# Este exercício, embora esteja dentro da aula sobre manipular textos,
#possui em sua execução conceitos matemáticos:
# A tarefa á conseguir informar quais são as unidades, dezenas, centenas e milhar
#número de input. Para isso se usa divisões inteiras (sem resto //) a operação de 
# resto de divisão (%) sucessivamente

# Criei uma variável com input para número inteiros
num=int(input("Digite um número de zero até 9.999:"))

#criei uma variável para calcular o valor da casa das unidades
# O resto da vivisão por dez vai colocar o último algarismo como resto da divisão
u=num //1 % 10

# Dividir por dez sem resto elimina o algarismo das unidades
#se depois disso, vc dividir por 10 de novo, o resto da divisão por dez 
#vai colocar o penúltimo algarismo, que agora é último algarismo, como resto da divisão
d=num// 10 %10

# Segue-se se fazendo a mesma coisa, divide por 100 e depois o resto da divisão por 10.
# Note que se você quiser encontrar o algarismo da centena, é necessário fazer divisão inteira por 100,
#se quiser encontrar o algarismo da unidade vc deve fazer divisão inteira por 1, se quiser encontrar o algarismo
#da dezena deve fazer divisão inteira por 10. Essa divisão inicial serve para colocar para trás da virgula, e depois 
#serem eliminados pela divisão inteira, os numeros à direita do algarismo que você quer encontrar. Esse algarismo poste-
#riormente vai sobrar como rest no reso da divisão (%). 
c=num//100 % 10
m=num// 1000 %10

# Printei um texto interativo
print("Analisando o número {} podemos ver que ele possui:".format(num))

#Segui com o prints de análise
print('{} unidades'.format(u))

print('{} dezenas'.format(d))

print('{} centenas'.format(c))

print('{} unidades/unidade de milhar'.format(m))