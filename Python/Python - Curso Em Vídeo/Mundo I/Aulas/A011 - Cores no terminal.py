# Qua9ndo quiser indicar uma cor para as letras o o background da linha,
#você precisa começar como contra barra zero trinta e três  e abrir colchete 
#\033[
# Dentro dos colchetes você pode colocar os códigos para estilo (de 1 a 4)
#os códigos para cor de letra (de 30 ate 37) e os códigos para cor de background
#(que vão de 40 até 47). Quando desejar que o estilo termine no texto, finalize
#com \033[m

# Dentro dos colchetes você deve digitar primeiro o estilo e separar por ponto e 
#vírgula ';'. Depois deve digitar a cor da letra e separar poe ponto e vírgula;
#depois deve escolher o preeenchimento e fechar com m. 
#Ex: \033[1;34;43m  e para finalizar depois da frase \033[m

# Exemplos das estilo:
print('\033[0m Sem estilo é o zero\033[m')
print('\033[1m Estilo 1 è bold (ou negrito)\033[m')
print('\033[4m Estilo 4 é sublinhado \033[m')
print('\033[7m Estilo 7 inverte os estilos \033[m')

# Exemplo de cores nas letras:
print('\033[0;30m Letra Cinza \033[m') #o zero no início do colchetes significa sem estilo.
print('\033[0;31m Letra Vermelha \033[m')
print('\033[0;32m Letra Verde \033[m')
print('\033[0;33m Letra Amarela \033[m')
print('\033[0;34m Letra Lilás \033[m')
print('\033[0;35m Letra Rosa \033[m')
print('\033[0;36m Letra Azul \033[m')
print('\033[0;37m Letra Branca \033[m')

# Exemplo de preenchimento
print('\033[0;0;40m Preenchimento Preto \033[m') #os dois zeros depois do colchete significa sem estilo e sem cor na letra
print('\033[0;0;41m Preenchimento Vermelho \033[m')
print('\033[0;0;42m Preenchimento Verde \033[m')
print('\033[0;0;43m Preenchimento Amarelo \033[m')
print('\033[0;0;44m Preenchimento Lilás \033[m')
print('\033[0;0;45m Preenchimento Rosa \033[m')
print('\033[0;0;46m Preenchimento Azul \033[m')
print('\033[0;0;47m Preenchimento Branco \033[m')

# Você também pode misturar estilos e cores:
print('\033[1;36;41m EStilo bold, letra azul e preenchimento vermelho \033[m')

# Como não existe letra preta porque o terminal normalment é preto, você consegue
#letra preta colocando branco no preenchimentoe invertendo os esilos com o 7 no início
print('\033[7;37;40m Estilo 7 (invertido), letra branca  preenchimento preto \033[m')