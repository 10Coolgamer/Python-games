import pygame
pygame.init()
WIDTH=600
HEIGHT=600  
tdx=0
tdy=0
x=300
y=300
speed=30
fps=30
clock=pygame.time.Clock()
sc=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Tron light cycle")
gameloop=True
tron=pygame.draw.rect(sc,"green",(300,300,30,30))
body=[]
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    sc.fill("white")
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            tdx=-1*speed
            tdy=0
        elif event.key==pygame.K_RIGHT:
            tdx=+1*speed
            tdy=0
        elif event.key==pygame.K_UP:
            tdx=0
            tdy=-1*speed
        elif event.key==pygame.K_DOWN:
            tdx=0
            tdy=+1*speed
    x=x+tdx
    y=y+tdy
    pos=(x,y,30,30)
    body.append(pos)
    tron=pygame.draw.rect(sc,"green",(pos))
    for parts in body:
        pygame.draw.rect(sc,"green",(parts))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()