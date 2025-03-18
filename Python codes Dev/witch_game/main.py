import pgzrun
from random import randint
TITLE="Potion run"
WIDTH=600
HEIGHT=500
potion=Actor("potion")
potion.pos=300,250
message=""
def draw():
    screen.blit("background",(0,0))
    potion.draw()
    screen.draw.text(message,center=(200,200),fontsize=40)
def spawn():
    potion.x=randint(50,WIDTH-50)
    potion.y=randint(50,HEIGHT-50)
def on_mouse_down(pos):
    global message
    if potion.collidepoint(pos):
        message="Good shot"
        spawn()
    else:
        message="You missed"
spawn()
pgzrun.go()