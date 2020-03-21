from graph import *


def update():
    moveObjectBy(obj,5,5)
    if xCoord(obj)>=400-20:
        close()
def keyPressed(event):
    if event.keycode==VK_ESCAPE:
        close()
brushColor(0,0,255)
rectangle(0,0,400,400)
x=100
y=100
brushColor(100,190,100)
obj=[]
obj=[(rectangle(x,y,x+20,y+20)),(rectangle(x,y+20,x+20,y+40))]
onKey(keyPressed)
onTimer(update,50)

run()


        
