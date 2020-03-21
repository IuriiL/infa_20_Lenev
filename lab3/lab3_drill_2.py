from graph import *
from tkinter import *
canvas()
windowSize(500,600)

def sun(x,y,r):
    # function draws the sun19:52 12.03.2020
    brushColor("yellow") 
    return circle(x,y,r)
    
def ship(x,y,k):
    # function draws the ship k-size of the ship
    # first draw down ship
    brushColor(40,50,100)
    rectangle(x-5*k,y,x+5*k,y+3*k)
    polygon([(x+5*k,y),(x+9*k,y),(x+5*k,y+3*k),(x+5*k,y)])
    #arc(x-8*k,y-3*k,x-2*k,y+3*k,180,270[PIESLICE,style])
    penSize(3)
    brushColor(255,255,255)
    circle(x+6*k,y+0.9*k,0.5*k)
    # ship mast 
    penSize(4)    
    penColor(0,0,0)
    line(x,y,x,y-7*k)
    # sail
    penSize(1)
    brushColor(240,240,240)
    polygon([(x+3*k,y-3.5*k),(x,y),(x+0.9*k,y-3.5*k),(x+3*k,y-3.5*k)])
    polygon([(x,y-7*k),(x+3*k,y-3.5*k),(x+0.9*k,y-3.5*k),(x,y-7*k)])

def umbrella(x,y,k):
    # draws the umbrella k-size of the umbrella
    brushColor("brown")               # the trunk of umbrella    
    rectangle(x-1,y+5,x+0.5*k,y+10*k)
    brushColor("pink")              # the cap of umbrella
    polygon([(x,y),(x-4*k,y+3*k), (x+4*k,y+3*k),(x,y)])
    penColor("black")                 # hatch the cap of umbrella
    
    for i in range(-3,4):
        line(x,y,x-i*k,y+3*k)
                
def cloud(x,y):
    # draws the cloud k- size of the cloud
    brushColor(255,255,255)
    return[circle(x,y,15),
    circle(x+10,y,15),
    circle(x-10,y+10,15),
    circle(x+10,y+10,15),
    circle(x+20,y+10,15),
    circle(x+20,y,15),
    circle(x+30,y+10,15)]
# Draw a landscape

brushColor(0,200,250)      # the sky
rectangle(0,0,500,300)
brushColor(0,100,255)      # the see
rectangle(0,300,500,450)
brushColor('orange')      # the sable
rectangle(0,450,500,600)

# Draw the units of the landscape

obj=sun(400,100,40)
umbrella(100,430,13)
obj1=cloud(40,30)
ship(350,320,15)
obj2=cloud(80,100)
obj3=cloud(350,80)
umbrella(250,420,7)
ship(110,310,6)
# Animation of the image
def keyPressed(event):
    if event.keycode==VK_ESCAPE:
        close()
def update():
    moveObjectBy(obj,-10,4)
    

onKey(keyPressed)
#onTimer(update,100)
run()



