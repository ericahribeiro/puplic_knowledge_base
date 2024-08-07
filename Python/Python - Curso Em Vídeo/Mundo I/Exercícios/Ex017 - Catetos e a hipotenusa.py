# Esse exercício pede para Criar um código onde
#dois dados entraram e é necessário mostrar no print 
#o resultado calculado com o teorema de pitágoras

# Iniciamos importando a bliblioteca math para poder usar a funcionalidade hipot
#pra calcular a hipotenusa
import math

# Criamso duas variáveis para cada cateto
catop=float(input('Digite o valor do cateto oposto: '))
catad=float(input('Digite o valor do cateto adjacente: '))
hip= math.hypot(catop, catad)

print('A hipotenusa desse triângulo mede {:.2f}'.format(hip))

