# O exercício visa ensinar sobre como trabalhar
#o início de uma string

# A tarefa consiste em verificar se a primeria palavra é de acordo
#com o requerido, que nesse caso é morar em uma cicade que começa com 
#o nome "Santo"

# Iniciei o programa com a variável de input, tamb´me coloqui um strip depois
#da variável pra eliminar os espaços antes e depois
cid=input("Digite o nome da sua cidade: ").strip()

# Agora 

# Pedi para programa printar apenas se as cinco primeiras letras fossem 
# iguais (==) a "SANTO" e trabalhei com a variável pra eliminar qualquer possibilidade de dar erro 
#por ter sido digitada com letras maiúsculas ou minúsculas usando 
# a função upper., retornará boleano
print(cid[:5].upper() =="SANTO")
