import pygame #importando lib do pygame
pygame.init() #inicialização de recursos
tamanho  = (800, 600) #Variável - tamanho da tela
clock = pygame.time.Clock() #frames por segundo
tela = pygame.display.set_mode(tamanho) #tamanho da tela
pygame.display.set_caption("Space Marker") 
branco  = (255,255,255) #tupla - definindo a cor da janela
estrelas = pygame.image.load("assets/starsJW.png")

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #fechar o jogo
            quit() #comando para fechar o jogo
    
    tela.fill(branco) #cor
    tela.blit(estrelas, (0,0))
    pygame.display.update() #novos eventos na tela
    clock.tick(60) #atualização da tela 

pygame.quit()
