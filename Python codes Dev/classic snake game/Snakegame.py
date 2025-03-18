#importing pygame module
import pygame
import random
#inisilizing pygame module
pygame.init()
#creating rood window
WIDTH=600
HEIGHT=600
sc=pygame.display.set_mode((WIDTH,HEIGHT))
SNAKE_SIZE=20
APPLE_SIZE=20
head_x=WIDTH//2
head_y=HEIGHT//2
snake_dx=0
snake_dy=0
score=0
speed=10
FPS=30
clock=pygame.time.Clock()
context=pygame.font.SysFont("Press Start 2)",45)
score_text=context.render("Score: "+str(score),True,"black","dark green")
score_rect=score_text.get_rect()
score_rect.topleft =(50,50)
game_text=context.render("Game Over",True,"Black","dark green")
game_rect=game_text.get_rect()
game_rect.center =(300,300)
#Giving a title to the game 
pygame.display.set_caption("Snake Game")
eatt=pygame.mixer.Sound("eat.mp3")
#Drawing a snake head
snake=pygame.draw.rect(sc,'lime',(head_x,head_y,SNAKE_SIZE,SNAKE_SIZE))
apple_pos=(500,500,APPLE_SIZE,APPLE_SIZE)
Apple=pygame.draw.rect(sc,"red",apple_pos)
head_pos=(head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
#Making a variable
gameloop=True
gameover=False
body=[]
#making a while loop for the root window to work and update
while gameloop:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            snake_dx= -1*speed
            snake_dy=0
        elif event.key == pygame.K_RIGHT:
            snake_dx= 1*speed
            snake_dy=0
        elif event.key == pygame.K_UP:
            snake_dx=0
            snake_dy= -1*speed
        elif event.key == pygame.K_DOWN:
            snake_dx=0
            snake_dy= 1*speed
    body.insert(0,head_pos)
    body.pop()
    head_x= head_x+snake_dx
    head_y=head_y+snake_dy
    head_pos=(head_x,head_y,SNAKE_SIZE,SNAKE_SIZE)
    if snake.left <0 or snake.right > WIDTH or snake.top <0 or snake.bottom > HEIGHT or head_pos in body:
        sc.blit(game_text,game_rect)
        gameover=True
        pygame.display.update()
    if gameover:
        sc.fill("black")
        sc.blit(game_text,game_rect)
        pygame.display.update()
        pygame.time.delay(2000)
        gameloop=False
    if snake.colliderect(Apple):
        eatt.play()
        score=score=score+1
        apple_x=random.randint(50,WIDTH-50)
        apple_y=random.randint(50,HEIGHT-50)
        apple_pos=(apple_x,apple_y,APPLE_SIZE,APPLE_SIZE)
        body.append(head_pos)
    score_text=context.render("Score: "+str(score),True,"black",)
    sc.fill(" dark green")
    sc.blit(score_text,score_rect)
    for parts in body:
        pygame.draw.rect(sc,"green",parts)
    snake=pygame.draw.rect(sc,'lime',(head_x,head_y,SNAKE_SIZE,SNAKE_SIZE))
    Apple=pygame.draw.rect(sc,"red",apple_pos)
    #updating the screen
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()