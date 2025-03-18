import pygame
pygame.init()
WIDTH=600
HEIGHT=600
hand_dx=0
hand_dy=0
speed=10
FPS=30
clock=pygame.time.Clock()
x=300
y=300
sc=pygame.display.set_mode((HEIGHT,WIDTH))
pygame.display.set_caption("Midas touch")
gameloop=True
pos=(x,y,30,30)
c=("blue")
b=("blue")
t=("blue")
q=("blue")
v=("blue")
r=("blue")
a=("blue")
d=("blue")
block=pygame.draw.rect(sc,"gold",pos)
block_1=pygame.draw.rect(sc,c,(550,550,30,30))
block_2=pygame.draw.rect(sc,b,(50,50,30,30))
block_3=pygame.draw.rect(sc,t,(50,550,30,30))
block_4=pygame.draw.rect(sc,q,(550,50,30,30))
block_5=pygame.draw.rect(sc,v,(275,275,30,30))
block_6=pygame.draw.rect(sc,r,(25,100,30,30))
block_7=pygame.draw.rect(sc,a,(275,100,30,30))
block_8=pygame.draw.rect(sc,d,(100,275,30,30))
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            hand_dx= -1*speed
            hand_dy=0
        elif event.key == pygame.K_RIGHT:
            hand_dx= 1*speed
            hand_dy=0
        elif event.key == pygame.K_UP:
            hand_dx=0
            hand_dy= -1*speed
        elif event.key == pygame.K_DOWN:
            hand_dx=0
            hand_dy= 1*speed
    x=x+hand_dx
    y=y+hand_dy
    pos=(x,y,30,30)
    if block.colliderect(block_1):
        c=("gold")
    if block.colliderect(block_2):
        b=("gold")
    if block.colliderect(block_3):  
        t=("gold")
    if block.colliderect(block_4):  
        q=("gold")
    if block.colliderect(block_5):  
        v=("gold")
    if block.colliderect(block_6):  
        r=("gold")
    if block.colliderect(block_7):  
        a=("gold")
    if block.colliderect(block_8):  
        d=("gold")
    sc.fill("black")
    block=pygame.draw.rect(sc,"gold",pos)
    block_1=pygame.draw.rect(sc,c,(550,550,30,30))
    block_2=pygame.draw.rect(sc,b,(25,25,30,30))
    block_3=pygame.draw.rect(sc,t,(25,550,30,30))
    block_4=pygame.draw.rect(sc,q,(550,25,30,30))
    block_5=pygame.draw.rect(sc,v,(275,25,30,30))
    block_6=pygame.draw.rect(sc,r,(25,275,30,30))
    block_7=pygame.draw.rect(sc,a,(275,550,30,30))
    block_8=pygame.draw.rect(sc,d,(550,275,30,30))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()