import pygame 

pygame.init()


clock = pygame.time.Clock()
velocidade_tick = 130 


pygame.display.set_caption("Pong")
pygame.font.init()
fonte = pygame.font.Font('summer-pixel-22.ttf', 36)

pygame.mixer.init()
som_beep = pygame.mixer.Sound("beep.mp3")

pygame.mixer.init()
som_win = pygame.mixer.Sound("ponto.mp3")

tela_largura = 1400
tela_altura = 900
tela = pygame.display.set_mode((tela_largura, tela_altura))

retangulo_largura = 24
retangulo_altura = 200
retangulo_velocidade = 8

retangulo_1_centro_x = tela_largura - retangulo_largura/2
retangulo_1_centro_y = tela_altura/2
retangulo_1 = pygame.Rect(retangulo_1_centro_x, retangulo_1_centro_y, retangulo_largura, retangulo_altura)
retangulo_1.center = (retangulo_1_centro_x, retangulo_1_centro_y)

retangulo_2_centro_x = retangulo_largura/2
retangulo_2_centro_y = tela_altura/2
retangulo_2 = pygame.Rect(retangulo_2_centro_x, retangulo_2_centro_y, retangulo_largura, retangulo_altura)
retangulo_2.center = (retangulo_2_centro_x, retangulo_2_centro_y)

pontos_1 = 0
pontos_2 = 0

linha = pygame.Rect(int(tela_largura / 2), 0, 5, tela_altura) 

bola_centro_x = tela_largura/2
bola_centro_y = tela_altura/2
bola_raio = 66
bola_velocidade_x = 5
bola_velocidade_y = 5
bola = pygame.Rect(bola_centro_x, bola_centro_y, bola_raio, bola_raio,)

"""bola_centro_x2 = tela_largura/3
bola_centro_y2 = tela_altura/3
bola_raio2 = 40
bola_velocidade_x2 = 5
bola_velocidade_y2 = 5
bola2 = pygame.Rect(bola_centro_x2, bola_centro_y2, bola_raio2, bola_raio2,)"""

while True:
    tela.fill((79, 76, 79))

    pygame.draw.rect(tela, (225, 255, 225), linha)
    pygame.draw.rect(tela, (143, 0, 225), retangulo_1)
    pygame.draw.rect(tela, (143, 0, 225), retangulo_2)
    pygame.draw.rect(tela, (0, 255, 247), bola,)

    pontos_1_texto = fonte.render("Player 1: {}".format(pontos_1), True, (255, 130, 243))
    pontos_2_texto = fonte.render("Player 2: {}".format(pontos_2), True, (0, 80, 240))
    pontos_1_retangulo = pontos_1_texto.get_rect()
    pontos_2_retangulo = pontos_2_texto.get_rect()
    pontos_1_retangulo.center = (tela_largura*0.25, tela_altura*0.95)
    pontos_2_retangulo.center = (tela_largura*0.75, tela_altura*0.95)
    tela.blit(pontos_1_texto, pontos_1_retangulo)
    tela.blit(pontos_2_texto, pontos_2_retangulo)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if bola.top <= 0 or bola.bottom >= tela_altura:
        bola_velocidade_y = -1*bola_velocidade_y
        som_beep.play()

    if bola.right >= retangulo_1.left:
        if retangulo_1.top <= bola.centery <= retangulo_1.bottom:
            bola_velocidade_x = -1*bola_velocidade_x
            som_beep.play()

    if bola.left <= retangulo_2.right:
        if retangulo_2.top <= bola.centery <= retangulo_2.bottom:
            bola_velocidade_x = -1*bola_velocidade_x
            som_beep.play()
    
    if bola.centerx >= tela_largura or bola.centerx <= 0:
        bola_centro_x = tela_largura/2
        bola_centro_y = tela_altura/2
        #pygame.mixer.init()
        #som_win = pygame.mixer.Sound("ponto.mp3")
        if bola.centerx >= tela_largura:
            pontos_1 += 1
            som_win.play()
        else:
            pontos_2 += 1
            som_win.play()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if retangulo_1.top >= 0:
            retangulo_1_centro_y -= retangulo_velocidade
    if keys[pygame.K_LEFT]:
        if retangulo_1.bottom <= tela_altura:
            retangulo_1_centro_y += retangulo_velocidade
    if keys[pygame.K_w]:
        if retangulo_2.top >= 0:
            retangulo_2_centro_y -= retangulo_velocidade
    if keys[pygame.K_s]:
        if retangulo_2.bottom <= tela_altura:
            retangulo_2_centro_y += retangulo_velocidade

    bola_centro_x += bola_velocidade_x
    bola_centro_y += bola_velocidade_y

    retangulo_1.center = (retangulo_1_centro_x, retangulo_1_centro_y)
    retangulo_2.center = (retangulo_2_centro_x, retangulo_2_centro_y)
    bola.center = (bola_centro_x, bola_centro_y)

    pygame.display.flip()
    clock.tick(velocidade_tick)

