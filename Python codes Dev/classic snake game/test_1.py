import pygame
pygame.init()
WIDTH=900
HEIGHT=500
sc=pygame.display.set_mode((WIDTH,HEIGHT))
x=450
y=400
mdx=0
mdy=0
speed=10
FPS=100
do=pygame.mixer.Sound("note1.mp3")
re=pygame.mixer.Sound("note2.mp3")
me=pygame.mixer.Sound("note3.mp3")
la=pygame.mixer.Sound("noteA.mp3")
ro=pygame.mixer.Sound("noteB.mp3")
lat=pygame.mixer.Sound("noteC.mp3")
latte=pygame.mixer.Sound("noteD.mp3")
laa=pygame.mixer.Sound("noteE.mp3")
no=pygame.mixer.Sound("no-252379.mp3")
clock=pygame.time.Clock()
pygame.display.set_caption("Xylophone")
gameloop=True
mallet=pygame.draw.rect(sc,"white",(x,y,30,30))
Bar1=pygame.draw.rect(sc,"red",(0,30,100,450))
Bar2=pygame.draw.rect(sc,"orange",(100,30,100,400))
Bar3=pygame.draw.rect(sc,"yellow",(200,30,100,350))
Bar4=pygame.draw.rect(sc,"lime",(300,30,100,300))
Bar5=pygame.draw.rect(sc,"dark blue",(400,30,100,250))
Bar6=pygame.draw.rect(sc,"purple",(500,30,100,200))
Bar7=pygame.draw.rect(sc,"pink",(600,30,100,150))
Bar8=pygame.draw.rect(sc,"red",(700,30,100,100))
Bart=pygame.draw.rect(sc,"silver",(800,30,100,50))
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    sc.fill("black")
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_LEFT:
            mdx=-1*speed
            mdy=0
        elif event.key==pygame.K_RIGHT:
            mdx=+1*speed
            mdy=0
        elif event.key==pygame.K_UP:
            mdx=0
            mdy=-1*speed
        elif event.key==pygame.K_DOWN:
            mdx=0
            mdy=+1*speed
        x=x+mdx
        y=y+mdy
    Bar1=pygame.draw.rect(sc,"red",(0,30,100,450))
    Bar2=pygame.draw.rect(sc,"orange",(100,30,100,400))
    Bar3=pygame.draw.rect(sc,"yellow",(200,30,100,350))
    Bar4=pygame.draw.rect(sc,"lime",(300,30,100,300))
    Bar5=pygame.draw.rect(sc,"dark blue",(400,30,100,250))
    Bar6=pygame.draw.rect(sc,"purple",(500,30,100,200))
    Bar7=pygame.draw.rect(sc,"pink",(600,30,100,150))
    Bar8=pygame.draw.rect(sc,"red",(700,30,100,100))
    Bart=pygame.draw.rect(sc,"silver",(800,30,100,50))
    mallet=pygame.draw.rect(sc,"white",(x,y,30,30))
    if mallet.colliderect(Bar1):
        do.play()
    if mallet.colliderect(Bar2):
        re.play()
    if mallet.colliderect(Bar3):
        me.play()
    if mallet.colliderect(Bar4):
        la.play()
    if mallet.colliderect(Bar5):
        ro.play()
    if mallet.colliderect(Bar6):
        lat.play()
    if mallet.colliderect(Bar7):
        latte.play()
    if mallet.colliderect(Bar8):
        laa.play()
    if mallet.colliderect(Bart):
        no.play()
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
