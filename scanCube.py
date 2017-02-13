import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import time
from graphics import *
import threading

np.seterr(over='ignore')
corners = [0]*4
edges = [0]*4
center = 0
displayResults = True

win = GraphWin('Cube', 150, 150)
win.setCoords(0.0, 0.0, 3.0, 3.0)
win.setBackground("white")

def getAverageColorImage(cubie,cubieSize):
    average_color_per_row = np.average(cubie, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    average_color = np.uint8(average_color)
    average_color_img = np.array([[average_color]*cubieSize]*cubieSize, np.uint8)
    return average_color_img

def getAverageColor(cubie):
    average_color_per_row = np.average(cubie, axis=0)
    average_color = np.average(average_color_per_row, axis=0)
    average_color = np.uint8(average_color) 
    return average_color

def colorDistance(color1, color2):
    return np.linalg.norm(color1 - color2)

def determineColor(measuredColor):
    yellow1 = np.array([0, 220, 254])
    #yellow2 = np.array([0, 156, 198])

    red1 = np.array([26, 0, 221])
    #red2 = np.array([22, 0, 178])

    orange1 = np.array([0, 120, 255])
    #orange2 = np.array([0, 79, 220])

    blue1 = np.array([182, 87, 20])
    #blue2 = np.array([171, 88, 0])

    black1 = np.array([8, 15, 22])
    #black2 = np.array([16, 9, 4])

    green1 = np.array([58, 156, 24])
    #green2 = np.array([93, 136, 1])

    distances = np.array([0]*6)
    distances[0] = colorDistance(measuredColor,yellow1)
    #distances[1] = colorDistance(measuredColor,yellow2)
    distances[1] = colorDistance(measuredColor,red1)
    #distances[3] = colorDistance(measuredColor,red2)
    distances[2] = colorDistance(measuredColor,orange1)
    #distances[5] = colorDistance(measuredColor,orange2)
    distances[3] = colorDistance(measuredColor,blue1)
    #distances[7] = colorDistance(measuredColor,blue2)
    distances[4] = colorDistance(measuredColor,black1)
    #distances[9] = colorDistance(measuredColor,black2)
    distances[5] = colorDistance(measuredColor,green1)
    #distances[11] = colorDistance(measuredColor,green2)
    color = np.argmin(distances)
    if color == 0: #or color == 1:
        return 2 #"yellow"
    if color == 1: #or color == 3:
        return 1 #"red"
    if color == 2: #or color == 5:
        return 6 #"orange"
    if color == 3: #or color == 7:
        return 3 #"blue"
    if color == 4: #or color == 9:
        return 4# "black"
    if color == 5: #or color == 11:
        return 5 #"green"

def drawPixel(win, x, y, color):
    square = Rectangle(Point(x,y), Point(x+1,y+1))
    square.draw(win)
    square.setFill(color)
    return

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

def drawSide(win, corners, edges, center):
    drawPixel(win, 0, 2, getColor(corners[3]))
    drawPixel(win, 1, 2, getColor(edges[2]))
    drawPixel(win, 2, 2, getColor(corners[2]))
    drawPixel(win, 0, 1, getColor(edges[3]))
    drawPixel(win, 1, 1, getColor(center))
    drawPixel(win, 2, 1, getColor(edges[1]))
    drawPixel(win, 0, 0, getColor(corners[0]))
    drawPixel(win, 1, 0, getColor(edges[0]))
    drawPixel(win, 2, 0, getColor(corners[1]))

#######################################################################################################################################################################
##############################################          Take images until it has a usable one           ###############################################################
#######################################################################################################################################################################

def getSide(finalCall=False):
    cam = cv2.VideoCapture(3)
    time.sleep(0.01)
    s, img = cam.read() # captures image
    height = img.shape[0]
    width = img.shape[1]
    correctImage = False
    counter = 0

    while correctImage == False:
        imageColor = getAverageColor(img)
        for i in range(height):
            for j in range(width):
                distance = img[i,j][0] - imageColor[0]
                if abs(distance)<0.001:
                    counter = counter + 1
        if counter == height*width:
            time.sleep(0.01)
            s, img = cam.read() # captures image
            counter = 0
        else:
            correctImage = True
            counter = 0
    #OPTIONAL: OUTPUT TO FILE
    #cv2.imwrite("test.png",im) # writes image test.png to disk
    cam.release()
    #OPTIONAL: READ FROM FILE
    #img = cv2.imread('test.png')

    height = img.shape[0]
    width = img.shape[1]
    centerX = width/2+80
    centerY = height/2-10
    cubieSize = 20
    distance = 70

#######################################################################################################################################################################
##############################################          get the average color of all of the cubies           ##########################################################
#######################################################################################################################################################################

    centerCubie = img[centerY-(cubieSize/2):centerY+(cubieSize/2), centerX-(cubieSize/2):centerX+(cubieSize/2)]
    leftEdge = img[centerY-(cubieSize/2):centerY+(cubieSize/2), centerX-(cubieSize/2)-distance-cubieSize:centerX-(cubieSize/2)-distance]
    rightEdge = img[centerY-(cubieSize/2):centerY+(cubieSize/2), centerX+(cubieSize/2)+distance:centerX+(cubieSize/2)+distance+cubieSize]
    topEdge = img[centerY+(cubieSize/2)+distance:centerY+(cubieSize/2)+distance+cubieSize, centerX-(cubieSize/2):centerX+(cubieSize/2)]
    underEdge = img[centerY-(cubieSize/2)-distance-cubieSize:centerY-(cubieSize/2)-distance, centerX-(cubieSize/2):centerX+(cubieSize/2)]
    leftTopCorner = img[centerY+(cubieSize/2)+distance:centerY+(cubieSize/2)+distance+cubieSize, centerX-(cubieSize/2)-distance-cubieSize:centerX-(cubieSize/2)-distance]
    rightTopCorner = img[centerY+(cubieSize/2)+distance:centerY+(cubieSize/2)+distance+cubieSize, centerX+(cubieSize/2)+distance:centerX+(cubieSize/2)+distance+cubieSize]
    leftUnderCorner = img[centerY-(cubieSize/2)-distance-cubieSize:centerY-(cubieSize/2)-distance, centerX-(cubieSize/2)-distance-cubieSize:centerX-(cubieSize/2)-distance]
    rightUnderCorner = img[centerY-(cubieSize/2)-distance-cubieSize:centerY-(cubieSize/2)-distance, centerX+(cubieSize/2)+distance:centerX+(cubieSize/2)+distance+cubieSize]

#OPTIONAL: WRITE AVERAGE COLOR BACK TO THE SAMPLED IMAGE LOCATIONS
    img[centerY-(cubieSize/2):centerY+(cubieSize/2), centerX-(cubieSize/2):centerX+(cubieSize/2)] = getAverageColorImage(centerCubie, cubieSize)
    img[centerY-(cubieSize/2):centerY+(cubieSize/2), centerX-(cubieSize/2)-distance-cubieSize:centerX-(cubieSize/2)-distance] = getAverageColorImage(leftEdge, cubieSize)
    img[centerY-(cubieSize/2):centerY+(cubieSize/2), centerX+(cubieSize/2)+distance:centerX+(cubieSize/2)+distance+cubieSize] = getAverageColorImage(rightEdge, cubieSize)
    img[centerY+(cubieSize/2)+distance:centerY+(cubieSize/2)+distance+cubieSize, centerX-(cubieSize/2):centerX+(cubieSize/2)] = getAverageColorImage(topEdge, cubieSize) #somehow this one is on top
    img[centerY-(cubieSize/2)-distance-cubieSize:centerY-(cubieSize/2)-distance, centerX-(cubieSize/2):centerX+(cubieSize/2)] = getAverageColorImage(underEdge, cubieSize) # somehow this one is on the bottom
    img[centerY+(cubieSize/2)+distance:centerY+(cubieSize/2)+distance+cubieSize, centerX-(cubieSize/2)-distance-cubieSize:centerX-(cubieSize/2)-distance] = getAverageColorImage(leftTopCorner, cubieSize)
    img[centerY+(cubieSize/2)+distance:centerY+(cubieSize/2)+distance+cubieSize, centerX+(cubieSize/2)+distance:centerX+(cubieSize/2)+distance+cubieSize] = getAverageColorImage(rightTopCorner, cubieSize)
    img[centerY-(cubieSize/2)-distance-cubieSize:centerY-(cubieSize/2)-distance, centerX-(cubieSize/2)-distance-cubieSize:centerX-(cubieSize/2)-distance] = getAverageColorImage(leftUnderCorner, cubieSize)
    img[centerY-(cubieSize/2)-distance-cubieSize:centerY-(cubieSize/2)-distance, centerX+(cubieSize/2)+distance:centerX+(cubieSize/2)+distance+cubieSize] = getAverageColorImage(rightUnderCorner, cubieSize)

    corners = [determineColor(rightTopCorner),determineColor(rightUnderCorner),determineColor(leftUnderCorner), determineColor(leftTopCorner)]
    edges = [determineColor(rightEdge),determineColor(underEdge),determineColor(leftEdge),determineColor(topEdge)]
    center = determineColor(centerCubie)

#######################################################################################################################################################################
#######################################################          visualize all the results           ##################################################################
#######################################################################################################################################################################

    if (displayResults == True):
        drawSide(win, corners, edges, center)
#OPTIONAL: VIEW PHOTO USING MATPLOTLIB
        cv2.imwrite( "test.png", img )
##        time.sleep(0.5)
##        img = cv2.imread('test.png')
##        plt.axis("off")
##        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
##        plt.show()
    if finalCall == True:
        #threading._sleep(3.0)
        win.close()
    return [corners, edges, center]



