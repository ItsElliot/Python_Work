from graphics import*
import random
import time



#Read in and print out the data in the data file
datafile = open("data.txt",'r')


#Create graphics window
window = GraphWin("Visualisation", 500, 500)



count = 0
col = 0
colBorder = 0
    
    
for line in datafile:
    #Slow down the loop drawings
    time.sleep(0.35)
    
    
    dataCircle = float(line)
    print(line)
    
    col += 5
    colBorder += 4.2
    
    #Draw circles in each different corner
    ball1 = Circle(Point(count+0,count+0), dataCircle)
    ball1.setFill(color_rgb(col, col, col))
    ball1.setOutline(color_rgb(colBorder, colBorder, colBorder))
    ball1.draw(window)
    
    ball2 = Circle(Point(count+0,500-count), dataCircle)
    ball2.setFill(color_rgb(col, col, col))
    ball2.setOutline(color_rgb(colBorder, colBorder, colBorder))
    ball2.draw(window)
    
    ball3 = Circle(Point(500-count,count+0), dataCircle)
    ball3.setFill(color_rgb(col, col, col))
    ball3.setOutline(color_rgb(colBorder, colBorder, colBorder))
    ball3.draw(window)
    
    ball4 = Circle(Point(500-count,500-count), dataCircle)
    ball4.setFill(color_rgb(col, col, col))
    ball4.setOutline(color_rgb(colBorder, colBorder, colBorder))
    ball4.draw(window)
    
    count += 15
        
    
# Waits until the mouse is clicked before closing the window
window.getMouse()
