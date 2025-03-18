
import pygame

pygame.init()

sc=pygame.display.set_mode((700,700))
 
pygame.display.set_caption("Initals")
letter=pygame.draw.rect(sc,'lime',(250,250,20,30))
letter2=pygame.draw.rect(sc,'lime',(270,320,20,30))
letter3=pygame.draw.rect(sc,'lime',(270,320,50,30))
letter4=pygame.draw.rect(sc,'lime',(250,250,20,100))
letter5=pygame.draw.rect(sc,'lime',(250,700,20,100))
letter6=pygame.draw.rect(sc,'lime',(250,250,20,100))
letter7=pygame.draw.rect(sc,'lime',(410,230,70,20))
letter8=pygame.draw.rect(sc,'lime',(410,290,70,20))
letter9=pygame.draw.rect(sc,'lime',(410,290,100,20))
gameloop=True

while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    sc.fill(" dark green")
    letter=pygame.draw.rect(sc,'lime',(250,250,20,100))
    letter2=pygame.draw.rect(sc,'lime',(270,320,50,30))
    letter3=pygame.draw.rect(sc,'lime',(270,250,50,30))
    letter4=pygame.draw.rect(sc,'lime',(320,279,20,45))
    letter5=pygame.draw.rect(sc,'lime',(400,250,20,100))
    letter6=pygame.draw.rect(sc,'lime',(400,240,80,20))
    letter7=pygame.draw.rect(sc,'lime',(410,290,70,20))
    letter8=pygame.draw.rect(sc,'lime',(480,260,20,30))
    letter9=pygame.draw.rect(sc,'lime',(480,310,20,40))
    pygame.display.flip()
pygame.quit()