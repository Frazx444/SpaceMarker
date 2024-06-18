import pygame #importando lib do pygame
from tkinter import simpledialog
from os import remove
from funcoes import verificaarquivo
from math import sqrt
pygame.init() #inicialização de recursos

clock = pygame.time.Clock() #frames por segundo
icone = pygame.image.load("assets/space.png") 
fundo = pygame.image.load("assets/bg.jpg")

tamanho  = (1000, 563) #Variável - tamanho da tela
tela = pygame.display.set_mode(tamanho) #tamanho da tela
pygame.display.set_caption("Space Marker")
pygame.display.set_icon(icone)
fonte = pygame.font.SysFont("comicsans",14)
clicksound = pygame.mixer.Sound("assets/ui-click-43196.mp3") #Var carregando som do Click
pygame.mixer.music.load("assets/space-sound-hi-low-109574.mp3") #Música de fund
pygame.mixer.music.play(-1)

branco  = (255,255,255) #tupla - definindo a cor da janela

def inicio():
    tela.fill(branco) #cor
    tela.blit(fundo, (0,0))

    texto1 = fonte.render('Pressione F10 para Salvar os Pontos',True, branco)
    texto2 = fonte.render('Pressione F11 para Carregar os Pontos',True, branco)
    texto3 = fonte.render('Pressione F12 para Deletar os Pontos', True, branco)

    tela.blit(texto1, (10, 10))
    tela.blit(texto2, (10, 30))
    tela.blit(texto3, (10, 50))

inicio()

estrelas = {}
linhas = []
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT: #fechar o jogo
            verificaarquivo(estrelas)
            pygame.quit() #comando para fechar o jogo

        elif evento.type == pygame.MOUSEBUTTONDOWN: #Se botão do mouse for press
            posicao = pygame.mouse.get_pos()
            pygame.mixer.Sound.play(clicksound) #Play som do click
            
            nome = simpledialog.askstring('space', 'Digite o nome da estrela: ')
            if nome == None:
                break

            elif not nome:
                nome = "desconhecido"+str(posicao)
            
            pygame.draw.circle(tela, branco, posicao, 4)
            

            estrelas[nome] = posicao
            linhas.append(posicao)  

            if len(linhas) > 1:
                pygame.draw.line(tela,branco,linhas[-1],linhas[-2],2)         

            estrela = fonte.render(nome, True, branco)
            tela.blit(estrela, (posicao))

        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                verificaarquivo(estrelas)
                quit()

            elif evento.key == pygame.K_F10:  
                verificaarquivo(estrelas)

            elif evento.key == pygame.K_F11:
                inicio()
                linhas = []
                try:
                    arquivo = open("pontossalvos.txt","r",encoding="utf-8")
                    arquivosalvo = eval(arquivo.read())
                    arquivo.close()                   
                
                    for key,value in arquivosalvo.items():                   
                        estrela = fonte.render(key, True, branco)
                        linhas.append(value)
                        tela.blit(estrela,value)
                        pygame.draw.circle(tela, branco, value, 4)               
                except:
                    pass 
                
                
                while True:
                    if len(linhas) > 1:
                        pygame.draw.line(tela, branco, linhas[0], linhas[1],2)
                    
                        calculo_distancia = sqrt((linhas[0][0] - linhas[1][0]) ** 2 + (linhas[0][1] - linhas[1][1] ) ** 2)
                        distancia = fonte.render(f"Distância: {calculo_distancia:.2f}", True, branco)
                    
                        ponto_mediox = ((linhas[1][0] + linhas[0][0]) / 2)
                        ponto_medioy = ((linhas[0][1] + linhas[1][1]) / 2) 
                        tela.blit(distancia,(ponto_mediox,ponto_medioy))
                        
                        #print(ponto_mediox)
                        #print(ponto_medioy)
                        
                        linhas.pop(0)

                    else:
                        break
               
            elif evento.key == pygame.K_F12:               
                inicio()                
                try:
                    remove("pontossalvos.txt")
                except:
                    pass
                estrelas = {}   
                linhas = []
                    
    
    pygame.display.update() #novos eventos na tela
    clock.tick(60) #atualização da tela
