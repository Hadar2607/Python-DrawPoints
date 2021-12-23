# -*- coding: utf-8 -*-
"""
Created on Thu Jul 22 16:50:22 2021

@author: hadar
"""

from point import point
from path import path
import turtle 

def main():
    path1,path2 = createTwoPath() 
    print(path1) # print path1 
    print(path2) # print path2 
    path1.merge(path2) 
    print(path1) # print after merge
    t,s =forEachPath(path1)
    stop(t,s)

def createTwoPath(): # Create 2 object of path and return them. 
    path1 = path()
    path2 = path()
    path1.fillRandom(-240,240,5)
    path2.fill([0,0,270,0,270,270,0,270,0,0])
    return path1,path2 


def createTurtleObj(point): # Only in the first iteration, create object turtle
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.setup(800,700)
    turtle.shape("circle")
    turtle.color("white")
    turtle.hideturtle()
    turtle.penup()
    turtle.setposition(point.get_x(),point.get_y()) # starting point
    turtle.pendown()
    turtle.showturtle()
    return turtle,screen # return tuple 
    
def drawMidPoint(point,turtle,previous): # Calculation of distance and midpoint
    turtle.hideturtle()
    turtle.penup()
    dis = round(point.distance(previous),1)
    mid = point.midPoint(previous)
    turtle.goto(mid.get_x(),mid.get_y())
    turtle.color("purple")
    turtle.write(dis,font=("Arial", 8, "bold"))
    turtle.goto(point.get_x(),point.get_y())
    turtle.pendown()
    turtle.showturtle()
    turtle.color("white")
    return turtle
    
def stop(turtle,screen): # When finished producing the exit making route.
    turtle.hideturtle()
    screen.mainloop()
    turtle.done()

def forEachPath(path1): # take path and draw the route    
    turtle,screen,previous,count = None,None,None,1
    for p in path1:    # foreach point in the path     
        if count==1 or previous == None:  
            turtle,screen = createTurtleObj(p)
        else:
            turtle.color("white")
            turtle.goto(p.get_x(),p.get_y())              
        if count>=2: 
            turtle =drawMidPoint(p,turtle,previous)
        turtle.color("green")
        turtle.dot(7,"red")
        turtle.write(count,font=("Arial", 10, "bold"))
        count+=1     
        previous = p
        turtle.update()
    return turtle,screen 
    

if __name__ == "__main__": 
    main()
    
  
