 configurações iniciais
import pygame
import random

pygame.init()
pygame.display.set_caption("Jogo Snake Python")
largura, altura = 600, 400
tela = pygame.display.set_mode((largure, altura))
relogio = pygame.time.Clock()

# cores RGB
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255, 0, 0)
verde = (0, 255, 0)

# parametros da cobrinha
tamanho_quadrado = 10
velocidade_cobra = 15

def rodar_jogo():
    fim_jogo = False

    while not fim_jogo:
       tela.fill(preta)
       
       for evento in pygame.event.get():
          if evento.type == pygame.QUIT:
            fim_jogo = True 
              
# criar um loop infinito

# desenhar os objetos do jogo na tela 
# pontuação
# cobrinha
# comida

# criar a logica de terminar o jogo
# o que aconteceu:
# cobra bateu na parede
# cobra bateu na propria cobra

# pegar a interações do usuário
# fechou a tela
# apertou as teclas do teclado pra mover a cobra

rodar_jogo()