#############################################################################################################################################
###################################################     Initialize variables       ##########################################################
#############################################################################################################################################

from graphics import *
import time
import random

solvedCorners = [[1,2,5],[1,3,2],[1,4,3],[1,5,4],[6,5,2],[6,2,3],[6,3,4],[6,4,5]]
solvedEdges = [[1,2],[1,3],[1,4],[1,5],[6,2],[6,3],[6,4],[6,5],[2,5],[2,3],[4,3],[4,5]]
listOfCommands = []
#dummyVariable1 = 0
#dummyVariable2 = 0

#############################################################################################################################################
###################################################     Function definitions       ##########################################################
#############################################################################################################################################

#### Functions for position and orientation of corners ####

def getCorners(side):
    if side == 1:
        return [0,1,2,3]
    elif side == 2:
        return [4,5,1,0]
    elif side == 3:
        return [5,6,2,1]
    elif side == 5:
        return [7,4,0,3]
    elif side == 4:
        return [6,7,3,2]
    elif side == 6:
        return [7,6,5,4]
    else:
        return []

def rotateSingleCorner(corner,singleRotation):
    rotatedCorner = [1,2,3]
    if singleRotation == 1: #counterclockwise
        rotatedCorner[0] = corner[2]
        rotatedCorner[2] = corner[1]
        rotatedCorner[1] = corner[0]
    else: #singleRotation == 2 clockwise
        rotatedCorner[0] = corner[1]
        rotatedCorner[1] = corner[2]
        rotatedCorner[2] = corner[0]
    return rotatedCorner

def getCornerOrientation(corner):
    if solvedCorners.count(corner)>0:
        return 0
    elif solvedCorners.count(rotateSingleCorner(corner,2)):
        return 1
    else:
        return 2
    
def findSingleCorner(corner):
    # finds index of a corner in the list of corners
    if corners.count(corner) > 0:
        return corners.index(corner)
    elif corners.count(rotateSingleCorner(corner,1)):
        return corners.index(rotateSingleCorner(corner,1))
    else:
        return corners.index(rotateSingleCorner(corner,2))

def rotateCornerPosition(side,rotation):
    # Rotate position of corners, orientation may be incorrect
    listOfCorners = getCorners(side)
    global corners
    if rotation == 1:
        dummyVariable1 = corners[listOfCorners[0]]
        corners[listOfCorners[0]] = corners[listOfCorners[1]]
        corners[listOfCorners[1]] = corners[listOfCorners[2]]
        corners[listOfCorners[2]] = corners[listOfCorners[3]]
        corners[listOfCorners[3]] = dummyVariable1
    elif rotation == 2:
        dummyVariable1 = corners[listOfCorners[0]]
        dummyVariable2 = corners[listOfCorners[1]]
        corners[listOfCorners[0]] = corners[listOfCorners[2]]
        corners[listOfCorners[1]] = corners[listOfCorners[3]]
        corners[listOfCorners[2]] = dummyVariable1
        corners[listOfCorners[3]] = dummyVariable2
    elif rotation == 3:
        dummyVariable1 = corners[listOfCorners[0]]
        corners[listOfCorners[0]] = corners[listOfCorners[3]]
        corners[listOfCorners[3]] = corners[listOfCorners[2]]
        corners[listOfCorners[2]] = corners[listOfCorners[1]]
        corners[listOfCorners[1]] = dummyVariable1
    else:
        return
    return

def rotateCornerOrientation(side, rotation):
    # Rotate orientation of the corners after the position has been rotated
    # Orientation is already correct if side == 1, side == 6 or rotation == 2
    global corners
    listOfCorners = getCorners(side)
    if (side == 2 or side == 3 or side == 4 or side == 5):
        if (rotation == 1 or rotation == 3):
            corners[listOfCorners[0]] = rotateSingleCorner(corners[listOfCorners[0]],1)
            corners[listOfCorners[1]] = rotateSingleCorner(corners[listOfCorners[1]],2)
            corners[listOfCorners[2]] = rotateSingleCorner(corners[listOfCorners[2]],1)
            corners[listOfCorners[3]] = rotateSingleCorner(corners[listOfCorners[3]],2)
        else:
            return
    return

#### Functions for position and orientation of edges ####

def getEdgesIndices(side):
    if side == 1:
        return [0,1,2,3]
    elif side == 2:
        return [4,9,0,8]
    elif side == 3:
        return [5,10,1,9]
    elif side == 5:
        return [7,8,3,11]
    elif side == 4:
        return [6,11,2,10]
    elif side == 6:
        return [6,5,4,7] #should only be called in functions used by rotateSide(), not when solving
    else:
        return []

def flipSingleEdge(edge, flip):
    if flip == 1:
        return [edge[1],edge[0]]
    else:
        return edge

def rotateListOfFour(someList):
    # rotates a list of four, counterclockwise
    finalList = [0]*4
    finalList[0] = someList[1]
    finalList[1] = someList[2]
    finalList[2] = someList[3]
    finalList[3] = someList[0]
    return finalList

def findSingleEdge(edge):
    global edges
    if edges.count(edge)>0:
        return edges.index(edge)
    else:
        return edges.index(flipSingleEdge(edge,1))

def getEdges(side):
    global edges
    trueEdges = []
    edgesIndices = getEdgesIndices(side)
    for i in range(4):
        trueEdges.append(edges[edgesIndices[i]])
    return trueEdges

def getEdgeOrientation(edge):
    if solvedEdges.count(edge)>0:
        return 0
    else:
        return 1

def rotateEdgePosition(side, rotation):
    # Rotate edge position, orientation may still be incorrect
    global edges
    listOfEdges = getEdgesIndices(side)
    if rotation == 1:
        dummyVariable1 = edges[listOfEdges[0]]
        edges[listOfEdges[0]] = edges[listOfEdges[1]]
        edges[listOfEdges[1]] = edges[listOfEdges[2]]
        edges[listOfEdges[2]] = edges[listOfEdges[3]]
        edges[listOfEdges[3]] = dummyVariable1
    elif rotation == 2:
        dummyVariable1 = edges[listOfEdges[0]]
        dummyVariable2 = edges[listOfEdges[1]]
        edges[listOfEdges[0]] = edges[listOfEdges[2]]
        edges[listOfEdges[1]] = edges[listOfEdges[3]]
        edges[listOfEdges[2]] = dummyVariable1
        edges[listOfEdges[3]] = dummyVariable2
    elif rotation == 3:
        dummyVariable1 = edges[listOfEdges[0]]
        edges[listOfEdges[0]] = edges[listOfEdges[3]]
        edges[listOfEdges[3]] = edges[listOfEdges[2]]
        edges[listOfEdges[2]] = edges[listOfEdges[1]]
        edges[listOfEdges[1]] = dummyVariable1
    else:
        return
    return

def rotateEdgeOrientation(side, rotation):
    # Rotate edge orientation after the position has been rotated
    # Orientation is only incorrect when:
    global edges
    listOfEdges = getEdgesIndices(side)
    if (side == 2 or side == 4):
        if rotation != 2:
            for i in range(4):
                edges[listOfEdges[i]] = flipSingleEdge(edges[listOfEdges[i]],1)
    return

#### Function that uses the previous functions to perform a rotation ####

def rotateSide(side, rotation):
    global listOfCommands
    global edges
    global corners
    if rotation == 0:
        pass
    else:
        rotateCornerPosition(side, rotation)
        rotateCornerOrientation(side, rotation)
        rotateEdgePosition(side, rotation)
        rotateEdgeOrientation(side, rotation)
        if rotation != 0:
            listOfCommands.append([side, rotation])
    return

def solveFinalPhase():
    global edges
    global corners
    commands = []
    for i in range(4):
        # check if cube is already solved
        if (edges == solvedEdges and corners == solvedCorners):
            break
        # RESTRICTED OPTIONS
        # check if edges are already correct, corners in incorrect position
        elif (edges == solvedEdges):
            if (corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+3)%4] and corners[(i+2)%4] == solvedCorners[(i+1)%4] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #1
                commands = [[3,3],[2,1],[3,3],[4,2],[3,1],[2,3],[3,3],[4,2],[3,2]]
            elif (corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+2)%4] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[(i+1)%4]): #2
                commands = [[3,2],[4,2],[3,1],[2,1],[3,3],[4,2],[3,1],[2,3],[3,1]]
            elif (corners[i] == solvedCorners[(i+1)%4] and corners[(i+1)%4] == solvedCorners[i] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #3
                commands = [[2,1],[3,3],[2,3],[5,1],[2,1],[3,1],[2,3],[5,2],[4,3],[3,1],[4,1],[5,1],[4,3],[3,3],[4,1]]
        # check if corners are already correct, edges in incorrect position
        elif (corners == solvedCorners):
            if (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[(i+2)%4]): #4
                commands = [[3,3],[1,1],[3,3],[1,3],[3,3],[1,3],[3,3],[1,1],[3,1],[1,1],[3,2]] #(R' U R') U' R' U' (R' U) R U R2
            elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+3)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4]): #5
                commands = [[3,2],[1,3],[3,3],[1,3],[3,1],[1,1],[3,1],[1,1],[3,1],[1,3],[3,1]] #(R2 U') R' U' R U R U (R U' R)
            elif (edges[i] == solvedEdges[(i+3)%4] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[i]): #6
                commands = [[3,3],[1,3],[3,1],[1,3],[3,1],[1,1],[3,1],[1,3],[3,3],[1,1],[3,1],[1,1],[3,2],[1,3],[3,3],[1,2]] #R' U' (R U') R U (R U') (R' U) R U (R2 U') R'
            elif (edges[i] == solvedEdges[(i+2)%4] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[i] and edges[(i+3)%4] == solvedEdges[(i+1)%4]): #7
                commands = [[5,2],[3,2],[6,1],[5,2],[3,2],[1,2],[5,2],[3,2],[6,1],[3,2],[5,2]]
        # check if 2 adjacent corners and 2 edges need to be permuted
        elif (edges[i] == solvedEdges[(i+1)%4] and edges[(i+1)%4] == solvedEdges[i] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+3)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+2)%4] and corners[(i+2)%4] == solvedCorners[(i+1)%4] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #8
            commands = [[3,1],[1,1],[3,3],[2,3],[3,1],[1,1],[3,3],[1,3],[3,3],[2,1],[3,2],[1,3],[3,3],[1,3]] #R (U R') F' R (U R') U' (R' F) (R2 U') R'
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[(i+3)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+2)%4] and corners[(i+2)%4] == solvedCorners[(i+1)%4] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #9
            commands = [[5,3],[3,3],[1,2],[3,1],[1,1],[3,3],[1,2],[5,1],[1,3],[3,1],[1,1]] #L' R' U2 R (U R') U2 (L U' R) [1,1] WAS ADDED LATER
        elif (edges[i] == solvedEdges[(i+1)%4] and edges[(i+1)%4] == solvedEdges[i] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+3)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #10
            commands = [[3,3],[1,2],[3,1],[1,2],[3,3],[2,1],[3,1],[1,1],[3,3],[1,3],[3,3],[2,3],[3,2],[1,3]] #(R' U) U (R U') U' (R' F) R (U R') U' R' F' R2
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[(i+3)%4] and
              corners[i] == solvedCorners[(i+1)%4] and corners[(i+1)%4] == solvedCorners[i] and corners[(i+2)%4] == solvedCorners[(i+2)%4] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #11
            commands = [[3,1],[1,2],[3,3],[1,2],[3,1],[4,3],[3,3],[1,3],[3,1],[1,1],[3,1],[4,1],[3,2],[1,1]] #(R U') U' (R' U) U (R B') R' U' R U R B R2
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+2)%4] and corners[(i+2)%4] == solvedCorners[(i+1)%4] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #12
            commands = [[3,1],[1,1],[3,3],[1,3],[3,3],[2,1],[3,2],[1,3],[3,3],[1,3],[3,1],[1,1],[3,3],[2,3]] #R (U R') U' (R' F) (R2 U') R' U' R (U R') F'
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #13
            commands = [[3,3],[1,1],[3,1],[1,3],[3,2],[2,3],[1,3],[2,1],[1,1],[3,1],[2,1],[3,3],[2,3],[3,2],[1,3]]
        # check if 2 opposite corners and edges need to be permuted
        elif (edges[i] == solvedEdges[(i+1)%4] and edges[(i+1)%4] == solvedEdges[i] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+3)%4] and
              corners[i] == solvedCorners[(i+2)%4] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[i] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #14
            commands = [[5,3],[1,1],[3,1],[1,3],[5,1],[1,1],[5,3],[1,1],[3,3],[1,3],[5,1],[1,2],[3,1],[1,2],[3,3]]
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+1)%4] and edges[(i+2)%4] == solvedEdges[(i+3)%4] and edges[(i+3)%4] == solvedEdges[(i+2)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+3)%4] and corners[(i+2)%4] == solvedCorners[(i+2)%4] and corners[(i+3)%4] == solvedCorners[(i+1)%4]): #15
            commands = [[2,1],[3,1],[1,3],[3,3],[1,3],[3,1],[1,1],[3,3],[2,3],[3,1],[1,1],[3,3],[1,3],[3,3],[2,1],[3,1],[2,3]] #F (R U') R' U' R (U R') F' R (U R') U' (R' F) (R F')
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4] and
              corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+3)%4] and corners[(i+2)%4] == solvedCorners[(i+2)%4] and corners[(i+3)%4] == solvedCorners[(i+1)%4]): #16
            commands = [[3,3],[1,1],[3,1],[1,3],[3,3],[2,3],[1,3],[2,1],[3,1],[1,1],[3,3],[2,1],[3,3],[2,3],[3,1],[1,3],[3,1]] #(R' U) (R U') R' F' U' F R (U R') F R' (F' R) (U' R)
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4] and
              corners[i] == solvedCorners[(i+2)%4] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[i] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #17
            commands = [[3,1],[1,3],[3,3],[1,1],[3,1],[4,1],[1,1],[4,3],[3,3],[1,3],[3,1],[4,3],[3,1],[4,1],[3,3],[1,1],[3,3]]
        # check if 3 corners and 3 edges need to be permuted
        elif (edges[i] == solvedEdges[(i+2)%4] and edges[(i+1)%4] == solvedEdges[(i+1)%4] and edges[(i+2)%4] == solvedEdges[(i+3)%4] and edges[(i+3)%4] == solvedEdges[i] and
              corners[i] == solvedCorners[(i+3)%4] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[i] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #18
            commands = [[3,1],[1,1],[3,3],[2,2],[6,3],[5,1],[1,3],[5,3],[1,1],[5,3],[6,1],[2,2]]
        elif (edges[i] == solvedEdges[(i+3)%4] and edges[(i+1)%4] == solvedEdges[i] and edges[(i+2)%4] == solvedEdges[(i+2)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4] and
              corners[i] == solvedCorners[(i+1)%4] and corners[(i+1)%4] == solvedCorners[(i+3)%4] and corners[(i+2)%4] == solvedCorners[(i+2)%4] and corners[(i+3)%4] == solvedCorners[i]): #19
            commands = [[3,2],[6,3],[2,1],[1,3],[2,1],[1,1],[2,3],[6,1],[3,2],[4,1],[1,3],[4,3]]
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[(i+2)%4] and
              corners[i] == solvedCorners[(i+2)%4] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[i]): #20
            commands = [[2,3],[1,3],[2,1],[3,2],[6,1],[4,3],[1,1],[4,1],[1,3],[4,1],[6,3],[3,2]]
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+3)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4] and
              corners[i] == solvedCorners[(i+3)%4] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[i] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #21
            commands = [[3,2],[6,1],[4,3],[1,1],[4,3],[1,3],[4,1],[6,3],[3,2],[2,3],[1,1],[2,1]]
        # shift commands to the correct perspective
        if len(commands) > 0:
            #print commands
            for command in commands:
                if (command[0] != 1 and command[0] != 6):
                    rotateSide(((i+command[0]-2) % 4)+2,command[1])
                else:
                    rotateSide(command[0],command[1])
            break;
    commands = []
    return

def solveFinalPhase2():
    global edges
    global corners
    commands = []
    for i in range(4):
        # check if cube is already solved
        if (edges == solvedEdges and corners == solvedCorners):
            break
        # OPTIONS WITHOUT RESTRICTIONS FOR EDGES
        # check if edges are already correct, corners in incorrect position
        if (corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+3)%4] and corners[(i+2)%4] == solvedCorners[(i+1)%4] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #1
            commands = [[3,3],[2,1],[3,3],[4,2],[3,1],[2,3],[3,3],[4,2],[3,2]]
        elif (corners[i] == solvedCorners[i] and corners[(i+1)%4] == solvedCorners[(i+2)%4] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[(i+1)%4]): #2
            commands = [[3,2],[4,2],[3,1],[2,1],[3,3],[4,2],[3,1],[2,3],[3,1]]
        elif (corners[i] == solvedCorners[(i+1)%4] and corners[(i+1)%4] == solvedCorners[i] and corners[(i+2)%4] == solvedCorners[(i+3)%4] and corners[(i+3)%4] == solvedCorners[(i+2)%4]): #3
            commands = [[2,1],[3,3],[2,3],[5,1],[2,1],[3,1],[2,3],[5,2],[4,3],[3,1],[4,1],[5,1],[4,3],[3,3],[4,1]]
        elif (corners[i] == solvedCorners[(i+2)%4] and corners[(i+1)%4] == solvedCorners[(i+1)%4] and corners[(i+2)%4] == solvedCorners[i] and corners[(i+3)%4] == solvedCorners[(i+3)%4]): #14
            commands = [[5,3],[1,1],[3,1],[1,3],[5,1],[1,1],[5,3],[1,1],[3,3],[1,3],[5,1],[1,2],[3,1],[1,2],[3,3]]
        elif (corners[(i+1)%4] == solvedCorners[(i+2)%4] and corners[(i+2)%4] == solvedCorners[(i+1)%4]):
            commands = [[5,3],[3,3],[1,2],[3,1],[1,1],[3,3],[1,2],[5,1],[1,3],[3,1],[1,1]]
        # shift commands to the correct perspective
        if len(commands) > 0:
            #print commands
            for command in commands:
                if (command[0] != 1 and command[0] != 6):
                    rotateSide(((i+command[0]-2) % 4)+2,command[1])
                else:
                    rotateSide(command[0],command[1])
            break;
    commands = []
    return

def solveFinalPhase3():
    global edges
    global corners
    commands = []
    for i in range(4):
        # check if cube is already solved
        if (edges == solvedEdges and corners == solvedCorners):
            break
        # OPTIONS WITHOUT RESTRICTIONS FOR CORNERS
        # check if edges are already correct, corners in incorrect position
        if (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[(i+2)%4]): #4
            commands = [[3,3],[1,1],[3,3],[1,3],[3,3],[1,3],[3,3],[1,1],[3,1],[1,1],[3,2]] #(R' U R') U' R' U' (R' U) R U R2
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+3)%4] and edges[(i+3)%4] == solvedEdges[(i+1)%4]): #5
            commands = [[3,2],[1,3],[3,3],[1,3],[3,1],[1,1],[3,1],[1,1],[3,1],[1,3],[3,1]] #(R2 U') R' U' R U R U (R U' R)
        elif (edges[i] == solvedEdges[(i+3)%4] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[i]): #6
            commands = [[3,3],[1,3],[3,1],[1,3],[3,1],[1,1],[3,1],[1,3],[3,3],[1,1],[3,1],[1,1],[3,2],[1,3],[3,3],[1,2]] #R' U' (R U') R U (R U') (R' U) R U (R2 U') R'
        elif (edges[i] == solvedEdges[(i+2)%4] and edges[(i+1)%4] == solvedEdges[(i+3)%4] and edges[(i+2)%4] == solvedEdges[i] and edges[(i+3)%4] == solvedEdges[(i+1)%4]): #7
            commands = [[5,2],[3,2],[6,1],[5,2],[3,2],[1,2],[5,2],[3,2],[6,1],[3,2],[5,2]]
        elif (edges[i] == solvedEdges[i] and edges[(i+1)%4] == solvedEdges[(i+2)%4] and edges[(i+2)%4] == solvedEdges[(i+1)%4] and edges[(i+3)%4] == solvedEdges[(i+3)%4]): #9
            commands = [[5,3],[3,3],[1,2],[3,1],[1,1],[3,3],[1,2],[5,1],[1,3],[3,1],[1,1]] #L' R' U2 R (U R') U2 (L U' R) [1,1] WAS ADDED LATER
        # shift commands to the correct perspective
        if len(commands) > 0:
            #print commands
            for command in commands:
                if (command[0] != 1 and command[0] != 6):
                    rotateSide(((i+command[0]-2) % 4)+2,command[1])
                else:
                    rotateSide(command[0],command[1])
            break;
    commands = []
    return

def mMod(number): # behaves like modulo 4, initially expected I needed something else, was too lazy to replace: mMod(...) by: (...) % 4
    if number < 0:
        return number + 4
    elif number > 3:
        return number - 4
    else:
        return number

#############################################################################################################################################
#####################################################     Solve bottom cross       ##########################################################
#############################################################################################################################################

def getSolution(inputCorners, inputEdges):
    global corners
    corners = inputCorners
    global edges
    edges = inputEdges
    copyEdges = list(edges)
    copyCorners = list(corners)
    for i in range(4):
        topEdges = getEdges(1)
        underEdges = getEdges(6)
        underEdges2 = [edges[4],edges[5],edges[6],edges[7]] # in some cases this is more convenient
        # check if edge is already in correct positions
        if solvedEdges[i+4] == underEdges2[i]:
            pass
        # check if edge is in top layer (correct orientation)
        elif topEdges.count(solvedEdges[i+4]) > 0:
            rotation = topEdges.index(solvedEdges[i+4])-i
            rotateSide(1,mMod(rotation))
            rotateSide(i+2,2)
        # check if edge is in top layer (incorrect orientation)
        elif topEdges.count(flipSingleEdge(solvedEdges[i+4],1)) > 0:
            rotation = topEdges.index(flipSingleEdge(solvedEdges[i+4],1))-i+1
            #print "test edge case"
            if mMod(rotation) == 2:
                rotateSide(mMod(i+1)+2,3)
                rotateSide(mMod(i)+2,1)
                rotateSide(mMod(i+1)+2,1)
            else:
                rotateSide(1,mMod(rotation))
                rotateSide(mMod(i-1)+2,1)
                rotateSide(mMod(i)+2,3)
                rotateSide(mMod(i-1)+2,3)
        # check if single rotation (90 degrees) of F, R, B, L is enough
        elif (solvedEdges[i+4] == flipSingleEdge(edges[i+8],1) and i % 2 == 0) or (solvedEdges[i+4] == edges[i+8] and i % 2 == 1):
            rotateSide(mMod(i)+2,3)
        elif (solvedEdges[i+4] == flipSingleEdge(edges[mMod(i+1)+8],1) and i % 2 == 0) or (solvedEdges[i+4] == edges[mMod(i+1)+8] and i % 2 == 1):
            rotateSide(mMod(i)+2,1)
        # edge is in same position as the previous case but, now edge is flipped
        elif (solvedEdges[i+4] == edges[i+8] and i % 2 == 0) or (solvedEdges[i+4] == flipSingleEdge(edges[i+8],1) and i % 2 == 1):
            rotateSide(mMod(i-1)+2,3)
            rotateSide(1,3)
            rotateSide(mMod(i-1)+2,1) #maybe not necessary
            rotateSide(mMod(i)+2,2)
        elif (solvedEdges[i+4] == edges[mMod(i+1)+8] and i % 2 == 0) or (solvedEdges[i+4] == flipSingleEdge(edges[mMod(i+1)+8],1) and i % 2 == 1):
            rotateSide(mMod(i+1)+2,1)
            rotateSide(1,1)
            rotateSide(mMod(i+1)+2,3) #maybe not necessary
            rotateSide(mMod(i)+2,2)
        # check if edge is in middle layer, but on opposite side than desired
        elif (solvedEdges[i+4] == flipSingleEdge(edges[mMod(i+2)+8],1) and i % 2 == 0) or (solvedEdges[i+4] == edges[mMod(i+2)+8] and i % 2 == 1):
            rotateSide(mMod(i+2)+2,1)
            rotateSide(1,2)
            rotateSide(mMod(i+2)+2,3) #maybe not necessary
            rotateSide(mMod(i)+2,2)
        elif (solvedEdges[i+4] == flipSingleEdge(edges[mMod(i+3)+8],1) and i % 2 == 0) or (solvedEdges[i+4] == edges[mMod(i+3)+8] and i % 2 == 1):
            rotateSide(mMod(i+2)+2,3)
            rotateSide(1,2)
            rotateSide(mMod(i+2)+2,1) #maybe not necessary
            rotateSide(mMod(i)+2,2)
        # check if edge is in middle layer, but on opposite side than desired and flipped
        elif (solvedEdges[i+4] == (edges[mMod(i+2)+8]) and i % 2 == 0) or (solvedEdges[i+4] == flipSingleEdge(edges[mMod(i+2)+8],1) and i % 2 == 1):
            rotateSide(mMod(i+1)+2,3)
            rotateSide(1,1)
            rotateSide(mMod(i+1)+2,1) #maybe not necessary
            rotateSide(mMod(i)+2,2)
        elif (solvedEdges[i+4] == (edges[mMod(i+3)+8]) and i % 2 == 0) or (solvedEdges[i+4] == flipSingleEdge(edges[mMod(i+3)+8],1) and i % 2 == 1):
            rotateSide(mMod(i+3)+2,1)
            rotateSide(1,3)
            rotateSide(mMod(i+3)+2,3) #maybe not necessary
            rotateSide(mMod(i)+2,2)
        # check if edge is in bottom layer, wrong position, correct orientation
        elif underEdges.count(solvedEdges[i+4]) > 0:
            rotation = underEdges2.index(solvedEdges[i+4]) - i
            rotateSide(mMod(rotation + i)+2,2)
            rotateSide(1,mMod(rotation))
            rotateSide(i+2,2)
        # check if edge is in bottom layer, incorrect orientation
        elif underEdges2.count(flipSingleEdge(solvedEdges[i+4],1)) > 0:
            rotation = underEdges2.index(flipSingleEdge(solvedEdges[i+4],1)) - i + 1
            side = mMod(underEdges2.index(flipSingleEdge(solvedEdges[i+4],1)))
            rotateSide(side%4 + 2,3)
            if mMod(rotation) == 0:
                rotateSide((side+1)%4 + 2,3)
            else:
                rotateSide((side+1)%4 + 2,1)
                rotateSide(1,mMod(rotation))
                rotateSide((side+1)%4 + 2,3)
                rotateSide(i+2,2)
        # print message if no algorithm was found
        else:
            print "command not found"

#firstStage = len(listOfCommands)
#print "Number of face rotations in phase 1: " + str(firstStage)

#############################################################################################################################################
#################################################     Solve first two layers       ##########################################################
#############################################################################################################################################

    #drawCube(win)
    for i in range(4):
        commands = []
        #print "current iteration: " + str(i)
        # check if both corner and edge are already correct
        if (edges[i+8] == solvedEdges[i+8] and corners[i+4] == solvedCorners[i+4]):
            #print "case " + str(1)
            pass
        elif (findSingleEdge(solvedEdges[i+8]) == i+8 and findSingleCorner(solvedCorners[i+4]) == i+4):
            #print "case " + str(2)
            # check if corner and edge in correct position, incorrect orientation
            if (edges[i+8] == flipSingleEdge(solvedEdges[i+8],1) and corners[i+4] == solvedCorners[i+4]): #ConF2L_1 #2
                commands = [[3,1],[1,3],[3,1],[1,2],[2,1],[3,2],[2,3],[1,2],[3,2]]
            elif solvedEdges[i+8] == edges[i+8] and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],3): #ConF2L_2 1 #4
                commands = [[3,2],[1,2],[3,3],[1,3],[3,1],[1,3],[3,3],[1,2],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i+8],1) and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],3): #ConF2L_2 2 #2
                commands = [[3,1],[1,3],[3,1],[1,1],[4,1],[1,3],[4,3],[3,2]]
            elif solvedEdges[i+8] == edges[i+8] and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],1): #ConF2L_3 1 #4
                commands = [[3,1],[1,2],[3,1],[1,1],[3,3],[1,1],[3,1],[1,2],[3,2]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i+8],1) and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],1): #ConF2L_3 2 #2
                commands = [[3,2],[4,1],[1,1],[4,3],[1,3],[3,3],[1,1],[3,3]]
        elif (findSingleEdge(solvedEdges[i+8]) == i+8 and findSingleCorner(solvedCorners[i+4]) != i+4):
            #print "case " + str(3)
            # check if edge in correct position, corner in incorrect position
            if findSingleCorner(solvedCorners[i+4]) > 3:
                side = findSingleCorner(solvedCorners[i+4])-2
                rotateSide(side,1)
                rotateSide(1,1)
                rotateSide(side,3)
            rotateSide(1,(findSingleCorner(solvedCorners[i+4])-i)%4)
            # check if edge in correct position, corner in upper layer
            if solvedEdges[i+8] == edges[i+8] and solvedCorners[i+4] == corners[i]: #InsertC_1 1 #8
                commands = [[3,2],[1,1],[3,2],[1,1],[3,2],[1,2],[3,2]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i+8],1) and solvedCorners[i+4] == corners[i]: #InsertC_1 2 #5
                commands = [[2,3],[1,1],[2,1],[3,1],[1,2],[3,3]]
            elif solvedEdges[i+8] == edges[i+8] and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #InsertC_2 1 #5 A
                commands = [[1,2],[3,1],[4,1],[1,2],[4,3],[1,2],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i+8],1) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #InsertC_2 2 #6
                commands = [[1,3],[3,1],[1,1],[3,3],[1,1],[2,3],[1,3],[2,1]]
            elif solvedEdges[i+8] == edges[i+8] and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #InsertC_3 1 #8 B
                commands = [[1,3],[3,1],[1,2],[3,3],[1,1],[3,1],[1,1],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i+8],1) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #InsertC_3 2 #5
                commands = [[1,1],[2,3],[1,3],[2,1],[1,3],[3,1],[1,1],[3,3]]
        elif(findSingleEdge(solvedEdges[i+8]) != i+8 and findSingleCorner(solvedCorners[i+4]) == i+4):
            #print "case " + str(4)
            # check if corner is in correct position, edge in incorrect position
            side = findSingleEdge(solvedEdges[i+8]) - 6
            if findSingleEdge(solvedEdges[i+8]) > 3:
                rotateSide(side,1)
                rotateSide(1,1)
                rotateSide(side,3)
            rotation = 0
            if edges.count(flipSingleEdge(solvedEdges[i+8],i%2))>0:
                rotation = edges.index(flipSingleEdge(solvedEdges[i+8],i%2))-i+1
            else:
                rotation = edges.index(flipSingleEdge(solvedEdges[i+8],(1+i)%2))-i
            rotateSide(1,rotation % 4)
            # check if corner is in correct position, edge in upper layer
            if (solvedEdges[i+8] == flipSingleEdge(edges[i],(1+i)%2) and corners[i+4] == solvedCorners[i+4]): #InsertE_1 #3
                commands = [[4,3],[3,2],[1,3],[3,3],[1,1],[3,2],[4,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],i%2) and corners[i+4] == solvedCorners[i+4]: #InsertE_1 #5
                commands = [[1,1],[3,1],[1,1],[3,3],[1,3],[2,3],[1,3],[2,1]]
            elif (solvedEdges[i+8] == flipSingleEdge(edges[i],(1+i)%2)) and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],3): #InsertE_2 1 #4
                commands = [[3,1],[1,3],[3,2],[2,1],[3,1],[2,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],3): #InsertE_2 2 #8
                commands = [[2,3],[1,3],[2,1],[1,1],[2,3],[1,3],[2,1]]
            elif (solvedEdges[i+8] == flipSingleEdge(edges[i],(1+i)%2)) and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],1): #InsertE_3 1 #8
                commands = [[3,1],[1,1],[3,3],[1,3],[3,1],[1,1],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i+4],1): #InsertE_3 2 #5
                commands = [[3,1],[1,2],[3,3],[2,3],[1,2],[2,1]]
        elif(findSingleEdge(solvedEdges[i+8]) != i+8 and findSingleCorner(solvedCorners[i+4]) != i+4):
            #print "case " + str(5)
            # check if both corner and edge are in incorrect position
            if (findSingleEdge(solvedEdges[i+8]) > 3 and findSingleCorner(solvedCorners[i+4]) > 3):
                if (findSingleEdge(solvedEdges[i+8])-4 == findSingleCorner(solvedCorners[i+4])):
                    # check if both corner and edge are connected in F2L in incorrect position
                    side = findSingleCorner(solvedCorners[i+4])-2
                    rotateSide(side,1)
                    rotateSide(1,1)
                    rotateSide(side,3)
            if findSingleCorner(solvedCorners[i+4]) > 3:
                side = findSingleCorner(solvedCorners[i+4])-2
                if ((findSingleCorner(solvedCorners[i+4])-3)%4) == findSingleEdge(solvedEdges[i+8]):
                    rotateSide(side,1)
                    rotateSide(1,3)
                    rotateSide(side,3)
                else:
                    rotateSide(side,1)
                    rotateSide(1,1)
                    rotateSide(side,3)
            if (findSingleEdge(solvedEdges[i+8]) > 3):
                side = findSingleEdge(solvedEdges[i+8])-6
                if (((findSingleEdge(solvedEdges[i+8])-8)%4) == findSingleCorner(solvedCorners[i+4])):
                    rotateSide(side,1)
                    rotateSide(1,3)
                    rotateSide(side,3)
                else:
                    rotateSide(side,1)
                    rotateSide(1,1)
                    rotateSide(side,3)
            rotateSide(1,(findSingleCorner(solvedCorners[i+4])-i)%4) #move corner to correct position
            # check if both corner and edge are in upper layer and connected
            if solvedEdges[i+8] == flipSingleEdge(edges[i],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #conU_1a 1 #6
                commands = [[3,3],[2,1],[3,1],[2,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #conU_1a 2 #3
                commands = [[2,3],[1,1],[5,3],[1,2],[5,1],[1,2],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #conU_2a 1 #8
                commands = [[1,3],[3,1],[1,3],[3,3],[1,1],[3,1],[1,1],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #conU_2a 2 #7
                commands = [[2,3],[5,3],[4,3],[1,1],[4,1],[5,1],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i],(1+i)%2) and solvedCorners[i+4] == corners[i]: #conU_3a 1 #8
                commands = [[3,1],[1,2],[3,3],[1,3],[3,1],[1,1],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[i],i%2) and solvedCorners[i+4] == corners[i]: #conU_3a 2 #3
                commands = [[2,3],[1,3],[2,3],[5,1],[2,1],[5,3],[1,2],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #conU_1b 1 #6
                commands = [[2,1],[3,3],[2,3],[3,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #conU_1b 2 #3
                commands = [[3,1],[1,3],[4,1],[1,2],[4,3],[1,2],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #conU_2b 1 #8
                commands = [[1,1],[2,3],[1,1],[2,1],[1,3],[2,3],[1,3],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #conU_2b 2 #7
                commands = [[3,1],[4,1],[5,1],[1,3],[5,3],[4,3],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],i%2) and solvedCorners[i+4] == corners[i]: #conU_3b 1 #8
                commands = [[2,3],[1,2],[2,1],[1,1],[2,3],[1,3],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i-1)%4],(1+i)%2) and solvedCorners[i+4] == corners[i]: #conU_3b 2 #3
                commands = [[3,1],[1,1],[3,1],[4,3],[3,3],[4,1],[1,2],[3,3]]
            # check if both corner and edge are in upper layer and separated
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+2)%4],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #SepU_1a 1 #7
                commands = [[3,1],[1,1],[4,1],[1,2],[4,3],[1,1],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+2)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #SepU_1a 2 #8
                commands = [[2,3],[1,3],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+2)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #SepU_2a 1 #5
                commands = [[3,1],[5,1],[1,1],[2,1],[1,3],[2,3],[5,3],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+2)%4],(i+1)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #SepU_2a 2 #2
                commands = [[3,1],[1,3],[4,1],[1,1],[4,3],[1,2],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+2)%4],(1+i)%2) and solvedCorners[i+4] == corners[i]: #SepU_3a 1 #4
                commands = [[3,1],[4,1],[1,2],[4,3],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+2)%4],i%2) and solvedCorners[i+4] == corners[i]: #SepU_3a 2 #2
                commands = [[1,3],[2,3],[1,2],[2,2],[3,3],[2,3],[3,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+1)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #SepU_1b 1 #7
                commands = [[2,3],[1,3],[5,3],[1,2],[5,1],[1,3],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+1)%4],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],3): #SepU_1b 2 #8
                commands = [[3,1],[1,1],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+1)%4],(1+i)%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #SepU_2b 1 #3
                commands = [[1,2],[3,1],[4,1],[1,1],[4,3],[1,2],[3,3]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+1)%4],i%2) and solvedCorners[i+4] == rotateSingleCorner(corners[i],1): #SepU_2b 2 #2
                commands = [[2,3],[1,1],[5,3],[1,3],[5,1],[1,2],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+1)%4],i%2) and solvedCorners[i+4] == corners[i]: #SepU_3b 1 #3
                commands = [[2,3],[5,3],[1,2],[5,1],[2,1]]
            elif solvedEdges[i+8] == flipSingleEdge(edges[(i+1)%4],(1+i)%2) and solvedCorners[i+4] == corners[i]: #SepU_3b 2 #2
                commands = [[1,1],[3,1],[1,2],[3,2],[2,1],[3,1],[2,3]]
            else:
                print "Command not found"
        else:
            print "Command not found"
        #shift the algorithm to the correct perspective
        if len(commands) > 0:
            for command in commands:
                if (command[0] != 1 and command[0] != 6):
                    rotateSide(((i-1+command[0]-2) % 4)+2,command[1])
                else:
                    rotateSide(command[0],command[1])
        #print "Final state this iteration:"

    #drawCube(win)
    #win.getMouse()
    #secondStage = len(listOfCommands) - firstStage
    #print "Number of face rotations in phase 2: " + str(secondStage)

    #############################################################################################################################################
    #################################################     Orientation last layer       ##########################################################
    #############################################################################################################################################

    commands = []
    for i in range(4):
        # first generate lists which contain the orientation of the edges and corners
        upperEdges = getEdges(1)
        upperCorners = [corners[0],corners[1],corners[2],corners[3]]
        #print "current iteration: " + str(i)
        for q in range(i):
            upperEdges = rotateListOfFour(upperEdges)
            upperCorners = rotateListOfFour(upperCorners)
        edgesOrientation = []
        cornersOrientation = []
        for t in range(4):
            edgesOrientation.append(getEdgeOrientation(upperEdges[t]))
            cornersOrientation.append(getCornerOrientation(upperCorners[t]))
        #print edgesOrientation
        #print cornersOrientation
        # check if orientation is already correct
        if edgesOrientation == [0,0,0,0] and cornersOrientation == [0,0,0,0]:
            break
        # check which of the 57 algorithms should be used
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [2,1,2,1]: #1
            commands = [[3,1],[1,2],[3,2],[2,1],[3,1],[2,3],[1,2],[3,3],[2,1],[3,1],[2,3]] #(R U') U' (R2 F) (R F') U2 (R' F) (R F')
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [2,2,1,1]: #2
            commands = [[2,1],[3,1],[1,1],[3,3],[1,3],[2,3],[4,1],[1,1],[5,1],[1,3],[5,3],[4,3]]
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [1,0,1,1]: #3
            commands = [[5,3],[3,1],[4,3],[5,1],[1,2],[5,3],[4,3],[3,1],[4,3],[3,2],[5,1]]
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [0,2,2,2]: #4
            commands = [[5,3],[3,2],[4,1],[3,3],[4,1],[5,1],[1,2],[5,3],[4,1],[3,3],[5,1]]
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [2,0,1,0]: #5
            commands = [[3,1],[1,1],[3,3],[1,1],[3,3],[2,1],[3,1],[2,3],[1,2],[3,3],[2,1],[3,1],[2,3]] #R (U R' U) (R' F) (R F') U2 (R' F) (R F')
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [1,2,0,0]: #6
            commands = [[5,1],[2,1],[3,3],[2,1],[3,1],[2,2],[5,2],[4,3],[3,1],[4,3],[3,3],[4,2],[5,1]]
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [2,1,0,0]: #7
            commands = [[5,3],[4,2],[3,1],[4,1],[3,3],[4,1],[5,2],[2,2],[3,3],[2,3],[3,1],[2,3],[5,3]]
        elif edgesOrientation == [1,1,1,1] and cornersOrientation == [0,0,0,0]: #8
            commands = [[5,3],[3,1],[4,1],[3,1],[4,1],[3,3],[4,3],[5,2],[3,2],[2,1],[3,1],[2,3],[5,3]]
        elif edgesOrientation == [0,1,0,1] and cornersOrientation == [2,1,2,1]: #9
            commands = [[3,1],[1,2],[3,2],[1,3],[3,1],[1,3],[3,3],[1,2],[2,1],[3,1],[2,3]] #(R U') U' (R2 U') (R U') (R' U) U F (R F')
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [2,1,2,1]: #10
            commands = [[2,1],[3,1],[1,1],[3,3],[1,3],[3,1],[2,3],[5,1],[2,1],[3,3],[2,3],[5,3]]
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [1,1,2,2]: #11
            commands = [[2,1],[1,1],[3,1],[1,3],[3,3],[1,1],[3,1],[1,3],[3,3],[2,3]] #F U (R U') (R' U) (R U') R' F'
        elif edgesOrientation == [0,1,0,1] and cornersOrientation == [1,1,2,2]: #12
            commands = [[3,3],[1,3],[3,1],[1,3],[3,3],[1,1],[2,3],[1,1],[2,1],[3,1]]
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [1,2,1,2]: #13
            commands = [[5,1],[2,2],[3,3],[2,3],[3,1],[2,1],[3,3],[2,3],[3,1],[2,3],[5,3]]
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [1,2,1,2]: #14
            commands = [[5,3],[4,2],[3,1],[4,1],[3,3],[4,3],[3,1],[4,1],[3,3],[4,1],[5,1]]
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [1,1,2,2]: #15
            commands = [[3,1],[4,3],[3,2],[2,1],[3,2],[4,1],[3,2],[2,3],[3,1]] #R B') (R2 F) R2 (B R2) (F' R)
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [1,1,2,2]: #16
            commands = [[3,3],[2,1],[3,2],[4,3],[3,2],[2,3],[3,2],[4,1],[3,3]] #R' F) (R2 B') (R2 F') R2 (B R')
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [2,2,1,1]: #17
            commands = [[2,1],[3,1],[1,1],[3,3],[1,3],[3,1],[1,1],[3,3],[1,3],[2,3]] #F R (U R') U' R (U R') U' F'
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [2,2,1,1]: #18
            commands = [[4,3],[3,3],[1,3],[3,1],[1,1],[3,3],[1,3],[3,1],[1,1],[4,1]] #B' R' U' R (U R') U' R U B
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [0,2,2,2]: #19
            commands = [[5,1],[2,1],[3,3],[2,1],[3,1],[2,2],[5,3]]
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [1,1,1,0]: #20
            commands = [[5,3],[4,3],[3,1],[4,3],[3,3],[4,2],[5,1]]
        elif edgesOrientation == [1,0,0,1] and cornersOrientation == [1,1,1,0]: #21
            commands = [[5,1],[3,2],[2,3],[3,1],[2,3],[3,3],[2,2],[3,1],[2,3],[3,1],[5,3]]
        elif edgesOrientation == [0,0,1,1] and cornersOrientation == [0,2,2,2]: #22
            commands = [[5,3],[3,2],[4,1],[3,3],[4,1],[3,1],[4,2],[3,3],[4,1],[3,3],[5,1]]
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [1,0,1,1]: #23
            commands = [[3,3],[1,3],[3,1],[2,1],[3,3],[2,3],[1,1],[2,1],[3,1],[2,3]] #R' U' R F R' F' U F (R F')
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [2,2,0,2]: #24
            commands = [[3,1],[1,1],[3,3],[4,3],[3,1],[4,1],[1,3],[4,3],[3,3],[4,1]]
        elif edgesOrientation == [0,0,1,1] and cornersOrientation == [2,0,2,2]: #25 TESTING
            commands = [[5,3],[4,2],[3,1],[4,1],[3,3],[4,1],[5,1]]
        elif edgesOrientation == [1,0,0,1] and cornersOrientation == [1,1,0,1]: #26
            commands = [[5,1],[2,2],[3,3],[2,3],[3,1],[2,3],[5,3]]
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [0,2,2,2]: #27
            commands = [[2,1],[1,1],[3,1],[1,2],[3,3],[1,3],[3,1],[1,1],[3,3],[2,3]] #F U (R U') U' R' U' R (U R') F'
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [1,0,1,1]: #28
            commands = [[3,3],[2,1],[3,1],[1,1],[3,3],[2,3],[3,1],[2,1],[1,3],[2,3]] #R' F) R (U R') F' R F U' F'
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [1,1,0,1]: #29
            commands = [[5,1],[2,1],[5,3],[3,1],[1,1],[3,3],[1,3],[5,1],[2,3],[5,3]]
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [2,2,2,0]: #30
            commands = [[3,3],[2,3],[3,1],[5,3],[1,3],[5,1],[1,1],[3,3],[2,1],[3,1]]
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [0,0,1,2]: #31
            commands = [[3,1],[1,1],[3,3],[1,1],[3,1],[1,2],[3,3],[2,1],[3,1],[1,1],[3,3],[1,3],[2,3]] #R (U R' U) (R U') U' (R' F) R (U R') U' F'
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [1,2,0,0]: #32
            commands = [[3,3],[1,3],[3,1],[1,1],[2,1],[3,1],[1,1],[3,3],[1,3],[3,3],[1,1],[3,1],[1,3],[2,3]] #R' U' R U F R (U R') U' (R' U) (R U') F'
        elif edgesOrientation == [0,0,1,1] and cornersOrientation == [2,1,0,0]: #33
            commands = [[3,2],[1,1],[3,3],[4,3],[3,1],[1,3],[3,2],[1,1],[3,1],[4,1],[3,3]] #R2 (U R') B' (R U') (R2 U) R (B R')
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [1,0,0,2]: #34
            commands = [[3,1],[1,1],[3,3],[1,3],[3,1],[1,3],[3,3],[2,3],[1,3],[2,1],[3,1],[1,1],[3,3]] #R (U R') U' (R U') R' F' U' F R (U R')
        elif edgesOrientation == [0,0,1,1] and cornersOrientation == [1,0,0,2]: #35
            commands = [[3,1],[1,1],[4,3],[1,3],[3,3],[1,1],[3,1],[4,1],[3,3]] #R U B' U' (R' U) R (B R')
        elif edgesOrientation == [1,0,0,1] and cornersOrientation == [1,0,0,2]: #36
            commands = [[3,3],[1,3],[2,1],[1,1],[3,1],[1,3],[3,3],[2,3],[3,1]] #R' U' F U (R U') R' (F' R)
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [1,0,2,0]: #37
            commands = [[2,1],[3,1],[1,3],[3,3],[1,3],[3,1],[1,1],[3,3],[2,3]] #F (R U') R' U' R (U R') F'
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [0,1,2,0]: #38
            commands = [[2,1],[1,1],[3,1],[1,3],[3,3],[2,3]] #F U (R U') R' F'
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [0,1,2,0]: #39
            commands = [[4,3],[1,3],[3,3],[1,1],[3,1],[4,1]] #B' U' (R' U) R B
        elif edgesOrientation == [0,0,1,1] and cornersOrientation == [1,0,2,0]: #40
            commands = [[3,1],[1,2],[3,2],[2,1],[3,1],[2,3],[3,1],[1,2],[3,3]] #(R U') U' (R2 F) (R F') (R U') U' R'
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [2,0,0,1]: #41
            commands = [[2,1],[3,1],[1,1],[3,3],[1,3],[2,3]] #F R (U R') U' F'
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [1,0,0,2]: #42
            commands = [[3,1],[1,1],[3,3],[1,3],[3,3],[2,1],[3,1],[2,3]] #R U R' U' (R' F) (R F')
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [0,2,0,1]: #43
            commands = [[3,1],[4,3],[3,3],[1,3],[3,1],[1,1],[4,1],[1,3],[3,3]] #(R B') R' U' R U B U' R'
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [2,0,1,0]: #44
            commands = [[3,3],[2,1],[3,1],[1,1],[3,3],[1,3],[2,3],[1,1],[3,1]] #(R' F) R (U R') U' F' U R
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [0,0,2,1]: #45
            commands = [[3,1],[1,1],[3,3],[1,3],[4,3],[3,3],[2,1],[3,1],[2,3],[4,1]] #R (U R') U' B' (R' F) R S
        elif edgesOrientation == [0,1,0,1] and cornersOrientation == [0,1,2,0]: #46
            commands = [[3,3],[1,3],[3,3],[2,1],[3,1],[2,3],[1,1],[3,1]] #R' U' (R' F) (R F') U R
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [0,1,0,2]: #47
            commands = [[3,1],[1,1],[3,3],[1,1],[3,1],[1,3],[3,3],[1,3],[3,3],[2,1],[3,1],[2,3]] #R (U R' U) (R U') R' U' (R' F) (R F')
        elif edgesOrientation == [0,1,1,0] and cornersOrientation == [1,0,2,0]: #48
            commands = [[3,3],[1,3],[3,1],[1,3],[3,3],[1,1],[3,1],[1,1],[3,1],[4,3],[3,3],[4,1]] #R' U' (R U') (R' U) (R U) (R B') (R' B)
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [1,2,1,2]: #49
            commands = [[3,1],[1,2],[3,3],[1,3],[3,1],[1,1],[3,3],[1,3],[3,1],[1,3],[3,3]] #(R U') U' R' U' R U R' U' (R U') R'
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [2,2,1,1]: #50
            commands = [[3,1],[1,2],[3,2],[1,3],[3,2],[1,3],[3,2],[1,2],[3,1]] #(R U') U' (R2 U') (R2 U') (R2 U') U' R
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [0,0,1,2]: #51
            commands = [[3,3],[1,2],[3,1],[2,1],[1,3],[3,3],[1,3],[3,1],[1,1],[2,3]] #R' U2 R F U' R' U' R U F'
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [1,0,0,2]: #52
            commands = [[5,1],[2,1],[3,3],[2,3],[5,3],[2,1],[3,1],[2,3]]
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [0,2,0,1]: #53
            commands = [[2,3],[5,1],[2,1],[3,3],[2,3],[5,3],[2,1],[3,1]]
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [1,1,0,1]: #54
            commands = [[3,1],[1,2],[3,3],[1,3],[3,1],[1,3],[3,3]] #R U (U R') U' (R U') R'
        elif edgesOrientation == [0,0,0,0] and cornersOrientation == [0,2,2,2]: #55
            commands = [[3,1],[1,1],[3,3],[1,1],[3,1],[1,2],[3,3]] #R (U R' U) (R U') U' R'
        elif edgesOrientation == [1,1,0,0] and cornersOrientation == [0,0,0,0]: #56
            commands = [[5,1],[2,1],[3,3],[2,3],[5,3],[3,1],[1,1],[3,1],[1,3],[3,3]]
        elif edgesOrientation == [1,0,1,0] and cornersOrientation == [0,0,0,0]: #57
            commands = [[3,1],[1,1],[3,3],[1,3],[5,1],[3,3],[2,1],[3,1],[2,3],[5,3]]
        else:
            pass
        # shift the commands to the correct perspective
        if len(commands) > 0:
            for command in commands:
                if (command[0] != 1 and command[0] != 6):
                    rotateSide(((i+command[0]-2) % 4)+2,command[1])
                else:
                    rotateSide(command[0],command[1])
            break;
    #print commands

    #thirdStage = len(listOfCommands) - firstStage - secondStage
    #print "Number of face rotations in phase 3: " + str(thirdStage)

    #############################################################################################################################################
    #################################################     Permutation last layer       ##########################################################
    #############################################################################################################################################
                    
    # solve the cube using standard algorithms
    solveFinalPhase()
    # in rare cases the cube is not yet solved, check if it is solved
    if (edges != solvedEdges or corners != solvedCorners):
        solveFinalPhase2() #this algorithm will at best solve all the corners, not the edges
        solveFinalPhase()
    if (edges != solvedEdges or corners != solvedCorners):
        solveFinalPhase3() #this algortihm will at best solve all the edges, not the corners
        solveFinalPhase()

    #If none of the above worked, this will solve at least one corner
    if (edges != solvedEdges or corners != solvedCorners):
        check = 0
        for i in range(4):
            if (corners[i] != solvedCorners[i] and corners[(i+1)%4] != solvedCorners[(i+1)%4] and corners[(i+2)%4] != solvedCorners[(i+2)%4] and corners[(i+3)%4] != solvedCorners[(i+3)%4]):
                check = check + 1
        if check == 4:
            for i in range(4):
                if corners[(i+1)%4] == solvedCorners[(i+3)%4]:
                    commands = [[3,3],[2,1],[3,3],[4,2],[3,1],[2,3],[3,3],[4,2],[3,2]]
                elif corners[(i+1)%4] == solvedCorners[(i+2)%4]:
                    commands = [[3,2],[4,2],[3,1],[2,1],[3,3],[4,2],[3,1],[2,3],[3,1]]
                elif corners[(i+1)%4] == solvedCorners[i]:
                    commands = [[2,1],[3,3],[2,3],[5,1],[2,1],[3,1],[2,3],[5,2],[4,3],[3,1],[4,1],[5,1],[4,3],[3,3],[4,1]]
                if len(commands) > 0:
                    for command in commands:
                        if (command[0] != 1 and command[0] != 6):
                            rotateSide(((i+command[0]-2) % 4)+2,command[1])
                        else:
                            rotateSide(command[0],command[1])
                    break;

    commands = []
    # try again to solve the cube
    if (edges != solvedEdges or corners != solvedCorners):
        solveFinalPhase()
    if (edges != solvedEdges or corners != solvedCorners):
        solveFinalPhase2() #this algorithm will at best solve all the corners, not the edges
        solveFinalPhase()
    if (edges != solvedEdges or corners != solvedCorners):
        solveFinalPhase3() #this algortihm will at best solve all the edges, not the corners
        solveFinalPhase()
    if (edges != solvedEdges or corners != solvedCorners):
        print "Command not found"
    
    #print listOfCommands
    #finalStage = len(listOfCommands) - firstStage - secondStage - thirdStage
    #print "Number of face rotations in phase 4: " + str(finalStage)

    newCommands = []
    includeNextIndex = True
    #print listOfCommands
    #print "Number of face rotations in full solution: " + str(len(listOfCommands))

    for z in range(len(listOfCommands)-1):
        if includeNextIndex == True:
            if listOfCommands[z][0] == listOfCommands[z+1][0]:
                newCommand = [listOfCommands[z][0],(listOfCommands[z][1]+listOfCommands[z+1][1])%4]
                if newCommand[1] != 0:
                    newCommands.append(newCommand)
                includeNextIndex = False
            else:
                newCommands.append(listOfCommands[z])
        else:
            includeNextIndex = True
    if includeNextIndex == True:
        newCommands.append(listOfCommands[-1])
    #print newCommands        
    print "Solution found! Requires " + str(len(newCommands)) + " moves"
    edges = copyEdges
    corners = copyCorners
    print edges
    print corners
    edgesStates = []
    cornersStates = []
    for command in newCommands:
        rotateSide(command[0],command[1])
        currentEdges = list(edges)
        currentCorners = list(corners)
        edgesStates.append(currentEdges)
        cornersStates.append(currentCorners)
        
    return newCommands, cornersStates, edgesStates

