import pygame


pygame.init()
screen = pygame.display.set_mode((1050, 750))
clock = pygame.time.Clock()
running = True
dt = 0
cell_width = 30
cell_height = 14
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
vx = -1 #velocidade inicial no eixo x
vy = 10 #velocidade inicial no eixo y
bola_pos = pygame.Vector2(550, 600)
ticks = 0
timer = 0
fps = 45
alreadyout = 'no'
eligable = 'no'
entered = 'no'
font = pygame.font.SysFont(None, 36)

rects = [] #fazer bricks
for i in range(30):
    for j in range(30):
        rects.append(pygame.Rect(j*(cell_width + 5), i * (cell_height + 5), cell_width, cell_height))

while running:
    screen.fill("black") #colocar fundo preto
    ticks += 1
    if (ticks % fps == 0):  #para aparecer o timer
        timer += 1
    timer_text = font.render(f"Time: {str(timer)}", True, (255, 255, 255))   
    screen.blit(timer_text,  (85, 650))

        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    base = pygame.Rect(player_pos.x, 700, 65, 10) #configuracao da base (cor, posicao, tamanho)
    pygame.draw.rect(screen, "green", (base))

    for rect in rects:
        pygame.draw.rect(screen, "green", (rect)) #configuracao da brikcs (cor e posicao)

    keys = pygame.key.get_pressed() #movimentação da base
    if keys[pygame.K_a]:
        player_pos.x -= 400 * dt
    if keys[pygame.K_d]:
        player_pos.x += 400 * dt


    bola = pygame.Rect(bola_pos.x, bola_pos.y, 20, 14) #configuracao da bola (cor, posicao, tamanho)
    pygame.draw.rect(screen, "white", (bola))


    bola_pos.x = bola_pos.x + vx #velocidade da bola no eixo x
    bola_pos.y = bola_pos.y + vy #velocidade da bola no eixo y

    if bola_pos.y > 700-14: #colisoes da bola com a base
        if bola_pos.x > player_pos.x - 20 and bola_pos.x < player_pos.x + 60: #se colidir com a base inverte a velocidade
            vy *= -1

    
    for element in rects: #colisoes da bola com os bricks
        if bola.colliderect(element):
            if (bola_pos.y <= element.y + 14): 

                vy *= -1

            elif (bola_pos.x + 20 >= element.x):

                vx *= -1

            elif (bola_pos.x <= element.x + 30): 

                vx *= -1
          
            rects.remove(element) #quando bate remove

    if bola_pos.x==0 or bola_pos.x==1050: #colisoes com borda esquerda e direita
        vx*=-1
    
    if bola_pos.y==0: #colisoes borda de cima
        vy*=-1

    if bola_pos.y==750: #colisoes borda de baixo (perde)
        pygame.quit()
        


    pygame.display.flip()   

    dt = clock.tick(fps) / 1000 #(fps)

pygame.quit()