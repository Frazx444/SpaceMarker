import pygame #importando lib do pygame
from tkinter import simpledialog

pygame.init() #inicialização de recursos
tamanho  = (800, 600) #Variável - tamanho da tela
clock = pygame.time.Clock() #frames por segundo
tela = pygame.display.set_mode(tamanho) #tamanho da tela
pygame.display.set_caption("Space Marker") 
branco  = (255,255,255) #tupla - definindo a cor da janela
fundo = pygame.image.load("assets/starsJW.png")
posicao = ()
estrelas = {}


fonte = pygame.font.SysFont("comicsans",14)

clicksound = pygame.mixer.Sound("assets/ui-click-43196.mp3") #Var carregando som do Click

pygame.mixer.music.load("assets/space-sound-hi-low-109574.mp3") #Música de fund
pygame.mixer.music.play(-1)

tela.fill(branco) #cor
tela.blit(fundo, (0,0))

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #fechar o jogo
            quit() #comando para fechar o jogo
        elif evento.type == pygame.MOUSEBUTTONDOWN: #Se botão do mouse for press
            posicao = pygame.mouse.get_pos()
            pygame.mixer.Sound.play(clicksound) #Play som do click
            pygame.draw.circle(tela, branco, posicao, 6)
            digitenome = simpledialog.askstring('space', 'Digite o nome da estrela: ')
            nomeestrela = fonte.render(digitenome, True, branco)
            tela.blit(nomeestrela, (posicao))
     
    
    texto1 = fonte.render('Pressione F10 para Salvar os Pontos',True, branco)
    texto2 = fonte.render('Pressione F11 para Carregar os Pontos',True, branco)
    texto3 = fonte.render('Pressione F12 para Deletar os Pontos', True, branco)

    tela.blit(texto1, (10, 10))
    tela.blit(texto2, (10, 30))
    tela.blit(texto3, (10, 50))

    pygame.display.update() #novos eventos na tela
    clock.tick(60) #atualização da tela 

pygame.quit()
