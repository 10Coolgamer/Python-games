import pygame
import pymunk
import pymunk.pygame_util

pygame.init()
sc=pygame.display.set_mode((800,600))
pygame.display.set_caption("Angry Bird Game")
clock=pygame.time.Clock()
space=pymunk.Space()
space.gravity=(0,981)
background=pygame.mixer.music.load("angry birds/Sounds/background_music.mp3")
background=pygame.mixer.music.set_volume(0.5)
background=pygame.mixer.music.play(-1)
background=pygame.mixer.music.stop()
hit=pygame.mixer.Sound("angry birds/Sounds/hit.mp3")
launch=pygame.mixer.Sound("angry birds/Sounds/launch.mp3")
lose=pygame.mixer.Sound("angry birds/Sounds/lose.mp3")
win=pygame.mixer.Sound("angry birds/Sounds/win.mp3")
draw_options=pymunk.pygame_util.DrawOptions(sc)
bird_image=pygame.image.load("angry birds/images/bird.png")
bird_image=pygame.transform.scale(bird_image,(40,40))
background_image=pygame.image.load("angry birds/images/background.jpg")
box_image=pygame.image.load("angry birds/images/wood1.png")
box_image=pygame.transform.scale(box_image,(60,60))
background_image=pygame.transform.scale(background_image,(800,600))
ground_body=pymunk.Body(body_type=pymunk.Body.STATIC)
ground_shape=pymunk.Segment(ground_body,(0,580),(800,580),5)
ground_shape.friction=0.5
space.add(ground_body,ground_shape)
PIG=pygame.image.load("angry birds/images/pig.png")
PIG=pygame.transform.scale(PIG,(60,60))

def create_bird(x,y):
    body=pymunk.Body(1,pymunk.moment_for_circle(1,0,20))
    body.position=x,y
    shape=pymunk.Circle(body,20)
    shape.elasticity=0.8
    space.add(body,shape)
    return body,shape

def create_block(x,y):
    body=pymunk.Body(1,pymunk.moment_for_box(1,(60,60)))
    body.position=x,y
    shape=pymunk.Poly.create_box(body,(60,60))
    shape.elasticity=0.4
    shape.friction=0.6
    space.add(body,shape)
    return body,shape
def create_pig(x,y):
    body=pymunk.Body(1,pymunk.moment_for_circle(1,0,20))
    body.position=x,y
    shape=pymunk.Circle(body,20)
    shape.elasticity=0.8
    space.add(body,shape)
    return body,shape
gameloop=True
score=0
attempts=3
bird_body,bird_shape=create_bird(150,500)
pigs=[create_pig(600,500),create_pig(720,500),create_pig(646,500)]
blocks=[create_block(600,520),create_block(720,520),create_block(646,520),create_block(550,520),create_block(550,490),create_block(550,440),create_block(550,390),create_block(510,490)]
def draw_objects():
    sc.blit(background_image,(0,0))
    bird_pos=bird_body.position
    sc.blit(bird_image,(bird_pos.x-20,bird_pos.y-20))
    for body,shape in blocks:
        block_pos=body.position
        angle=body.angle*(180/3.14159)
        rotated_block=pygame.transform.rotate(box_image,angle)
        rect=rotated_block.get_rect(center=(block_pos.x,block_pos.y))
        sc.blit(rotated_block,rect.topleft)
    for body,shape in pigs:
        global score
        pigs_pos=body.position
        if pigs_pos.x>800:
            pigs.remove((body,shape))
            space.remove(body,shape)
            score=score+1
        else:
            sc.blit(PIG,(pigs_pos.x,pigs_pos.y))
    font=pygame.font.SysFont("Impact",30) 
    score_text=font.render("score="+str(score),True,"black")
    if score==3 and attempts>0:
        font=pygame.font.SysFont("Impact",100)
        win_text=font.render("You Win :)",True,"orange")
        sc.blit(win_text,(100,400))
    if score<3 and attempts==0:
        font=pygame.font.SysFont("Impact",100)
        lose_text=font.render("You lose :(",True,"orange")
        sc.blit(lose_text,(100,400))
        

    sc.blit(score_text,(580,20)) 
    attempts_text=font.render("attempts="+str(attempts),True,"black")

    sc.blit(attempts_text,(290,20))
while gameloop:
    sc.fill("black")
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameloop=False
            
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            bird_body.position=150,500
            bird_body.velocity=((mouse_pos[0]-150)*5,(mouse_pos[1]-500)*5)
            attempts=attempts-1
    space.step(1/60)
    draw_objects()
    pygame.display.flip()
    clock.tick(60)
    pygame.display.update()
    

pygame.quit()