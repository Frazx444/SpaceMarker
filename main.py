import pygame #importando lib do pygame
pygame.init() #inicialização de recursos
tamanho  = (800, 600) #Variável - tamanho da tela
clock = pygame.time.Clock() #frames por segundo
tela = pygame.display.set_mode(tamanho) #tamanho da tela
pygame.display.set_caption("Space Marker") 
branco  = (255,255,255) #tupla - definindo a cor da janela
estrelas = pygame.image.load("assets/starsJW.png")

clicksound = pygame.mixer.Sound("assets/ui-click-43196.mp3") #Var carregando som do Click

pygame.mixer.music.load("assets/space-sound-hi-low-109574.mp3") #Música de fund
pygame.mixer.music.play(-1)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #fechar o jogo
            quit() #comando para fechar o jogo
        elif evento.type == pygame.MOUSEBUTTONDOWN: #Se botão do mouse for press
            pygame.mixer.Sound.play(clicksound) #Play som do click
    
    tela.fill(branco) #cor
    tela.blit(estrelas, (0,0))
    pygame.display.update() #novos eventos na tela
    clock.tick(60) #atualização da tela 

pygame.quit()
