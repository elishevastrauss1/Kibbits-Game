from tkinter import *
from tkinter import messagebox
import random

dice = []

def rollDice(): 
    dice = []
    canvas.delete("all")
    random1=random.randrange(0,2)
    if random1 == 0:       
        dice.append(PhotoImage(file="Big.gif"))
    elif random1 == 1:     
        dice.append(PhotoImage(file="Small.gif"))

    random2=random.randrange(0,3)
    if random2 == 0:       
        dice.append(PhotoImage(file="Cherry.gif"))
    elif random2 == 1:     
        dice.append(PhotoImage(file="Fudge.gif"))
    elif random2 == 2:     
        dice.append(PhotoImage(file="Sprinkles.gif"))

    random3=random.randrange(0,3)
    if random3 == 0:       
        dice.append(PhotoImage(file="Chocolate.gif"))
    elif random3 == 1:     
        dice.append(PhotoImage(file="Vanilla.gif"))
    elif random3 == 2:     
        dice.append(PhotoImage(file="Strawberry.gif"))

    random4=random.randrange(0,2)
    if random4 == 0:       
        dice.append(PhotoImage(file="Cup.gif"))
    elif random4 == 1:     
        dice.append(PhotoImage(file="Cone.gif"))
    counter = 1
    for die in dice:
        canvas.create_image(10*counter, 40, image=die, anchor='nw')
        label = Label(image=die)
        label.image = die
        counter+=5

#main
canvas = Canvas(width = 225, height = 90) 
canvas.pack(expand = YES, fill = BOTH) 

B = Button(text = "Roll Dice", command = rollDice)
B.place(x = 75,y = 10)
mainloop()