from tkinter import *
import tkinter.font as font
import random
root=Tk()
root.title("Rock Paper Sissors Game")
root.geometry("700x300")
player_score=0
computer_score=0
options=[('rock',0),('paper',1),('scissors',2)]
#computer score winning
def computer_wins():
    global computer_score,player_score
    computer_score=computer_score+1
    winner_label.config(text="Computer Won!!!!")
    computer_score_label.config(text="computer Score"+str(computer_score))
    player_score_label.config(text="Player Score"+str(player_score))
#player score winning
def player_wins():
    global computer_score,player_score
    player_score=player_score+1
    winner_label.config(text="You Won!!!!")
    computer_score_label.config(text="computer Score"+str(computer_score))
    player_score_label.config(text="Player Score"+str(player_score))
#Tie
def tie():
    global computer_score,player_score
    winner_label.config(text="It is a tie!!!!")
    computer_score_label.config(text="computer Score"+str(computer_score))
    player_score_label.config(text="Player Score"+str(player_score))
def player_choice(player_input):
    global player_score,computer_score
    print(player_input)
    computer_input=get_computer_choice()
    print(computer_input) 
    player_choice_label.config(text="You selected:"+player_input[0])
    computer_choice_label.config(text="Computer selected:"+computer_input[0])
    if (player_input==computer_input):
        tie()
    if(player_input[1]==0):
        if computer_input[1]==1:
            computer_wins()
        elif computer_input[1]==2:
            player_wins()
    if(player_input[1]==1):
        if computer_input[1]==2:
            computer_wins()
        elif computer_input[1]==0:
            player_wins()
    if(player_input[1]==2):
        if computer_input[1]==0:
            computer_wins()
        elif computer_input[1]==1:
            player_wins()
def get_computer_choice():
    return random.choice(options)
#other stuff
game_title=Label(root,text="Rock Paper scissors",font=("Impact",20,"bold"),fg="gray")
game_title.pack()
winner_label=Label(root,text="Let's start the game...",font=("Impact",15,"bold"),fg="orange",pady=3)
winner_label.pack()
inf=Frame(root)
inf.pack()
player_options=Label(inf,text="Your options:",font=("Impact",12,"bold"),fg="gray")
player_options.grid(row=0,column=0,pady=8)
rock_btn=Button(inf,text="Rock",width=15,bd=0,bg="orange",pady=5,command=lambda: player_choice(options[0]))
rock_btn.grid(row=1,column=1,padx=8,pady=5)
paper_btn=Button(inf,text="Paper",width=15,bd=0,bg="orange",pady=5,command=lambda: player_choice(options[1]))
paper_btn.grid(row=1,column=2,padx=8,pady=5)
scissors_btn=Button(inf,text="Scissors",width=15,bd=0,bg="orange",pady=5,command=lambda: player_choice(options[2]))
scissors_btn.grid(row=1,column=3,padx=8,pady=5)
score_label=Label(inf,text="Score:",font=("Impact",12,"bold"),fg='grey')
score_label.grid(row=2,column=0)
player_choice_label=Label(inf,text="You selected:---",font=("Impact",12,"bold"))
player_choice_label.grid(row=3,column=1,pady=5)
player_score_label=Label(inf,text="Your score:---",font=("Impact",12,"bold"))
player_score_label.grid(row=3,column=2,pady=5)
computer_choice_label=Label(inf,text="Computer selected:---",font=("Impact",12,"bold"))
computer_choice_label.grid(row=4,column=1,pady=5)
computer_score_label=Label(inf,text="Computer's score:---",font=("Impact",12,"bold"))
computer_score_label.grid(row=4,column=2,pady=5)
root.mainloop()