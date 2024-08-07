# O exercício pedia para tocar uma música usando o python
#muitas bibliotecas podem ser usadas para fazer essa trefa, mas 
#o professor indicou a biblioteca pygame

# Iniciei importando a biblioteca
import pygame 

# Iniciei a biblioteca com o comando init
pygame.init()

# Iniciei  download do arquivo
pygame.mixer.music.load('rosalia.mp3')

# Dei o comando para tocar
pygame.mixer.music.play()

# Dei o comando para esperar a musica terminar para encerrar o programa
pygame.event.wait()