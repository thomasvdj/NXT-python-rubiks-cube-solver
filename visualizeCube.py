from graphics import *

def getColor(number):
    if number == 1:
        return "red"
    elif number == 2:
        return  "yellow"
    elif number == 3:
        return "blue"
    elif number == 5:
        return "green"
    elif number == 4:
        return "black"
    elif number == 6:
        return "orange"
    else:
        return ""

def drawPixel(win, x, y, color):
    square = Rectangle(Point(x,y), Point(x+1,y+1))
    square.draw(win)
    square.setFill(color)
    return
    
def drawCube(win, corners, edges, finalCall=False):
    # Back
    drawPixel(win, 3, 11, getColor(corners[7][1]))
    drawPixel(win, 4, 11, getColor(edges[6][1]))
    drawPixel(win, 5, 11, getColor(corners[6][2]))
    drawPixel(win, 3, 10, getColor(edges[11][0]))
    drawPixel(win, 4, 10, "black")
    drawPixel(win, 5, 10, getColor(edges[10][0]))
    drawPixel(win, 3, 9, getColor(corners[3][2]))
    drawPixel(win, 4, 9, getColor(edges[2][1]))
    drawPixel(win, 5, 9, getColor(corners[2][1]))
    # Top
    drawPixel(win, 3, 8, getColor(corners[3][0]))
    drawPixel(win, 4, 8, getColor(edges[2][0]))
    drawPixel(win, 5, 8, getColor(corners[2][0]))
    drawPixel(win, 3, 7, getColor(edges[3][0]))
    drawPixel(win, 4, 7, "red")
    drawPixel(win, 5, 7, getColor(edges[1][0]))
    drawPixel(win, 3, 6, getColor(corners[0][0]))
    drawPixel(win, 4, 6, getColor(edges[0][0]))
    drawPixel(win, 5, 6, getColor(corners[1][0]))
    # Front
    drawPixel(win, 3, 5, getColor(corners[0][1]))
    drawPixel(win, 4, 5, getColor(edges[0][1]))
    drawPixel(win, 5, 5, getColor(corners[1][2]))
    drawPixel(win, 3, 4, getColor(edges[8][0]))
    drawPixel(win, 4, 4, "yellow")
    drawPixel(win, 5, 4, getColor(edges[9][0]))
    drawPixel(win, 3, 3, getColor(corners[4][2]))
    drawPixel(win, 4, 3, getColor(edges[4][1]))
    drawPixel(win, 5, 3, getColor(corners[5][1]))
    # Under
    drawPixel(win, 3, 2, getColor(corners[4][0]))
    drawPixel(win, 4, 2, getColor(edges[4][0]))
    drawPixel(win, 5, 2, getColor(corners[5][0]))
    drawPixel(win, 3, 1, getColor(edges[7][0]))
    drawPixel(win, 4, 1, "orange")
    drawPixel(win, 5, 1, getColor(edges[5][0]))
    drawPixel(win, 3, 0, getColor(corners[7][0]))
    drawPixel(win, 4, 0, getColor(edges[6][0]))
    drawPixel(win, 5, 0, getColor(corners[6][0]))
    # Left
    drawPixel(win, 0, 8, getColor(corners[7][2]))
    drawPixel(win, 1, 8, getColor(edges[11][1]))
    drawPixel(win, 2, 8, getColor(corners[3][1]))
    drawPixel(win, 0, 7, getColor(edges[7][1]))
    drawPixel(win, 1, 7, "green")
    drawPixel(win, 2, 7, getColor(edges[3][1]))
    drawPixel(win, 0, 6, getColor(corners[4][1]))
    drawPixel(win, 1, 6, getColor(edges[8][1]))
    drawPixel(win, 2, 6, getColor(corners[0][2]))
    # Right
    drawPixel(win, 6, 8, getColor(corners[2][2]))
    drawPixel(win, 7, 8, getColor(edges[10][1]))
    drawPixel(win, 8, 8, getColor(corners[6][1]))
    drawPixel(win, 6, 7, getColor(edges[1][1]))
    drawPixel(win, 7, 7, "blue")
    drawPixel(win, 8, 7, getColor(edges[5][1]))
    drawPixel(win, 6, 6, getColor(corners[1][1]))
    drawPixel(win, 7, 6, getColor(edges[9][1]))
    drawPixel(win, 8, 6, getColor(corners[5][2]))
    if finalCall == True:
        win.close()
    return

