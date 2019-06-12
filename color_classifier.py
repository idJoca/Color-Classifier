from nn import NeuralNetwork
import random
from graphics import *

brain = NeuralNetwork(3, 3, 2)

width = 400
height = 400
global win
win = GraphWin('Color Picker', width, height) # give title and dimensions 
random.seed(None, 2)
global r, g, b
r =  random.randint(0, 255)
g =  random.randint(0, 255)
b =  random.randint(0, 255) 
Color = color_rgb(r, g, b)
win.setBackground(Color)

text = Text(Point(width/2, height/4), "Preto")
text.setTextColor("black")
text.setSize(32)
text.draw(win)

line = Line(Point(0, height/2), Point(width, height/2))
line.draw(win)

text = Text(Point(width/2, height * 3/4), "Branco")
text.setTextColor("White")
text.setSize(32)
text.draw(win)

inputs = [r/255, g/255, b/255] 
guess = brain.guess(inputs)

if(guess.toArray()[0] > guess.toArray()[1]):
    circ = Circle(Point(width/2, height/4+ 50), 20)
    circ.setFill("black")
    circ.draw(win)
else:
    circ = Circle(Point(width/2, height * 3/4+ 50), 20)
    circ.setFill("white")
    circ.draw(win)


def getTextColor(y):    
    if (y < height/2):
        return [1, 0]
    else:
        return [0, 1]      
  
def bestColor(r, g, b):
    if (r + g + b > 300):
        return [1, 0]
    else:
        return [0, 1]

for i in range(0, 10000):     
    r =  random.randint(0, 255)
    g =  random.randint(0, 255)
    b =  random.randint(0, 255)   

    brain.train([r/255, g/255, b/255]   , bestColor(r, g, b))

while(True):       
    where = win.getMouse()     
    r =  random.randint(0, 255)
    g =  random.randint(0, 255)
    b =  random.randint(0, 255)  
    Color = color_rgb(r, g, b)
    win.setBackground(Color)     
    inputs = [r/255, g/255, b/255] 
    guess = brain.guess(inputs)    
    brain.train(inputs, getTextColor(where.getY()))  
    if(guess.toArray()[0] > guess.toArray()[1]):            
        circ.undraw()
        circ = Circle(Point(width/2, height/4+ 50), 20)
        circ.setFill("black")
        circ.draw(win)
    else:
        circ.undraw()
        circ = Circle(Point(width/2, height * 3/4+ 50), 20)
        circ.setFill("white")
        circ.draw(win)
    print(guess.toArray())
