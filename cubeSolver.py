import nxt, thread, time
import nxt.bluesock
from scanCube import getSide
from getCube import stitchSides
from graphics import *
from cubeSolvingAlgorithm import getSolution
from visualizeCube import drawCube

# This is the main program that will control the robot

# setup the bluetooth connection using the MAC adress of my NXT brick
NXT1 = nxt.bluesock.BlueSock('00:16:53:02:1F:7D').connect()

# initialize motors
m = nxt.motcont.MotCont(NXT1)
#NXT1:  PORT_A move cube up/ down
#       PORT_B rotate cube holder
#       PORT_C rotate entire cube/ single side

cubeHolderStatus = 0 # 0: open 1: closed
elevatorPosition = 0 # 0: cube in holder, 1: one layer in cube chamber, 2: two layers in cube chamber, 3: entire cube in cubechamber
orientation = range(1,7) # the default orientation of the cube
direction = 0 # used to correct for undesired overshoot, it makes sure that motor C does not rotate too often in the same direction
#the overshoot in both directions roughly cancels out each other(there is also desired overshoot which is necessary to properly turn a face)

################################################################################################################################################
###################################################     FUNCTION DEFINITIONS       #############################################################
################################################################################################################################################

def allReady():
    if (m.is_ready(nxt.PORT_A) and m.is_ready(nxt.PORT_B) and m.is_ready(nxt.PORT_C)):
        return True
    else:
        return False
    
def rotateCubeHolder(wait = True):
    if wait == True:
        while allReady() == False:
            pass
    global cubeHolderStatus
    global orientation
    global elevatorPosition
    if cubeHolderStatus == 0:
        m.cmd(nxt.PORT_B, -90, 166, 1, 0, 1)
        cubeHolderStatus = 1
        if elevatorPosition == 0:
            orientation = [orientation[1],orientation[5],orientation[2],orientation[0],orientation[4],orientation[3]]
    else:
        m.cmd(nxt.PORT_B, 90, 166, 1, 0, 1)
        cubeHolderStatus = 0
        if elevatorPosition == 0:
            orientation = [orientation[3],orientation[0],orientation[2],orientation[5],orientation[4],orientation[1]]
    return

def moveElevator(target):
    global elevatorPosition
    additional = 0
    if target == 3 or elevatorPosition == 3:
        additional = 28
    if elevatorPosition == target:
        return
    while allReady() == False:
        pass
    if target > 0 and elevatorPosition == 0:
        m.cmd(nxt.PORT_A, -90, 360 + (target - 1) * 88 + additional, 1, 0, 1)
    elif target == 0 and elevatorPosition >0:
        m.cmd(nxt.PORT_A, 90, 360 + (elevatorPosition - 1) * 88 + additional, 1, 0, 0)
    elif target > elevatorPosition:
        m.cmd(nxt.PORT_A, -90, (target - elevatorPosition) * 88 + additional, 1, 0, 1)
    elif target < elevatorPosition:
        m.cmd(nxt.PORT_A, 90, (elevatorPosition - target) * 88 + additional, 1, 0, 1)
    elevatorPosition = target
    return

def rotateCubeChamber(rotation):
    correction = 0
    overshoot = 22
    global direction
    global elevatorPosition
    global orientation
    while allReady() == False:
        pass
    if rotation == 1 or rotation == 2:
        if rotation == 1 and elevatorPosition != 1:
            orientation = [orientation[0],orientation[2],orientation[3],orientation[4],orientation[1],orientation[5]]
        elif rotation == 2 and elevatorPosition != 1:
            orientation = [orientation[0],orientation[3],orientation[4],orientation[1],orientation[2],orientation[5]]
        if rotation == 2 and direction > 0:
            m.cmd(nxt.PORT_C, 90, 210 * rotation + correction + overshoot, 1, 0, 1)
            if overshoot > 0:
                direction = direction - 1
                while allReady() == False:
                    pass
                m.cmd(nxt.PORT_C, -75, overshoot, 1, 0, 1)
        else:
            m.cmd(nxt.PORT_C, -90, 210 * rotation + correction + overshoot, 1, 0, 1)
            if overshoot > 0:
                direction = direction + 1
                while allReady() == False:
                    pass
                m.cmd(nxt.PORT_C, 75, overshoot, 1, 0, 1)
    else:   # rotation == 3
        direction = direction - 1
        if elevatorPosition != 1:
            orientation = [orientation[0],orientation[4],orientation[1],orientation[2],orientation[3],orientation[5]]
        m.cmd(nxt.PORT_C, 90, 210 + correction + overshoot, 1, 0, 1)
        if overshoot > 0:
            while allReady() == False:
                pass
            m.cmd(nxt.PORT_C, -75, overshoot, 1, 0, 1)
    return

################################################################################################################################################
##########################################################     SCAN THE CUBE       #############################################################
################################################################################################################################################

print "scanning side 1"
side1 = getSide()
print "done"
moveElevator(3)
rotateCubeChamber(1)
moveElevator(0)
while allReady() == False:
    pass
print "scanning side 2"
side2 = getSide()
print "done"
moveElevator(3)
rotateCubeChamber(1)
moveElevator(0)
while allReady() == False:
    pass
print "scanning side 3"
side3 = getSide()
print "done"
moveElevator(3)
rotateCubeChamber(1)
moveElevator(0)
while allReady() == False:
    pass
print "scanning side 4"
side4 = getSide()
print "done"
moveElevator(3)
rotateCubeHolder()
moveElevator(0)
rotateCubeHolder()
while allReady() == False:
    pass
print "scanning side 5"
side5 = getSide()
print "done"
moveElevator(3)
rotateCubeChamber(2)
moveElevator(0)
while allReady() == False:
    pass
print "scanning side 6"
side6 = getSide(True)
print "done"
print ""

win = GraphWin('Cube', 450, 600)
win.setCoords(0.0, 0.0, 9.0, 12.0)
win.setBackground("white")

cube = stitchSides(side1, side2, side3, side4, side5, side6)
corners = cube[0]
edges = cube[1]
orientation = cube[2]
drawCube(win, corners, edges)

################################################################################################################################################
#########################################################     SOLVE THE CUBE       #############################################################
################################################################################################################################################

listOfCommands, cornersStates, edgesStates = getSolution(corners, edges)
count = 1
moves = len(listOfCommands)

if moves == 0:
    exit()

for command in listOfCommands:
    #The to be rotated face is on top (with respect to its current orientation)
    if orientation[0] == command[0]:
        moveElevator(1)
        rotateCubeChamber(command[1])
    #The to be rotated face is on the bottom (with respect to its current orientation)
    elif orientation[5] == command[0]:
        moveElevator(2)
        rotateCubeChamber(command[1])
    #The to be rotated face is on front or on the back (with respect to its current orientation)
    elif (orientation[1] == command[0] or orientation[3] == command[0]) and cubeHolderStatus == 0:
        moveElevator(0)
        if orientation[1] == command[0]:
            rotateCubeHolder()
            moveElevator(1)
            rotateCubeChamber(command[1])
        elif orientation[3] == command[0]:
            rotateCubeHolder()
            moveElevator(2)
            rotateCubeChamber(command[1])
    #The to be rotated face is on front or on the back (with respect to its current orientation)
    elif (orientation[1] == command[0] or orientation[3] == command[0]) and cubeHolderStatus == 1:
        moveElevator(0)
        if orientation[1] == command[0]:
            rotateCubeHolder()
            moveElevator(2)
            rotateCubeChamber(command[1])
        elif orientation[3] == command[0]:
            rotateCubeHolder()
            moveElevator(1)
            rotateCubeChamber(command[1])
    #The to be rotated face is on the left or the right (with respect to its current orientation)
    elif orientation[2] == command[0] or orientation[4] == command[0]:
        moveElevator(3)
        # rotating left or right yields a similar result, it rotates in the direction which has been chosen the least
        if direction > 0:
            rotateCubeChamber(3)
        else:
            rotateCubeChamber(1)
        moveElevator(0)
        rotateCubeHolder()
        if orientation[0] == command[0]:
            moveElevator(1)
            rotateCubeChamber(command[1])
        elif orientation[5] == command[0]:
            moveElevator(2)
            rotateCubeChamber(command[1])
    print count
    #Display an image of the current state of the cube
    if count == len(listOfCommands):
        drawCube(win, cornersStates[count - 1], edgesStates[count - 1], True)
    else:
        drawCube(win, cornersStates[count - 1],  edgesStates[count - 1])
    print "Executing move " + str(count) + " out of " + str(moves)
    count = count + 1
    
moveElevator(0)
if cubeHolderStatus == 1:
    rotateCubeHolder()
